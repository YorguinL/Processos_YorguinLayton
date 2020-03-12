
from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

  def do_GET(self):
      if self.path == '/practica.html':
          try:
              file_to_open = open('practica.html','rb')
              self.send_response(200)
              self.send_header("Content-type", "text/html")
              self.end_headers()
              self.wfile.write(file_to_open.read())
          except:
              print('Errror file')
      else:

          self.send_response(404,"Not found")
          self.send_header("Content-type", "text/html")
          self.end_headers()
          self.wfile.write(bytes("<html><head><title>Error 404</title></head><body><h1>404 Not found.l.</h1></body></html>", 'utf8'))


httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()
