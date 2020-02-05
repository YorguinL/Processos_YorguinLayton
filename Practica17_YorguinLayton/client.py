
import socket
from threading import Thread
import missatge

HOST = 'localhost'    # The remote host
PORT = 50007          # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


t_env = Thread(target=missatge.enviar_missatge, args=(s,))
t_reb = Thread(target=missatge.rebre_missatge, args=(s,) )
t_env.daemon = True

t_env.start()
t_reb.start()

t_reb.join()

s.close()
