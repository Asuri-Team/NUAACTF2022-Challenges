import string
from Crypto.Util.number import *

def dec(m, a, b):
    if m not in string.ascii_lowercase + string.ascii_uppercase:
        return m
    table = string.ascii_lowercase if m in string.ascii_lowercase else string.ascii_uppercase
    return table[((table.index(m) - b) * inverse(a, 26)) % 26]

cipher = 'SNFFLKU{D_4p_ka3_aRe0_0u_Ka3_LezykV_tvEmo}'
flag = 'NUAACTF'

def check(a, b):
    table = string.ascii_uppercase
    for i in range(7):
        if (table.index(flag[i]) * a + b) % 26 != table.index(cipher[i]):
            return False
    return True

for a in range(26):
    for b in range(26):
        if check(a, b):
            print(a, b)
            break

flag = ''
for i in cipher:
    flag += dec(i, 3, 5)
print(flag)