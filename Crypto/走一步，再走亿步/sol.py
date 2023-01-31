from hashlib import md5
from sage.all import *

A = [114514**2, 1, 0]
M = [
    [114514, 233, 0],
    [0, 1919810, 1],
    [0, 1, 0]
]
A = matrix(A)
M = matrix(M)
ans = A*(M**1919809)
ans = ans[0][2]

flag = md5(str(ans).encode()).hexdigest()
flag = 'NUAACTF{' + flag + '}'
print(flag)