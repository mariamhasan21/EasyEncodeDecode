#Easy Encode Decode
import random
import string
random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=3)) #let the random.choices choose where to select characters from
print("_______________________Welcome_______________________")
running = True
def enicode():
  if choice.upper() == "E":
    if len(code) == 3:
      reversed_code = code[::-1] #used string method for jumping from the end to get the last number at the beginning
      print(f"Encoded message: {reversed_code}")
    elif len(code) >= 3: #if len of the code is less than 3, it doesn't add the random characters
      reversed_code = code[::-1]
      en_code = random_chars + reversed_code + random_chars
      print(f"Encoded message: {en_code}")
    else:
      print("Invalid choice")

def decode():
  if choice.upper() == "D":
    if len(code) <= 3: #since len of code is less or equal to 3, no random characters are joined. So, only the word is reversed
      reversed_code = code[::-1]
      print(reversed_code)
    elif len(code) >= 3:
      de_code = code[3:-3]
      orignal = de_code[::-1]
      print(f"Decoded message: {orignal}")
    else:
      print("Invalid choice")
while running: #while loop is used to keep the code running as long as the user don't quit
  choice = input("Please enter 'E' for Encoding And 'D' For decoding (Press 'q' to break): ")
  if choice.upper() == "Q":
    running = False #with false statment, the program stops running
    break  
  code = (input("Enter the message: "))
  if choice.upper() =="E":
    enicode()
  elif choice.upper() == "D":
    decode()

print("Thank you!")
