import struct
import hashlib
import codecs

g_table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
DE = 0x1145141
N = 32


def encrypt(block, key, endian="!"):
    (pack, unpack) = (struct.pack, struct.unpack)
    
    (y, z) = unpack(endian+"2L", block)
    k = unpack(endian+"4L", key)
    
    global DE, N
    (sum, de, n) = 0, DE, N
    
    for i in range(n):
        y = (y + (((z<<4 ^ z>>5) + z) ^ (sum + k[sum&3]))) & 0xFFFFFFFF
        sum = (sum + de) & 0xFFFFFFFF
        z = (z + (((y<<4 ^ y>>5) + y) ^ (sum + k[sum>>11 &3]))) & 0xFFFFFFFF
    return pack(endian+"2L", y, z)

def enc_a(data, key, endian="!"):
    n_d = b''
    d_s = len(data)
    d_p = d_s % 8
    if d_p:
        d_pl = 8 - d_p
        data += (d_pl*chr(0))
        d_s += d_pl
    for i in range(d_s//8):
        b = data[i*8:(i*8)+8]
        n_d += encrypt(b, key, endian)
    return n_d

def entry(d):
    key = b'{r{r\x7fx\x7fxjqjq(+*-'
    data = input("Here is your flag:\n")
    data = data.zfill(len(d))

    magic_num = 0x19
    m = bytearray(key)
    k = ''.join([chr(c^magic_num) for c in m])
    f_k = k.encode()
    
    if enc_a(data.encode(), f_k) == d:
        print("Correct!")
    else:
        print("Wrong!")