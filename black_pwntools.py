# type: ignore
from pwn import *
print(cyclic(50))
print(cyclic_find("laaa"))

print(shellcraft.sh())
print(hexdump(asm(shellcraft.sh())))
# use for remote networking communication
r = remote("127.0.0.1", 1234)
r.sendline("hello!")
r.interactive()
r.close()

# for more information doing research on https://docs.pwntools.com/en/stable/ in this website