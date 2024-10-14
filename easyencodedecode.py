import random
import string
random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
print("_______________________Welcome_______________________")
running = True
def enicode():
  if choice.upper() == "E":
    if len(code) == 3:
      reversed_code = code[::-1]
      print(f"Encoded message: {reversed_code}")
    elif len(code) >= 3:
      reversed_code = code[::-1]
      en_code = random_chars + reversed_code + random_chars
      print(f"Encoded message: {en_code}")
    else:
      print("Invalid choice")

def decode():
  if choice.upper() == "D":
    if len(code) <= 3:
      reversed_code = code[::-1]
      print(reversed_code)
    elif len(code) >= 3:
      de_code = code[3:-3]
      orignal = de_code[::-1]
      print(f"Decoded message: {orignal}")
    else:
      print("Invalid choice")
while running:
  choice = input("Please enter 'E' for Encoding And 'D' For decoding (Press 'q' to break): ")
  if choice.upper() == "Q":
    running = False
    break  
  code = (input("Enter the message: "))
  if choice.upper() =="E":
    enicode()
  elif choice.upper() == "D":
    decode()

print("Thank you!")
