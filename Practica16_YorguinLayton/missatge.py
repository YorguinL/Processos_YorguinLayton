
import socket

s = socket

def enviar_missatge(s):
    while True:
        missatge = raw_input('Introdueix missatge: ')
        s.sendall(missatge)
        if missatge == "bye":
            break

def rebre_missatge(s):
    while True:
        missatge = s.recv(1024)
        print (missatge)
        if missatge == "bye":
            break
