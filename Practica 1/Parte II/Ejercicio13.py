from pwn import *
import re
from libnum import *
# Nos conectamos utilizando remote
con = remote("ic.catedras.linti.unlp.edu.ar", 11012)

# para quitar el texto que no nos interesa (banner), 
# leemos hasta justo antes de la cuenta, es decir, hasta ":\n"
con.readuntil(" siguiente texto:\n")

digitos = r'\d+'

p = int(re.findall(digitos, con.readline().decode())[0])
q = int(re.findall(digitos, con.readline().decode())[0])
e = int(re.findall(digitos, con.readline().decode())[0])
c = int(re.findall(digitos, con.readline().decode())[0])

print(p)
print(q)
print(e)
print(c)

n = p*q
phi_n = (p-1)*(q-1)

d = invmod(e, phi_n)

mensaje = pow(c, d, n)
mensaje_decodificado = n2s(mensaje).decode()
print(mensaje_decodificado)

con.send((mensaje_decodificado+"\n").encode())

# Imprimimos toda la respuesta del servidor
print(con.readall())