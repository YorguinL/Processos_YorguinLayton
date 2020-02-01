
import socket
from threading import Thread
import missatge

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
conn, addr = s.accept()

t_env = Thread(target=missatge.enviar_missatge, args=(conn,))
t_reb = Thread(target=missatge.rebre_missatge, args=(conn,) )
t_env.deamon = True

t_env.start()
t_reb.start()

t_reb.join()

s.close()
