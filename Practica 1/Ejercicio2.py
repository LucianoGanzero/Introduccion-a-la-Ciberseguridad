from pwn import *
import base64

# Nos conectamos utilizando remote
con = remote("ic.catedras.linti.unlp.edu.ar", 11002)

# para quitar el texto que no nos interesa (banner), 
# leemos hasta justo antes de la cuenta, es decir, hasta ":\n"
con.readuntil("base64 esta palabra:\n")

# Leemos hasta el salto de línea, la cuenta deseada
cuenta = con.readline()

#Transformo los bytes que me llegan a string, le saco el salto de linea y lo vuelvo a transformar a bytes asi puedo mandarlo al encoder
palabra_bytes = cuenta.decode()
palabra_bytes = palabra_bytes.strip()
palabra_recortada = palabra_bytes.encode('ascii')

# Pasamos los bytes a string, para poder realizar la cuenta
palabra_encodeada = base64.b64encode(palabra_recortada)


print(f"La palabra era {palabra_bytes}")
palabra_enviar = palabra_encodeada.decode('ascii')
print(f"La palabra encodeada es {palabra_enviar}")

# Enviamos la respuesta de la cuenta, como bytes:
con.send(palabra_enviar.encode()) 

# Imprimimos toda la respuesta del servidor
print(con.readall())
