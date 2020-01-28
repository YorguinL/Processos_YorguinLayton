# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))

while True:
    text = raw_input('Introdueix text:')
    s.sendall(text)
    if text == 'Bye':
        break

s.close()
