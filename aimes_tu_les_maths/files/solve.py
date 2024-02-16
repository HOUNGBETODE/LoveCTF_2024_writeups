from Crypto.Util.number import *
from sympy import *
from sys import *

u = 103223593878323616966427038558164830926502672938304332798494105455624811850665520007232855349275322661436610278579342219045141961390918581096853786570821153558254045159535424052709695034827346813080563034864500825268678590931984539859870234179994586959855078548304376995608256368401270715737193311910694875689

output = open("love.txt", "rb").read().decode()

x = int(output.replace("❤️", "1").replace("😘", "0")[::-1], 2)

b = ntheory.nthroot_mod(x, 2, u, True)
for i in b :
    for j in ntheory.nthroot_mod(i, 2, u, True) :
        for k in ntheory.nthroot_mod(j, 2, u, True) :
            for l in ntheory.nthroot_mod(k, 2, u, True) :
                for m in ntheory.nthroot_mod(l, 2, u, True) :
                    for n in ntheory.nthroot_mod(m, 2, u, True) :
                        try :
                            message = long_to_bytes(n).decode()
                        except :
                            pass
                        else :
                            print(message)
                            exit()