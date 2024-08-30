from pwn import *
import base64
import re
# Nos conectamos utilizando remote
con = remote("ic.catedras.linti.unlp.edu.ar", 11004)

# para quitar el texto que no nos interesa (banner), 
# leemos hasta justo antes de la cuenta, es decir, hasta ":\n"
con.readuntil("Bienvenidos!")
numero = con.readline()
numero = numero.decode()

numero = re.findall(r'\d+', numero)
numero = int(''.join(numero))
# Leemos hasta el salto de línea, la cuenta deseada
frase = con.readline()
frase = frase.decode().strip()

#frase_a_devolver = ''
#for char in frase:
#    if char != ' ':        
#        suma = ord(char) + numero
#        if suma > 122:
#            resto = suma % 122
#            suma = 96 + resto

#        sumo = chr(suma)
#    else:
#        sumo = " "
#    frase_a_devolver += sumo

frase_a_devolver = ''.join(
    chr(((ord(char) + numero - 97) % 26) + 97) if char != ' ' else ' ' 
    for char in frase
)

print(f"El ROT fue {numero}")
print(f"LA frase es {frase}")
print(f"La frase con rot aplicado es {frase_a_devolver}")
print((str(frase_a_devolver) + "\n").encode())

con.send((str(frase_a_devolver) + "\n").encode())

# Imprimimos toda la respuesta del servidor
print(con.readall())