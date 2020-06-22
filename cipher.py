import string
SHIFT = 3

alphabet = string.ascii_letters
al_set = list(alphabet)
digits = string.digits
print(alphabet)

def encypher(text):
  ciphered = ""
  for char in text:
  
    if char in al_set:
      print(al_set.index(char))
      ciphered += al_set[(al_set.index(char) + SHIFT) % len(al_set)]
    elif char in digits:
      print(char)
      ciphered += str((int(char) + SHIFT) % 10)
    else:
      print(char)
      ciphered += char
  return (ciphered)

uncyphered = input("Provide your text to encrypt: ")
print(encypher(uncyphered))
