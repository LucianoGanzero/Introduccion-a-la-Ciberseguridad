from pwn import *
import re
from libnum import *
from sympy.ntheory import factorint

# Nos conectamos utilizando remote
con = remote("ic.catedras.linti.unlp.edu.ar", 11017)

# para quitar el texto que no nos interesa (banner), 
# leemos hasta justo antes de la cuenta, es decir, hasta ":\n"
con.readuntil(" siguiente texto:\n")

digitos = r'\d+'
n = con.readline().decode()
e = con.readline().decode()
c = con.readline().decode()
n = int(re.findall(digitos, n)[0])
e = int(re.findall(digitos, e)[0])
c = int(re.findall(digitos, c)[0])

print(n)
print(e)
print(c)

prime_factors = factorint(n)
print(prime_factors)
primos = [key for key in prime_factors]
print(primos)

phi_n = (primos[0] - 1)*(primos[1] - 1)
d = invmod(e, phi_n)

mensaje = pow(c, d, n)
mensaje_decodificado = n2s(mensaje).decode()
print(mensaje_decodificado)

con.send((mensaje_decodificado+"\n").encode())

# Imprimimos toda la respuesta del servidor
print(con.readall())