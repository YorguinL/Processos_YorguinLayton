# -*- coding: utf:8 -*-
"""Aquest programa consisteix en omplir una matriu amb els nombres primers ordenats de petit
a gran. La longitud d'aquesta matriu serà del mateix valor que el paràmetre que introdueix
l'usuari a l'hora de cridar el programa.

Ex: python nomPrograma.py 5
Per tant, el que ens retornarà és la següent matriu: [2, 3, 5, 7, 11]"""

import sys

class llista_primers:
    def __init__(self, n):
        """ Atributs """
        self.n = n
        self.llista = []
        self.busca()

    def busca(self):
        """ Comprova la longitud de la matriu i afegeix els números primers"""
        if (len(self.llista) == 0):
            #Si la longitud de la matriu és 0 o 1, afegeix el primer nombre primer, és a dir, 2.
            self.llista.append(2)
            self.busca()
        elif (len(self.llista) < self.n):
            #Mentres la longitud de la matriu sigui més petita al paràmetre introduït per l'usuari
            trobat = False
            seguent = self.llista[-1]+1
            while not trobat:           #Initcialitzem bucle per omplir la matriu.
                for i in self.llista:   #Busquem tants números primers com vulgui l'usuari.
                    if seguent%i == 0:  #Descartem els números compostos.
                        seguent += 1
                        trobat = False
                        break
                    else:
                        trobat = True
            self.llista.append(seguent)
            self.busca()


if __name__ == '__main__':
    #Executa el codi quan no és cridat des d'un altre programa
    l = llista_primers(int(sys.argv[1]))
    print l.llista
