import sys
import base64
import re

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

arg = sys.argv[1]
print(f"El mensaje codificado es {arg}")


try:
    res = ''.join(chr(int(i)) for i in arg.split(" "))
    
    print (f"Es un ascii y significa {str(res)}")
except Exception as e:
    print(f"No es un ascii porque {e}")


try:
    res = base64.b64decode(arg)
    print(f"Esta en base 64 y significa {str(res)}")

except Exception as e:
    print(f"No es un base64 porque {e}")


try:
    res = base64.b32decode(arg)

    print(f"Esta en base 32 y significa {str(res)}")

except Exception as e:
    print(f"No es un base32 porque {e}")

try:
    res = ''.join(chr(int(i) + 96) for i in re.split('-| ', arg) if i)
    
    print (f"Es un A1Z26 y significa {str(res)}")
except Exception as e:
    print(f"No es un A1Z26 porque {e}")

try:
    arreglo = arg.split("_")
    devolver = []
    
    for palabra in arreglo:
        palabra_a = ""
        for i in range(0,len(palabra),2):
            valor = int(palabra[i:i+2])
            suma = valor + 65
            palabra_a += chr(int(suma)) 
        devolver.append(palabra_a + " ")
    print("".join(devolver))
except Exception as e:
    print(f"No es un valor decimal porque {e}")

try:
    byte_string = bytes.fromhex("".join(arg.split(" ")))  
    ascii_string = byte_string.decode("ASCII")  
    print(f"Es un hexa es ascii y significa {ascii_string}")  
except Exception as e:
    print(f"No es un hexa en ASCII porque {e}")


try:
    arg += ' '
    decipher = ''
    citext = ''
    for letter in arg:
 
        # checks for space
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            citext += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
 
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                decipher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''

    print(f"Es codigo Morse y significa {decipher}")

except Exception as e:
    print(f"No es Morse porque {e}")