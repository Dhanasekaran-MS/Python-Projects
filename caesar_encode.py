#art

logo="""
  ___ __ _  ___  ___  __ _ _ __  
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|   
      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                    
"""

#main

# from art import logo

print(logo)

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z'
]

#def encrypt(plain_text, shift_amount):
# cipher_text = ""
#  for letter in plain_text:
#    position = alphabet.index(letter)
#    new_position = position + shift_amount
#    cipher_text += alphabet[new_position]

#  print(f"The Coded text is : {cipher_text}")

#def decrypt(cipher_text,shift_amount):
#  plain_text=""
# for letter in cipher_text:
#   position = alphabet.index(letter)
#  new_position = position-shift_amount
# plain_text += alphabet[new_position]

#print(f"The Decoded text is : {plain_text}")


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == 'decode':
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"The {cipher_direction}d text is : {end_text}")


#if direction=='encode':
# encrypt(plain_text=text,shift_amount=shift)
#elif direction=='decode':
# decrypt(cipher_text=text,shift_amount=shift)
contin = True
while contin:
  direction = input("Type 'encode' to Encrypt and 'decode' to Decrypt : \n").lower()
  text = input("Enter the Text : ").lower()
  shift = int(input("Type the Shift Number : "))
  shift %= 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("If you want to continue type 'yes' and to stop type 'no' :").lower()
  if result == 'no':
    contin = False
    print(" GOOD BYE ")


