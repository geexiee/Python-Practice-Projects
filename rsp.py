import random

rsp = {1:'rock',
        2:'scissors',
        3:'paper'}

matchups = {'rock':'scissors',
        'scissors':'paper',
        'paper':'rock'}

rng = rsp[random.randint(1,3)]
while True:
    userinput = input('Please enter rock, scissors, or paper (To quit, enter ''q'' at any time):')
    if userinput == 'q':
        break
    elif userinput == matchups[rng]:
        print('You lose!')
    else:
        print('Congratulations! Lets play again!')
    
