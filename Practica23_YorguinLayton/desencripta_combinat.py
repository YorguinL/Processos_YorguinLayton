# -*- coding: utf-8 -*-
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import base64

# 1-Obtenir clau privada, clau encriptada i missatge encriptat
def readFiles(keyF, enc_key, msg_enc):
    prv_key = RSA.importKey(open(keyF).read()) # Importem la clau privada
    enc_k = open(enc_key).read()
    msg_e = open(msg_enc).read()

    return prv_key, enc_k, msg_e

# 2-Desxifrar la clau per RSA
def decipherKey(enc_k, prv_key):
    cipher = PKCS1_OAEP.new(prv_key)
    dec_key = cipher.decrypt(enc_k)

    return dec_key

# 3-Desxifrar missatge per AES
def decipherMsg(msg, key):

    d_msg = base64.b64decode(msg)

    # Desglocem el missatge per blocs
    iv = d_msg[:AES.block_size]
    enc_msg = d_msg[AES.block_size:]

    cipher_aes = AES.new(key, AES.MODE_CBC, iv)
    dec_msg = cipher_aes.decrypt(enc_msg)

    # Guardem el missatge desxifrat en el fitxer missatge
    file = open("missatge.txt", "wb")
    file.write(dec_msg)
    file.close()

    return dec_msg

# Comprovem número de paràmetres
if(len(sys.argv) > 3):

    if __name__ == '__main__':

        # 1-Guardem clau privada, clau encriptada i missatge encriptat
        private_key, enc_key, msg_enc = readFiles(sys.argv[1], sys.argv[2], sys.argv[3])

        # 2-Guardem la clau SHA256 desxifrada
        dec_key = decipherKey(enc_key, private_key)

        # 3-Desxifrem missatge i el guardem
        dec_msg = decipherMsg(msg_enc, dec_key)
        # print(dec_msg)

else:
    print "És necessari executar amb tres paràmetres"
    print "python programa.py param1 param2 param3"
