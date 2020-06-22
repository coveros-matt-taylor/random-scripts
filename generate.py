from secrets import randbelow
from math import factorial
from math import log2 as ln

"""EUA passwords must...
 - start with a letter
 - have at least one number
 - have at least one lowercase and one uppercase
 - be EXACTLY 8 charcters long (WHYYY)
"""
PP_LENGTH = 3
ASCII_PWD_LENGTH = 8
TRIALS = 10
EUA = True

separators = True
titlecase = True
numbers = 2 # 0-9

breakpoints = {}
breakpoints[20] = "very weak" # 0-20
breakpoints[40] = "weak" # 20-40
breakpoints[60] = "good enough" # 40-60
breakpoints[80] = "strong" # 60-80
breakpoints[99999999] = "very strong" # 80+

wordlist = []
with open('google-10000-english-usa-no-swears-medium.txt') as f:
    for word in f:
        wordlist.append(word.split()[0])

length = len(wordlist)

sep_num = (PP_LENGTH-1)
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" #!@#$%^&*
perms = length ** PP_LENGTH + (8 ** sep_num) + (9 ** sep_num)
ascii_perms = len(charset) ** ASCII_PWD_LENGTH # 26 upper + 26 lower + 10 numbers
# print(length)
# print("number of words: {}".format(length))

for j in range(TRIALS):
    pp = ""
    words = []
    seps = []
    for i in range(PP_LENGTH):
        if titlecase:
            words.append(wordlist[randbelow(length)].title())
        else:
            words.append(wordlist[randbelow(length)])
    pp = words[0]
    for word in words[1:]:
        sep = "!@#$%^&*"[randbelow(8)] if separators else ""
        pp += sep + word
    for i in range(numbers):
        pp += str(randbelow(10))

    print(pp)

    ####### Ascii #######
    if EUA:
        pw = ""
        for i in range(ASCII_PWD_LENGTH):
            pw += charset[randbelow(len(charset))]
        
        print(pw)



# perms2 = 26 ** 3 + 9 ** 5
passphrase = {"name": "PASSPHRASE", "perms": perms, "length": PP_LENGTH}
ascii_pwd = {"name": "ASCII PASSWORD", "perms": ascii_perms, "length": ASCII_PWD_LENGTH}
# methods = [passphrase, ascii_pwd]
methods = [passphrase]

MY_LAPTOP_GUESS_SPEED = 2652509

for method in methods:

    tperms = method['perms']

    # print("*"*8,'calulations for method {}'.format(method['name']),"*"*20)
    # print("    passphrase possible permutations are {:,}".format(tperms))
    entropy = ln(tperms)
    # print("    entropy of {} is {:.6}".format(method['name'].lower(), entropy))
    if (entropy < 20):
        print("very weak")
    elif (20 <= entropy < 35):
        print("weak")
    elif (35 <= entropy < 55):
        print("good enough")
    elif (55 <= entropy < 80):
        print("strong")
    else:
        print("very strong")

    print("{:.4} bits of entropy".format(entropy))
    guesses = 10000000 # guesses per second

    for i in range(1):
        # s = perms // guesses
        s = tperms // guesses
        m, s = divmod(s, 60)
        hr, m = divmod(m, 60)
        d, hr = divmod(hr, 24)
        yr, d = divmod(d, 365)

        cracked = "{:,d} years, {:d} days,\n    {:d} hours, {:d} minutes,\n    and {:d} seconds".format(yr, d, hr, m, s)
        print("    At {:,} guesses per second,\n    it would take {} to crack".format(guesses, cracked))
        guesses *= 10

