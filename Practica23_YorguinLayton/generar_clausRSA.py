# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 1-Generar clau RSA
def generateKey():
    key = RSA.generate(2048)
    return key

# 2-Exportar claus RSA en un fitxer .pem
def expKey(filename, key):
    exp_key = key.exportKey('PEM')

    file = open(filename + ".pem", "wb")
    file.write(exp_key)
    file.close();


if __name__ == '__main__':

    # 1-Generem clau
    k = generateKey()

    # 2-Exportem claus
    expKey("Yorguin_private", k)
    expKey("Yorguin_public", k.publickey())
