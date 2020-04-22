# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Hash import SHA256
from Crypto import Random
import base64

# 1-Generar clau RSA de 2048 bytes
def generateKey():
    key = RSA.generate(2048)
    return key


# 2-Exportar claus RSA en un fitxer .pem
def expKey(filename, key):
    exp_key = key.exportKey('PEM')

    file = open(filename + ".pem", "wb")
    file.write(exp_key)
    file.close();


# 3-Importar clau RSA a partir d'un fitxer .pem
def impKey(filename):
    key = RSA.importKey(open(filename).read())
    return key


# 4-Encriptar missatge per RSA
def encryptMessage(msg, key):
    cipher_rsa = PKCS1_OAEP.new(key)
    enc_msg = cipher_rsa.encrypt(msg)
    return enc_msg


#  5-Desxifrar missatge per RSA
def decipherMessage(encryptedMsg, key):
    cipher_rsa = PKCS1_OAEP.new(key)
    dec_msg = cipher_rsa.decrypt(encryptedMsg)
    return dec_msg


# 6-Generar clau a partir de SHA256
def generateKeySHA256():
    pwd = raw_input("Contrasenya: ")
    hash = SHA256.new()
    hash.update(pwd)
    return hash.digest()


# 7-Encriptar missatge per AES en mode CBC
def encryptAES(msg, key):

    # Generem vector d'inicialització
    iv = Random.new().read(AES.block_size)

    # Afegim padding al missatge
    p_msg = msg + " " * (16 - len(msg) % 16)

    cipher_aes = AES.new(key, AES.MODE_CBC, iv)
    enc_msg = cipher_aes.encrypt(p_msg)

    return base64.b64encode(iv + enc_msg)


# 8-Desxifrar missatge per AES en mode CBC
def decipherAES(msg, key):

    d_msg = base64.b64decode(msg)

    # Desglocem el missatge per blocs
    iv = d_msg[:AES.block_size]
    enc_msg = d_msg[AES.block_size:]

    cipher_aes = AES.new(key, AES.MODE_CBC, iv)
    dec_msg = cipher_aes.decrypt(enc_msg)

    return dec_msg




if __name__ == '__main__':

    # 1-Generem clau
    k = generateKey()


    # 2-Exportem claus
    expKey("private_key", k)
    expKey("public_key", k.publickey())


    # 3-Importem claus
    prv_key = impKey("private_key.pem")
    print("Private key: " + str(prv_key))


    pbc_key = impKey("public_key.pem")
    print("Public key: " + str(pbc_key))


    # 4-Encriptar missatge utilitzan la clau pùblica
    enc_data = encryptMessage("Pràctica mòdul processos", pbc_key)
    print("Missatge encriptat: " + str(enc_data))


    # 5- Desxifrar missatge utilitzan la clau privada
    dec_data = decipherMessage(enc_data, prv_key)
    print("Missatge desxifrat: " + dec_data)


    # 6-Generem clau SHA256
    hash = generateKeySHA256()
    print("Hash generat: " + str(hash))


    # 7-Encriptem missatge
    msg = "Pràctica mòdul processos"
    enc_dataAES = encryptAES(msg, hash)
    print("Missatge encriptat: " + str(enc_dataAES))


    # 8-Desxifrem missatge
    dec_dataAES = decipherAES(enc_dataAES, hash)
    print("Missatge desxifrat: " + dec_dataAES)
