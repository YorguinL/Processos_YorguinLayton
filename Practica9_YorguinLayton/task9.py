#-*- coding: utf8 -*-
#4523

# 40 / 2 = 20
# 40 / 4 = 10

from multiprocessing import Pool
from datetime import datetime

def primers(num):
    for i in range(2, num/2):
        if num % i == 0:
            return False
        else:
            pass
    return True

if __name__ == '__main__':

    l = range(40000000, 40000100)#[45445535, 56534563, 43566487, 43635453, 52346557, 53454433, 43546453, 26847357, 54577647]
    start = datetime.now()

    pool = Pool(processes=8) #Creem el Pool després d'importar-lo. Com més processos menys temps triga.
    result = pool.map(primers, l) #La funció map() no envia el resultat fins que està del tot finalitzat. 
   #result = pool.imap(primers, l) #La funció imap() envia el resultat mentres ho calcula.  
    
    for i in range(len(l)):
       print l[i], result  #Si utilitzem imap() hem d'afegir .next() a result.

    print datetime.now() - start
