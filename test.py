from time import sleep
# # #
from secrets import randbelow
from math import factorial
from math import log2 as ln
# # #

alpha = "abcdefghijklmnopqrstuvwxyz"

decel1 = 0
decel2 = 0
decel3 = 0

stop1 = max(randbelow(26), 1)
stop2 = max(randbelow(26), 1)
stop3 = max(randbelow(26), 1)
a1, b1, c1, a2, b2, c2, a3, b3, c3 = 0, 0, 0, 0, 0, 0, 0, 0, 0

print()
for j in range(2):
    for i, char in enumerate(alpha):
        if j == 1:
            # decel += .02
            decel1 = min(i/stop1, .2)
            decel2 = min(i/stop2, .2)
            decel2 = min(i/stop3, .2)
            
        if i <= stop1 and j < 1:
            a1 = alpha[(i-1) % len(alpha)]
            b1 = alpha[i]
            c1 = alpha[(i+1) % len(alpha)]
            
        if i <= stop2 and j < 1:
            a2 = alpha[(i-1) % len(alpha)]
            b2 = alpha[i]
            c2 = alpha[(i+1) % len(alpha)]
        
        if i <= stop3 and j < 1:
            a3 = alpha[(i-1) % len(alpha)]
            b3 = alpha[i]
            c3 = alpha[(i+1) % len(alpha)]

        r1 = "{}[{}]{}".format(a1, b1, c1)
        r2 = "{}[{}]{}".format(a2, b2, c2)
        r3 = "{}[{}]{}".format(a3, b3, c3)
        print("\r{} {} {}".format(r1, r2, r3), flush=True, end='')
        sleep(.08 + decel1)
print()
    


# for i in range(10):
#     sleep(.2)
#     print(i, end="\r", flush=True)