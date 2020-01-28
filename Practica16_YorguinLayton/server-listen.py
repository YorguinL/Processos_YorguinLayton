# Echo server program
import socket
import time
from threading import Thread

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STAMP)
s.bind((HOST, PORT))

def enviar(s):
    while True:
        text_servidor = raw_input('Que vols enviar?')
        s.sendall(text_servidor) 

def rebre(s):
    dades = s.recv(1024)
    print dades
    if dades == 'Bye':
        sys.exit()

while True:
    rebre()

tenv = Thread(target=enviar args=(s,))     
treb = Thread(target=rebre args=(s,))
tenv.start()
treb.start()

s.close()




