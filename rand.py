from random import random
from math import ceil, floor

TRIALS = 10000

trial = 0
one_count = 0
two_count = 0

while (trial < TRIALS):
  trial += 1

  x = ceil(random() * 2)
  if x == 1:
    one_count += 1
  elif x == 2:
    two_count +=1

print(f"Number of 1s rolled: {one_count}\nNumber of 2s roled: {two_count}")


