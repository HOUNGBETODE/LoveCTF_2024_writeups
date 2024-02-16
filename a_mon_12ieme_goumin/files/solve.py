from string import *
from pwn import *

# xoring the ciphertext with 12
ciphertext = b"=<5:8=<;9=59=<598598584===9?9=59=<5=>=599:==89=9>99=<8=<="
xor_result = xor(ciphertext, 12).decode()

# creating a dictionary based on the charset
charset = digits + ascii_letters + "_@"
dico = dict()
for i in charset :
    dico[ord(i)] = i

# recovering the plaintext from the number found after xor
recover = ""
size = 0
while size < len(xor_result) :
    j = 1
    while j>=1 :
        c = int(xor_result[size:size+j])
        if c in dico :
            recover += dico[c]
            size += j
            break
        j += 1
print(recover)