import time
import random as r

yourScore = 0
computerScore = 0

while True:
    player = input('Select: rock, paper, scissors')
    if player == 'rock' or player == 'scissors' or player == 'paper':
        computer = r.randint(1, 3)
        if computer == 1:
            computer = 'rock'
        elif computer == 2:
            computer = 'scissors'
        else:
            computer = 'paper'
        print('Rock, paper, scissors!')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('The computer selected:', computer)
        if computer == player:
            print('Draw')
        elif player == 'rock' and computer == 'scissors':
            print('You win!')
            yourScore = yourScore + 1
        elif player == 'paper' and computer == 'rock':
            print('You win!')
            yourScore = yourScore + 1
        elif player == 'scissors' and computer == 'paper':
            print('You win!')
            yourScore = yourScore + 1
        else:
            print('You lost!')
            computerScore = computerScore + 1
        print('Score: You:', yourScore, ', Computer:', computerScore)
        
    else:
        print('Error: bad input')
