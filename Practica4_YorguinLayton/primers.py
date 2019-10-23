# -*- coding: utf:8 -*-
"""Aquest programa consisteix en omplir una matriu amb els nombres primers ordenats de petit
a gran. La longitud d'aquesta matriu serà del mateix valor que el paràmetre que introdueix
l'usuari a l'hora de cridar el programa.

Ex: python nomPrograma.py 5
Per tant, el que ens retornarà és la següent matriu: [2, 3, 5, 7, 11] """

import sys

class llista_primers:
    def __init__(self, n):
        self.n = n
        self.llista = []
        self.busca()

    def busca(self):
        if (len(self.llista) == 0):
            self.llista.append(2)
            self.busca()
        elif (len(self.llista) < self.n):
            trobat = False
            seguent = self.llista[-1]+1
            while not trobat:
                for i in self.llista:
                    if seguent%i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else:
                        trobat = True
            self.llista.append(seguent)
            self.busca()


if __name__ == '__main__':
    l = llista_primers(int(sys.argv[1]))
    print l.llista
