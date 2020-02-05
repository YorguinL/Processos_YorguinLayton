
def registre(s):
    while True:
        usuari_nou = raw_input('Nom d\'usuari: ')
        mss_benvinguda = usuari_nou + ' se ha unido.'
        s.sendall(mss_benvinguda)


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
