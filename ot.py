#!/bin/env python3

from Crypto.Cipher import AES
import hashlib
import random
import sys

g = 9
n = 1001

a = random.randint(5, 10)
b = random.randint(10, 15)

alice = pow(g, a)
c = 1
if (len(sys.argv) > 1):
    c = int(sys.argv[1])

bob = pow(g, b)
if (c != 0):
    bob = alice * bob

# Alice
key0 = hashlib.sha256(str(pow(bob, a)).encode('utf-8')).digest()
key1 = hashlib.sha256(str(pow(int(bob / alice), a)).encode('utf-8')).digest()

# Bob
kr = hashlib.sha256(str(pow(alice, b)).encode('utf-8')).digest()

# Alice
cipher0 = AES.new(key0, AES.MODE_ECB)
cipher1 = AES.new(key1, AES.MODE_ECB)

# Bob
cipher_r = AES.new(kr, AES.MODE_ECB)

# Alice
# 16 char strings
en0 = cipher0.encrypt('Bob did it      ')
en1 = cipher1.encrypt('Alice did it    ')

# Bob
mr1 = cipher_r.decrypt(en0)
mr2 = cipher_r.decrypt(en1)

print(' ---- Keys ---- ')
print(key0)
print(key1)
print(kr)
print(' ---- Encrypted messages ---- ')
print(en0)
print(en1)
print(' ----  Decripted messages ---- ')
print(mr1)
print(mr2)
