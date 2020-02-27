import string
import random

l = input('How many characters would you like your password to be? ')
n = input('How many digits would you like your password to contain? ')
c = input('How many letters would you like your password to contain? ')

alphabet = string.ascii_lowercase + string.ascii_uppercase
specials = string.punctuation
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

try:
    i = 0
    while i < c:
        i += 1
        print(random.choice(alphabet)
        continue
except ValueError: 
    print('Please stop trying to break my program and enter digits only.')
