# -*- coding: utf-8 -*-
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto import Random
import base64

# 1-Obtenir clau i missatge
def readFiles(keyFile, msgFile):
    keyF = RSA.importKey(open(keyFile).read()) # Importem la clau pública
    msgF = open(msgFile).read()
    return keyF, msgF

# 2-Generar clau a partir de SHA256
def generateKeySHA256():
    pwd = raw_input("Contrasenya: ")
    hash = SHA256.new()
    hash.update(pwd)
    return hash.digest()

# 3-Encriptar missatge per AES
def encryptAES(msg, key):
    # Generem vector d'inicialització
    iv = Random.new().read(AES.block_size)

    # Afegim padding al missatge
    p_msg = msg + " " * (16 - len(msg) % 16)

    cipher_aes = AES.new(key, AES.MODE_CBC, iv)
    enc_msg = cipher_aes.encrypt(p_msg)

    # Guardem missatge encriptat en el fitxer missatge_enc
    file = open("missatge_enc.txt", "wb")
    file.write(base64.b64encode(iv + enc_msg))
    file.close()

# 4- Encriptar clau SHA256 per RSA
def encryptKey(hash, key):
    cipher = PKCS1_OAEP.new(key)
    enc_key = cipher.encrypt(hash)

    # Guardem clau encriptada en el fitxer enc_k_aes
    file = open("enc_k_aes.txt", "wb")
    file.write(enc_key)
    file.close()

    return enc_key

# Comprovem número paràmetres
if(len(sys.argv) > 2):

    if __name__ == '__main__':

        # 1-Guardem clau i missatge
        key_public, msg = readFiles(sys.argv[1], sys.argv[2])

        # 2-Generem clau SHA256
        hash = generateKeySHA256()
        # print("Hash generat: " + str(hash))

        # 2-Encriptem missatge amb la clau SHA256 generada i el guardem en un fitxer
        encryptAES(msg, hash)

        # 3-Encriptem clau per RSA i la guardem en un fitxer
        enc_key_AES = encryptKey(hash, key_public)
        # print("Clau encriptada: " + enc_key_AES)

else:
    print "És necessari executar amb dos paràmetres"
    print "python programa.py param1 param2"
