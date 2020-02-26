# coding=utf-8
import socket
from threading import Thread
import time
import os, sys

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

usuari = []
llista_usuaris = []


def enviar_missatge(missatge, usuari):
    m = missatge
    for i in llista_usuaris:    #Recorrer la llista d'usuaris
        if i != usuari:         #Enviar missatge a tots els usuris connectats menys a ell
            i[0].sendall(str(usuari[1])+m)    

def rebre_missatge(usuari):

    while True:
        dades = usuari[0].recv(1024)
        print (dades)
        if dades == 'Bye\n':
            enviar_missatge(dades, usuari) #Enviar ultim missatge
            usuari[0].close()   #Desconnectem usuari
            llista_usuaris.remove(usuari)   #Eliminem l'usuari de la llista d'usuaris connesctats
            print(str(usuari[1]) + " ha surtit")
            break

        t_env = Thread(target=enviar_missatge, args=(dades, usuari)) #
        t_env.start()

def connectar(s):

    while True:
        try:
            conn, addr = s.accept()     #Acceptar la conexió
            nomUsuari = conn.recv(1024)     #Assignar nom usuari

            if nomUsuari.find("\n") != -1:
                nomUsuari = nomUsuari[:(len(nomUsuari)-1)]+":"
                print(nomUsuari)

            usuari = (conn, nomUsuari)   #Assignar conexió client amb el seu nom
            llista_usuaris.append(usuari)   #Afegim client a llista_clients
            

            t_reb = Thread(target=rebre_missatge, args=(usuari,))
            t_reb.start()
        except:
            print("Ha fallat la connexió.")

t_con = Thread(target=connectar, args=(s,))

t_con.start()
t_con.join()
time.sleep(1)
s.close()
