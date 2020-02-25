import random

with open("sowpods.txt", "r") as dictionary:
    wordlist = list(dictionary)
randomword = random.choice(wordlist).strip()
count = 0
wordlen = len(randomword)
nguesses = wordlen+1
intro = 'Welcome to hangman! Please enter individual characters to guess the word. This word has {} letters in it. You have {} guesses to figure out what the word is.'.format(wordlen,nguesses )
print(intro)
underscores = ''
for i in randomword:
    underscores += '_'
print(underscores)

while count < nguesses:
    guess = input('Guess a letter: ')
    if guess.isalpha() and len(guess) == 1:
        if guess in randomword:
            j = 0
            while j < len(randomword):
                if randomword[j] == guess:
                    underscores = underscores[:j] + guess + underscores[j+1:]
                j += 1
        count += 1
        remaining_guesses = nguesses - count
        remaining_guesses_str = 'You have {} guesses remaining.'.format(remaining_guesses)
        print(remaining_guesses_str)
        print(underscores)
        if '_' not in underscores:
            print('Congratulations, you win!')
            break
    else:
        print('Please enter a valid character')

reveal = 'The word was {}.'.format(randomword)
print('You lose :(')
print(reveal)
