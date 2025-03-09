import nacl.public
from websockets.sync.client import connect as Websocket

class Client:
  def __init__(self, host='127.0.0.1', port=28, privkey=None, pubkey=None):
    self.socket = Websocket(f'ws://{host}:{port}')
    if privkey and pubkey:
      self.privkey = privkey
      self.pubkey = pubkey
    else:
      self.privkey = nacl.public.PrivateKey.generate()
      self.pubkey = self.privkey.public_key
    self.dec = nacl.public.SealedBox(self.privkey)
    self.sever_pubkey = nacl.public.PrivateKey(self.socket.recv()[7:])
    self.enc = nacl.public.SealedBox(self.sever_pubkey)
    self.socket.send(self.enc.encrypt(b'PUBKEY ' + self.pubkey._public_key))

  def get(self, route):
    self.socket.send(self.enc.encrypt(b'GET ' + route.encode()))
    response = self.dec.decrypt(self.socket.recv()).split(b'\n')
    sep = response.index(b'!msg:')

    headersList = response[:sep]
    headers = {}
    for header in headersList:
      key, value = header.split(b': ')
      headers[key] = value

    return Client.Response(headers, response[sep+1], b'\n'.join(response[sep+2:]))

  def post(self, route, data):
    pass
    # self.socket.send(enc.encrypt(b'POST ' + data.encode()))

  class Response:
    def __init__(self, headers, status, message):
      self.headers = headers
      self.status = status
      self.status_code = int(status.split(' ')[0])
      self.message = message

    def __repr__(self):
      return f'<Phoenix Webserver Response {self.status}>'

    def __str__(self):
      return self.headers.decode()
