from random import random, seed
import random

num = random.randint(1,20)
var = input('Guess a number: ')

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

guessnum(int(var))
