from pwn import *
import hashlib

def sha256_encoder(palabra):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(palabra.encode())
    return sha256_hash.hexdigest()

# Nos conectamos utilizando remote
con = remote("ic.catedras.linti.unlp.edu.ar", 11007)

# para quitar el texto que no nos interesa (banner), 
# leemos hasta justo antes de la cuenta, es decir, hasta ":\n"
con.readuntil("diccionario rockyou.txt):\n")


# Leemos hasta el salto de línea, la palabra deseada
palabra = con.readline()
# La configuramos correctamente y la imprimo para tenerla a mano
palabra = palabra.decode().strip()
print(palabra)
try:
    with open('rockyou.txt', 'r') as file:
        print("ENTRO AL ARCHIVO")
        for word in file:
            #Limpio la palabra recibida de posibles caracteres extras
            possible_password = word.strip()
            print(line)
            #Hasheo la palabra
            palabra_hasheada = sha256_encoder(possible_password)
            print(palabra_hasheada)
            if palabra == palabra_hasheada:
                con.send((possible_password+"\n").encode())
                break

    # Imprimimos toda la respuesta del servidor
    print(con.readall())
except Exception as e:
    print(e)