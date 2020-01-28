# Echo client program
import socket
from threading import Thread

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STAMP)
s.connect((HOST, PORT))

def enviar(s):
    while True:
        text_client = raw_input('Que vols enviar?')
        s.sendall(text_client) 

def rebre(s):
    dade = s.recv(1024)
    print dades
    if dades == 'Bye':
        sys.exit()

tenv = Thread(target=enviar, args=(s,))
treb = Thread(target=rebre, args=(s,))
tenv.start()
treb.start()

s.close()
