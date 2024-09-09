from pwn import *

# Nos conectamos utilizando remote
con = remote("ic.catedras.linti.unlp.edu.ar", 11015)

# para quitar el texto que no nos interesa (banner), 
# leemos hasta justo antes de la cuenta, es decir, hasta ":\n"
con.readuntil("la primer palabra es:\n")

# Leemos hasta el salto de línea, la cuenta deseada
primera_palabra = con.readline().decode()

mensaje = con.readline().decode()

primera_palabra_hex = [ord(x) for x in primera_palabra]
mensaje_hex = [int(mensaje[i:i+2],16) for i in range(0, len(mensaje) -2, 2)]
clave = [mensaje_hex[i]^primera_palabra_hex[i] for i in range(len(primera_palabra_hex))]
clave = clave[:4]
print(primera_palabra)
print(primera_palabra_hex)
print(mensaje)
print(mensaje_hex)
print(clave)

decoficado = [chr(mensaje_hex[i] ^ clave[i % len(clave)]) for i in range(len(mensaje_hex))]

print("".join(decoficado))

con.send(("".join(decoficado)+"\n").encode())

# Imprimimos toda la respuesta del servidor
print(con.readall())

