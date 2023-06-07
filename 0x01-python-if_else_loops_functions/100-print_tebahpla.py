#!/usr/bin/python3
alph = 0
for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char - alph)), end="")
    alph = 32 if alph == 0 else 0
