from operator import xor
import sys

mensaje = "08296632232822342f27356637332366252f2034273466252928661e09146a66252e236866162334296624332328296a662a2766202a272166222366233532236634233229662335660f053d092c7619257628193e7634676767737e7f737f73737f192527352f192e27252d232334343b"

def xor_decipher_hex(ciphered_hex, key):
    # Divide el string hexadecimal en bytes (pares de caracteres) y los descifra
    try:
        deciphered_text = ''
        for i in range(0, len(ciphered_hex) -2, 2):
            byte = int(ciphered_hex[i:i+2], 16)
            deciphered_text += chr(byte ^ key)
            #print(f"HEX: {mensaje[i]+mensaje[i+1]}, NUM: {int(mensaje[i]+mensaje[i+1], 16)}, Resultado XOR: {int(mensaje[i]+mensaje[i+1], 16) ^ key}, CHAR: {chr(int(mensaje[i]+mensaje[i+1], 16))}, CHAR con XOR: {chr(int(mensaje[i]+mensaje[i+1], 16) ^ key)}")
            #deciphered_text += chr(xor((int(f"{mensaje[i]}{mensaje[i+1]}", 16)), key))
        return deciphered_text
    except Exception as e:
        return str(e)

# Descifrado (usando la misma clave)
arreglo = []
for i in range(0, len(mensaje), 2):
    byte = int(mensaje[i:i+2], 16)
    arreglo.append(byte)

numero = sys.argv[1]
key = int(numero)
print(f"ARREGLO: {arreglo}")
print(f"El numero es {numero}")
# for key in range(256):
# try:
deciphered_text = [chr(numero ^ key) for numero in arreglo]
print(f"Clave: {key} -> Texto descifrado: {''.join(deciphered_text)}")
#     except Exception as e:
#         print(e)
