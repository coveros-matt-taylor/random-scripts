from secrets import randbelow
from math import factorial
from math import log2 as ln

wordlist = []
with open('google-10000-english-usa-no-swears-medium.txt') as f:
    for word in f:
        wordlist.append(word.split()[0])


length = len(wordlist)
pplength = 5
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

sep_quantity = (pplength-1)
# sep_quantity = 2

perms = length ** pplength + (8 ** sep_quantity) + (9 ** sep_quantity)
entropy = ln(perms)

perms2 = 26 ** 3 + 9 ** 5
entropy2 = ln(perms2)
print("passphrase possible permutations are {:,}".format(perms))
print("entropy of passphrase is {:.6}".format(entropy))
print("password possible permutations are {:,}".format(perms2))
print("entropy of password is {}".format(entropy2))

guesses = 100000000 # guesses per second
s = perms // guesses
m, s = divmod(s, 60)
# s_rm = s % 60
hr, m = divmod(m, 60)
# m_rm = m % 60
d, hr = divmod(hr, 24)
# hr_rm = hr % 24
yr, d = divmod(d, 365)

cracked = "{:,d} years, {:d} days, {:d} hours, {:d} minutes, and {:d} seconds".format(yr, d, hr, m, s)
print("At {:,} guesses per second,\nit would take {} to crack".format(guesses, cracked))

