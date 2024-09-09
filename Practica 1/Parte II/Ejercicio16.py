from pwn import *
import re
from libnum import *
import gmpy2

# Nos conectamos utilizando remote
con = remote("ic.catedras.linti.unlp.edu.ar", 11018)

# para quitar el texto que no nos interesa (banner), 
# leemos hasta justo antes de la cuenta, es decir, hasta ":\n"
con.readuntil("Diffie Hellman:\n")

digitos = r'\d+'
p = con.readline().decode()
g = con.readline().decode()
public_alice = con.readline().decode()
private_bob = con.readline().decode()
p = int(re.findall(digitos, p)[0])
g = int(re.findall(digitos, g)[0])
public_alice = int(re.findall(digitos, public_alice)[0])
private_bob = int(re.findall(digitos, private_bob)[0])

print(f"p = {p}")
print(f"g = {g}")
print(f"public alice = {public_alice}")
print(f"private bob = {private_bob}")

key = gmpy2.powmod(public_alice, private_bob, p)
print(f"key = {key}") 

con.send((str(key) +"\n").encode())
# Imprimimos toda la respuesta del servidor
print(con.readall())