
from http.server import HTTPServer, BaseHTTPRequestHandler
import smtplib, ssl
import urllib

class Serv(BaseHTTPRequestHandler):

  def do_GET(self):
      if self.path == '/g.jpg':

          file_to_open = open('g.jpg','rb')
          self.send_response(200)
          self.send_header("Content-type", "image/jpg")
          self.end_headers()
          self.wfile.write(file_to_open.read())

          send_email(self.client_address)
      else:
          self.send_response(404,"Not found")
          self.send_header("Content-type", "text/html")
          self.end_headers()
          self.wfile.write(bytes("<html><head><title>Error 404</title></head><body><h1>404 Not found.l.</h1></body></html>", 'utf8'))

  def send_email(addr):

      context = ssl.create_default_context()
      pswd = "practica20"
      smtp = smtplib.SMTP_SSL("stmp.gmail.com", 465)
      smtp.ehlo()
      smtp.login("laytonyorguin@gmail.com", "practica20")
      msg = "Subject: Visitas " + "\n\n\nLa següent adreça " + str(addr) + " ha vist la imatge."
      stmp.sendmail("laytonyorguin@gmail.com", "laytonyorguin@gmail.com", msg)
      smtp.quit()


if __name__ == '__main__':

    httpd = HTTPServer(('127.0.0.1', 8080), Serv)
    httpd.serve_forever()
