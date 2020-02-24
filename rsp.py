import random

rsp = {1:'rock',
        2:'scissors',
        3:'paper'}

matchups = {'rock':'scissors',
        'scissors':'paper',
        'paper':'rock'}

losses = {'rock':'paper',
        'scissors':'rock',
        'paper':'scissors'}

while True:
    rng = rsp[random.randint(1,3)]
    message = 'The computer has selected {}'.format(rng)
    userinput = input('Please enter rock, scissors, or paper (To quit, enter ''q'' at any time): ').lower()
    if userinput == 'q':
        break
    elif userinput == matchups[rng]:
        print(message)
        print('You lose!')
    elif userinput == rng:
        print(message)
        print('Its a draw!')
    elif userinput == losses[rng]:
        print(message)
        print('Congratulations, you win! Lets play again!')
    else: 
        print('Please insert a valid input')
