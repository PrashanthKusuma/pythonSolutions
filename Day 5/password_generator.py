#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '응', '&', '(', ')', '*', '+']

lettersin = int(input('How many characters you want?\n'))
specialCharacters = int(input('How many special characters you want?\n'))
numbersin = int(input('How many numbers you want?\n'))

passwordList = []
for letter in range(1, lettersin + 1):
  passwordList += random.choice(letters)

for symbol in range(1, specialCharacters + 1):
  passwordList += random.choice(symbols)

for number in range(1, numbersin + 1):
  passwordList += random.choice(numbers)

random.shuffle(passwordList)

password = ''

for char in passwordList:
  password += char

print("Your password is : ", password)
