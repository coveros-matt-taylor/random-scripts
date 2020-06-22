from secrets import randbelow
from timeit import default_timer as timer
from itertools import product

import numpy as np

def cartesian_product(*arrays):
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)

# METHOD = "itertools"
METHOD = "itertools"

target = "password"
array_target = np.asarray([c for c in target])
print(array_target)
validchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# validchars = set(validchars)
# validchars = np.array(validchars)
validchars = np.asarray([c for c in validchars])
# print(validchars)

if METHOD == "itertools":
    start = timer()
    count = 0

    # previously, before numpy: for chars in product(validchars, repeat=len(target)):
    result = product(validchars, repeat=len(target))
    for chars in result:
        count += 1
        guess = "".join(chars)
        # print(word)
        if guess == target:
            print(guess)
            break
    
    elapsed = timer() - start
    print("{:,} guesses in {} seconds".format(count, elapsed))
    print("{:,} guesses per second".format(count/elapsed))

# METHOD = "numpy"
# print("----- Method 2 -----")
if METHOD == "numpy":

    start = timer()
    result = cartesian_product(*[validchars for i in range(len(target))])
    for c in result:
        if np.array_equal(c, array_target):
            print("".join(c))
            break

    # # real = np.intersect1d(result, array_target)
    # print(np.isin(array_target, result))

    elapsed = timer() - start
    print("{:,} guesses in {} seconds".format(len(result), elapsed))
    print("{:,} guesses per second".format(len(result)/elapsed))
# print("# results: {} vs # expected perms {}".format(len(results), (len(validchars) ** len(target))))