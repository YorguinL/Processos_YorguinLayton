
def enviar_missatge(s):
    while True:
        missatge = raw_input('Introdueix missatge: ')
        s.sendall(missatge)
        if missatge == 'Bye':
            break

def rebre_missatge(s):
    while True:
        dades = s.recv(1024)
        print (dades)
        if dades == 'Bye':
            s.sendall(dades)
            break
