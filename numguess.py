from random import random, seed
import random

num = random.randint(1,20)
var = input('Guess a number between 1 and 20 (inclusive): ')

def guessnum(n: int):
    guess = n
    while True:   
        if guess == num:
            print("Good guess m8!")
            return
        elif guess < num:
            guess = int(input("Higher! Guess again fool: "))
        elif guess > num:
            guess = int(input("Lower! Guess again idiot: "))

try:
    guessnum(int(var))
except ValueError:
    print("Please stop trying to break my program and just insert a regular integer")
