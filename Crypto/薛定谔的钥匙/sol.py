from pwn import *
from tqdm import tqdm

def talk(io, payload):
    io.recvuntil("Ask for the god:\n")
    io.sendline(payload)
    return 1 if b'True' in io.recvline() else 0

def makexor(a, b):
    return f'( ( not ( {a} ) ) and ( {b} ) ) or ( ( {a} ) and ( not ( {b} ) ) )'

def gen_payloads():
    payloads = []
    count = 0
    for i in range(1, 16):
        if bin(i).count('1') == 1:
            payloads.append('')
        else:
            payloads.append(f'C{count}')
            count += 1

    for i in range(len(payloads)):
        if payloads[i] == '':
            tmp, res = i+1, '0'
            for j in range(1, len(payloads)+1):
                if tmp & j != 0 and tmp != j:
                    res = makexor(res, payloads[j-1])
            payloads[i] = res
    return payloads

io = remote('121.4.118.92', 9367)
# context.log_level = 'debug'

payloads = gen_payloads()
for _ in tqdm(range(100)):
    code = [talk(io, i) for i in payloads]
    tmp = 1
    lie = ''
    while tmp <= len(code):
        res = 0
        for i in range(len(code)):
            if (i+1) & tmp != 0:
                res = res ^ code[i]
        lie += str(res)
        tmp <<= 1
    lie = int(lie[::-1], 2)-1
    code[lie] = 1 ^ code[lie]
    ans = ''
    for i in range(len(code)):
        if bin(i+1).count('1') != 1:
            ans += str(code[i]) + ' '
    io.recvuntil("Now open the chests:\n")
    io.sendline(ans)

io.recvuntil("You've found all the keys!\n ")
flag = io.recvline(False)
print(flag)
io.close()