from pwn import *

# Nos conectamos utilizando remote
con = remote("ic.catedras.linti.unlp.edu.ar", 10002)

# para quitar el texto que no nos interesa (banner), 
# leemos hasta justo antes de la cuenta, es decir, hasta ":\n"
while True:
    
    con.readuntil("!:\n")
    

    # Leemos hasta el salto de línea, la cuenta deseada
    try:
        cuenta = con.readline()
    except EOFError:
        print(con.readall())
        break

    print(type(cuenta))
    print(cuenta)

    # Pasamos los bytes a string, para poder realizar la cuenta
    cuenta = cuenta.decode()

    # Para evitar usar eval podríamos parsear la información.
    # Split convierte una cadena de texto en una lista, utilizando como separador los
    # espacios en blanco
    cuenta = cuenta.split()

    # Convierto a entero los operandos
    op1 = int(cuenta[0]) 
    op2 = int(cuenta[2])
    operador = cuenta[1]

    # Sumo multiplico o resto según el operador
    if operador == '+':
        resultado = op1 + op2
    elif operador == '*':
        resultado = op1 * op2
    else:
        resultado = op1 - op2

    # Enviamos la respuesta de la cuenta, como bytes:
    con.send((str(resultado) + "\n").encode())

