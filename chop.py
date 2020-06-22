from random import randint
from timeit import default_timer as timer

testdata = [1, 4, 5, 6, 7, 11, 17, 22, 26, 31, 40, 59]

# take 1
def bin1(data, target):
  def bin1offset(data, target, offset):
    ''' Keep track of offset when we take the greater indices' half '''

    # base case
    if len(data) == 0:
      return -1
    if target < data[0] or target > data[-1]:
      return -1
    index = -(-len(data) // 2) # ceil div
    pivot = data[index]

    if pivot == target:
      return offset + index

    elif pivot > target:
      return bin1offset(data[:index], target, offset)
    elif pivot < target:
      offset += (index-1)
      return bin1offset(data[index-1:], target, offset)

  return bin1offset(data, target, 0)

# take 2
def bin2(data, target):
  """Really shitty iterative"""
  if len(data) == 0:
      return -1
  if target < data[0] or target > data[-1]:
    return -1

  pivot = -(-len(data) // 2)

  iters = 0
  while(data[pivot] != target):
    iters += 1
    if iters > len(data)//2:
      return -1
    if data[pivot] > target:
      pivot = len(data[:pivot]) // 2
    elif data[pivot] < target:
      pivot = pivot + len(data[pivot-1:]) // 2
  return pivot

# take 3
# Hey, vince shloami here!
def bin3(data, target):
  """Effectively a dumber, more complicated version of bin1"""
  shift = 0
  
  def cut_left(data, target, index, shift):
    data = data[:index]
    return measure(data, target, shift)

  def cut_right(data, target, index, shift):
    data = data[index:]
    shift += index
    return measure(data, target, shift)
  
  def measure(data, target, shift):
    if len(data) == 0:
      return -1

    cut_index = (len(data) // 2) # floor

    if data[cut_index] == target:
      return cut_index + shift
    elif target < data[cut_index]:
      return cut_left(data, target, cut_index, shift)
    elif target > data[cut_index]:
      return cut_right(data, target, cut_index, shift)

  return measure(data, target, shift)

# take 4
def bin4(data, target):
  """Really by the book"""
  left = 0
  right = len(data) - 1
  while left <= right:
    middle = (left + right) // 2
    if data[middle] < target:
      left = middle + 1
    elif data[middle] > target:
      right = middle - 1
    else:
      return middle
  return -1

# take 5
def bin5(data, target):
  # if len(data) == 1 and data[0] != target:
  if target > data[-1] or target < data[0]:
    return -1

  def wrap(data, target):    
    middle = len(data) // 2
    if target < data[middle]:
      return wrap(data[:middle], target)
    elif target > data[middle]:
      return middle + wrap(data[middle:], target)
    else:
      return middle

  return wrap(data, target)
  # else:
  #   return -1

def bin6(data, target):
  for i, val in enumerate(data):
    if val == target:
      return i
  return -1

def run_timed(function, data, target, method="default"):
  """runs the function 10000 times and times it"""
  start = timer()
  for i in range(10000):
    function(data, target)
  print(f"completed binary sort with method '{method}' in {1000*(timer() - start):.4} ms")
  

target = 26
print(bin1(testdata, target))
print(bin2(testdata, target))
print(bin3(testdata, target))
print(bin4(testdata, target))
print(bin5(testdata, target))
print(bin6(testdata, target))

run_timed(bin1, testdata, target, 'naive recursive')
run_timed(bin2, testdata, target, "bad iterative")
run_timed(bin3, testdata, target, "inefficient")
run_timed(bin4, testdata, target, "textbook")
run_timed(bin5, testdata, target, "very recursive")
run_timed(bin6, testdata, target, "not even binary")
