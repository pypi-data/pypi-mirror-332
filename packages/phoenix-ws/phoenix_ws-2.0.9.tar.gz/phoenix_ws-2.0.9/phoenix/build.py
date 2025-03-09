from .minify import html_minify, js_minify, css_minify
import os, mimetypes

# Read a file from the filesystem
def readfile(dir, config):
  try:
    # Read the file as plaintext
    f = open(dir)
    data = f.read()
  except UnicodeDecodeError:
    # Read the file as binary
    f = open(dir, 'rb')
    data = f.read()
  f.close()
  
  # Get mimetype from file extension
  mime = str(mimetypes.guess_type(dir)[0])
  
  # Minify the file
  if config["minify"]:
    try:
      # Minify HTML, CSS, and JS
      if mime == "text/html":
        data = html_minify(data)
      elif mime == "text/css":
        data = css_minify(data)
      elif mime == "text/js":
        data = js_minify(data)
    except Exception as e:
      print(f"[Error] {str(e)}")
  
  # Return the mimetype and data
  return {
    "mime": mime,
    "cont": data
  }

# Traverse a directory and add all files to the cache
def directoryTraverse(dir="./", urldir="/", indexDirectories=False, cache={}, config={}):
  # Print the directory being traversed if verbose
  if config["verbose"]:
    print(f"[Build] traversing static directory {dir} ({urldir})")
  
  index_dir = ""
  
  # Iterate through each item in the directory
  dir_ls = os.listdir(dir)
  for f in dir_ls:
    if config["verbose"]:
      print("[Build] reading "+dir+f+" ("+urldir+f+")")
    if os.path.isfile(dir+f):
      # Run readfile() on the file
      cache[urldir+f] = readfile(dir+f, config)
      # Add an entry to the indexed list
      if indexDirectories:
        index_dir += f"<a href='{urldir+f}'>File: {f}</a><br>"
        if config["verbose"]:
          print(f"[Build] indexed file {dir+f} ({urldir+f})")
    else:
      # Recursively traverse the directory
      directoryTraverse(dir+f+"/", urldir+f+"/", indexDirectories, cache, config)
      
      # Check if the directory contains an index.html file, and read it if it does
      if os.path.exists(dir+f+"/index.html") and os.path.isfile(dir+f+"/index.html"):
        cache[urldir+f+'/'] = readfile(dir+f+"/index.html", config)
      elif indexDirectories:
        # Index the directory
        index_dir += f"<a href='{urldir+f}'>Dir: {f}</a><br>"
        if config["verbose"]:
          print("[Build] indexed subdir "+dir+f+" ("+urldir+f+")")
  if indexDirectories:
    # Add the indexed list to the cache
    cache[urldir] = {"mime": "text/html", "cont": f"<!DOCTYPE html><html><body><h1>Index of {urldir}</h1><div><a href=\"{urldir+'..'}\">Parent Directory</a><br>{index_dir}</div></body></html>"}

# Traverse the extensions' directories
def extensionTraverse(dir="./", urldir="/", cache={}, config={}, extensions={}):
  if config["verbose"]:
    print(f"[Build] traversing dynamic directory {dir} ({urldir})")
  
  # List the files in the directory
  dir_ls = os.listdir(dir)
  # Iterate through each file
  for f in dir_ls:
    if config["verbose"]:
      print("[Build] reading "+dir+f+" ("+urldir+f+")")
    
    # Check if the file is a directory and recursively traverse it
    if os.path.isfile(dir+f):
      for extension in extensions.keys():
        if hasattr(extensions[extension], 'srccompile_file'):
          print(f'[Info] Extension {extension}: srccompile_file')
          try:
            # Add the source files to the extension cache
            extensions[extension].srccompile_file(dir+f, urldir+f, cache, readfile, config)
          except Exception as e:
            print(f"[Error] Extension {extension} in srccompile phase: {e} (file: {dir+f}, url: {urldir+f})'")
    else:
      # Recursively traverse the directory
      extensionTraverse(dir+f+"/", urldir+f+"/", cache, config, extensions)
          
        

def build(indexDirectories=False, config={}, cache={}, extensions={}):
  for ext in extensions.keys():
    if hasattr(extensions[ext], 'prebuild'):
      print(f'[Info] Extension {extension}: prebuild')
      try:
        extensions[ext].prebuild(config, cache)
      except Exception as e:
        print(f'[Error] Extension {extension} in prebuild phase: {e}')


  # ./public/
  if os.path.exists("public"):
    # Traverse the public directory
    directoryTraverse("public/", "/", indexDirectories, cache, config)

  # ./src/
  if os.path.exists("src"):
    # Traverse the src directory
    extensionTraverse("src/", "/src/", cache, config, extensions)

  # ./phoenix_files/
  if os.path.exists("phoenix_files/modules"):
    # Traverse the phoenix_files directory
    directoryTraverse("phoenix_files/modules/", "/phoenix/modules/", config["indexPhoenix"], cache, config)

  # ./index.html
  if os.path.exists("public/index.html") and os.path.isfile("public/index.html"):
    # Add the index.html file to the cache
    index = open("public/index.html")
    cache["/"] = {
      "mime": "text/html",
      "cont": index.read()
    }
    index.close()
  elif not '/' in cache.keys() and not indexDirectories:
    # If indexDirectories is false, add a default index.html file to the cache
    cache["/"] = {
      "mime": "text/html",
      "cont": "<!DOCTYPE html>\n<html><head><!-- Default Phoenix Webpage --></head><body></body></html>"
    }

  for ext in extensions.keys():
    if hasattr(ext, 'postbuild'):
      print('[Info] Extension {ext}: postbuild')
      try:
        # Run the postbuild() function for each extension
        extensions[ext].postbuild(cache)
      except Exception as e:
        # Print an error if one occurs during the execution of the extension's postbuild() function
        print(f"[Error] Extension {ext} in postbuild phase: {e}")

  # Return the cached directory tree
  return cache
