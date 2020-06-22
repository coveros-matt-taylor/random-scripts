from secrets import randbelow
from timeit import default_timer as timer

def assert_equal(arg1, arg2):
  return (arg1 == arg2)

class SinglyLinkedll(object):
  """A singly-linked linked ll"""
  def __init__(self):
    self.linked_ll = []
    self.head = None

  def __repr__(self):
    return str(self.linked_ll)

  def draw(self):
    # return str(self.linked_ll)
    rtn = "null"
    for item in self.linked_ll:
      rtn += " -> " + str(item)
      if item == self.head:
        rtn += " (HEAD)"
    return rtn

  def __iter__(self):
    return iter(self.linked_ll)
  
  def add(self, node_str):
    node = SinglyLinkedNode(node_str)
    node.prev = self.head
    self.head = node
    self.linked_ll.append(node)

  def find(self, value):
    iter_head = self.head
    while iter_head is not None:
      if iter_head.value == value:
        return iter_head
      iter_head = iter_head.prev
    return False
  
  def delete(self, node):
    it = self.head
    prev = it
    index = len(self.linked_ll) - 1
    while it is not None:
      # print(self.linked_ll[index])
      if it.value == node.value:
        prev.prev = it.prev # remove current iter's link in chain
        return self.linked_ll.pop(index)
      prev = it
      it = it.prev
      index -= 1
    return False

  def getHead(self):
    return self.head

  def values(self):
    return self.linked_ll
  
  def expunge(self):
    for item in self.linked_ll:
      print(f"prev: {item.prev}")


class DoublyLinkedll(object):
  """A doubly-linked linked ll"""
  def __init__(self):
    self.linked_ll = []
    self.head = None

  def __repr__(self):
    return str(self.linked_ll)

  def add(self, node_str):
    node = DoublyLinkedNode(node_str)
    node.prev = self.head
    
    if (node.prev):
      node.prev.next = node
      node.next = node.prev.next
    else:
      node.next = None
    self.head = node
    self.linked_ll.append(node)
  
  def find(self, value):
    it = self.head
    while it is not None:
      if it.value == value:
        return it
      it = it.prev
    return False
  
  def delete(self, node):
    value = node.value
    it = self.head

    if it.value == value:
      if (it.prev):
        it.prev.next = None
      self.head = it.prev
    prev = it
    index = len(self.linked_ll) - 1
    while it is not None:
      if it.value == value:
        # delete the node
        prev.prev = it.prev # remove current iter's link in chain

        if (it.next):
          it.next.prev = it.prev # AHHHH this was borken
        
        return self.linked_ll.pop(index)
        # finish deleting
      prev = it
      it = it.prev
      index -= 1
    return False

  def draw(self):
    # return str(self.linked_ll)
    rtn = "null"
    for item in self.linked_ll:
      rtn += " <-> " + str(item)
      if item == self.head:
        rtn += " (HEAD)"
    return rtn

  def values(self):
    return self.linked_ll

  def expunge(self):
    for item in self.linked_ll:
      print(f"next: {item.next} prev: {item.prev}")
  
class SinglyLinkedNode(object):
  
  def __init__(self, value):
    self.value = value
    self.prev = None

  def __repr__(self):
    return str(self.value)

  def value(self):
    return self.value

class DoublyLinkedNode(object):
  
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

  def __repr__(self):
    return str(self.value)

  def value(self):
    return self.value
    

class Gachapon(object):
  bank = []
  def add(self, item):
    self.bank.append(item)
  
  def find(self, item):
    if item not in self.bank:
      return False
    else:
      pull = None
      while (pull != item):
        pull = self.bank[randbelow(len(bank))]
      return pull
  
  def delete(self, node):
    pass

  def draw(self):
    # return str(self.linked_ll)
    pass
    # rtn = "null"
    # for item in self.linked_ll:
    #   rtn += " <-> " + str(item)
    #   if item == self.head:
    #     rtn += " (HEAD)"
    # return rtn

  def values(self):
    return self.linked_ll


ll1 = SinglyLinkedll()
ll2 = DoublyLinkedll()
ll3 = None
linked_lls = [ll1, ll2]
for ll in linked_lls:
  
  start = timer()
  print("begin trial")
  ll.add("node1")
  ll.add("node2")
  ll.add("node3")
  print(ll)
  ll.delete(ll.find('node2'))
  print(ll)
  print(ll.draw())

  assert(ll.find("node3"))
  assert(not ll.find("bigfoot"))
  print(ll.linked_ll)
  ll.expunge()
  assert(not ll.find("node2"))

  # end my tests
  assert(not ll.find("fred"))
  ll.add("fred")
  assert_equal("fred", ll.find("fred").value)
  assert(not ll.find("wilma"))
  ll.add("wilma")
  assert_equal("fred",  ll.find("fred").value)
  assert_equal("wilma", ll.find("wilma").value)
  assert_equal(["fred", "wilma"], ll.values())
  print("end phase 1")

  # clear out the list
  ll.delete(ll.find("fred"))
  ll.delete(ll.find("wilma"))

  ll.add("fred")
  ll.add("wilma")
  ll.add("betty")
  ll.add("barney")
  assert_equal(["fred", "wilma", "betty", "barney"], ll.values())
  ll.delete(ll.find("wilma"))
  assert_equal(["fred", "betty", "barney"], ll.values())
  ll.delete(ll.find("barney"))
  assert_equal(["fred", "betty"], ll.values())
  ll.delete(ll.find("fred"))
  assert_equal(["betty"], ll.values())
  ll.delete(ll.find("betty"))
  assert_equal([], ll.values())

  elapsed = timer() - start
  print(f"Tests completed in {elapsed} seconds")
