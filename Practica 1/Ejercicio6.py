from pwn import *
import hashlib

# Nos conectamos utilizando remote
con = remote("ic.catedras.linti.unlp.edu.ar", 11006)

# para quitar el texto que no nos interesa (banner), 
# leemos hasta justo antes de la cuenta, es decir, hasta ":\n"
con.readuntil("siguiente palabra:\n")

# Leemos hasta el salto de línea, la cuenta deseada
palabra = con.readline()
palabra = palabra.decode()
palabra = palabra.strip()
print(palabra)
md5_hash = hashlib.md5()
md5_hash.update(palabra.encode())
palabra_hasheada = md5_hash.hexdigest()
print(palabra_hasheada)

con.send((palabra_hasheada+"\n").encode())

# Imprimimos toda la respuesta del servidor
print(con.readall())