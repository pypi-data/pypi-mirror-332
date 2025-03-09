import asyncio, base64, flask, json, nacl.public, os, sys, threading
from waitress import serve as WSGI_SERVER
from websockets.server import serve as WebSocketServer

routes = {}

class Server:
  def __init__(self, config={}, cache={}, host=False, httpport=8080, wsport=28, httpthreads=4):
    self.host = host
    self.httpport = httpport
    self.wsport = wsport
    self.httpthreads = httpthreads
    self.app = flask.Flask(__name__)
    self.app.secret_key = os.urandom(32)
    self.wsroutes = {}

    self.config = config
    self.cache = cache

    if 'privkey' in self.config and 'pubkey' in self.config:
      self.privkey = nacl.public.PrivateKey(base64.b64decode(config['privkey']))
      self.pubkey = nacl.public.PublicKey(base64.b64decode(config['pubkey']))
    else:
      self.privkey = nacl.public.PrivateKey.generate()
      self.pubkey = self.privkey.public_key
      self.config['privkey'] = base64.b64encode(self.privkey._private_key).decode()
      self.config['pubkey'] = base64.b64encode(self.pubkey._public_key).decode()

      file = open('config.phoenix', 'w')
      file.write(json.dumps(self.config))
      file.close()

    self.decrypt_key = nacl.public.SealedBox(self.privkey)

  async def wshandler(self, socket):
    await socket.send(b'PUBKEY ' + self.pubkey._public_key)
    client_pubkey = None

    async def send(data):
      if type(data) in (list, dict, tuple):
        data = json.dumps(data)
      if type(data) == str:
        data = data.encode()

      return await socket.send(client_pubkey.encrypt(data))

    async for message in socket:
      if type(message) == str:
        message = message.encode()
      message = self.decrypt_key.decrypt(message).strip()
      if message.startswith(b'PUBKEY '):
        client_pubkey = nacl.public.SealedBox(nacl.public.PublicKey(message[7:]))
      elif message.startswith(b'GET '):
        route = message[4:].decode()
        if route in self.cache:
          route = flask.Response(self.cache[route]['cont'], mimetype=self.cache[route]["mime"])
        elif route in self.wsroutes:
          route = self.wsroutes[route]()
        elif '404' in self.wsroutes:
          route = self.wsroutes['404']()
        else:
          route = flask.Response('404 Not Found', status=404, mimetype='text/html')

        if type(route) in (list, dict, tuple):
          route = json.dumps(route)
        if type(route) != flask.Response:
          route = flask.Response(route)

        await send(b'\n'.join([': '.join(x).encode() for x in route.headers]) + b'\n!msg:\n' + route.status.encode() + b'\n' + route.data)

  def route(self, path, methods=['GET']):
    def wrapper(func):
      self.wsroutes[path] = func
      self.app.route(path, methods=methods)(func)
      return func
    return wrapper

  async def runFlask(self):
    return await WSGI_SERVER(self.app, host=('0.0.0.0' if self.host else 'localhost'), port=self.httpport, ident='Phoenix', threads=self.httpthreads)

  def runWebsocket(self):
    async def wrapper():
      async with WebSocketServer(self.wshandler, '0.0.0.0' if self.host else 'localhost', self.wsport):
        await asyncio.Future()
    asyncio.run(wrapper())

  def run(self):
    httploop = asyncio.new_event_loop()
    httploop.create_task(self.runFlask())
    threading.Thread(target=httploop.run_forever, daemon=True).start()
    self.runWebsocket()
