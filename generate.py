from secrets import randbelow
from math import factorial
from math import log2 as ln

wordlist = []
with open('google-10000-english-usa-no-swears-medium.txt') as f:
    for word in f:
        wordlist.append(word.split()[0])


length = len(wordlist)
pplength = 2
quantity = 5

print("number of words: {}".format(length))

for j in range(quantity):
    pp = ""
    for i in range(pplength):
        sep = "!@#$%^&*"[randbelow(8)]
        pp += sep + wordlist[randbelow(length)]

    for i in range(2):
        pp += str(randbelow(10))
    print(pp)

perms = length ** pplength + (8 ** 2) + (9 ** 2)
entropy = ln(perms)

perms2 = 26 ** 3 + 9 ** 5
entropy2 = ln(perms2)
print("passphrase possible permutations are {}".format(perms))
print("entropy of passphrase is {}".format(entropy))
print("password possible permutations are {}".format(perms2))
print("entropy of password is {}".format(entropy2))


