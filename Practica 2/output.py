# decompyle3 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.3 (main, Sep 28 2024, 12:30:34) [GCC 13.2.0]
# Embedded file name: ./hard.py
# Compiled at: 2024-10-11 11:29:53
# Size of source mod 2**32: 565 bytes
import time, binascii
from Crypto.Cipher import AES
y = "s4Pd"

def get_passwd():
    return input("Password: ")


def check(s):
    z = "0w5" + y + "r"
    x = (s[6:8] + s[0:3] + s[3:6])[::-1]
    return x == z


def get_secret(k):
    secret = binascii.unhexlify("e83fe32861ccec8a065f3ce5f6361d9f609e286adf8eb3e50a39fc3b72fc6b68")
    aes = AES.new(k.encode("utf8") * 2, AES.MODE_CBC, "thisIsNotTheFlag".encode("utf8"))
    return aes.decrypt(secret)


s = get_passwd()
if check(s):
    print(get_secret(s).decode("utf8"))
else:
    time.sleep(3)
    print("Invalid password!")

# okay decompiling Descargas/hard24.pyc
