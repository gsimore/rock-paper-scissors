'''
Rock paper scissors.
vs. the computer

rock > scissors ; 0 > 2
scissors > paper;
paper > rock

First player with a score of 3 wins!

* mod: play to get best 2 out of 3

'''

import random


choices = ('r', 'p', 's')
user_name = input('Enter your user name: ')
play_prompt = 'Enter (r)ock, (p)aper, or (s)cissors:  '
your_score = 0
cpu_score = 0
tries = 0

score = '''
        Your choice: {} \t|\t Opponent's choice: {}
        Your score: {} \t|\t Computer score: {}
        Out of {} tries.
        '''

def play_game():
    while your_score < 2 and cpu_score < 2:
        your_choice = input(play_prompt)
        computer = random.choice(choices)

        if your_choice == computer:
            tries += 1
            print('\tTie!')
        elif your_choice == 'r' and computer != 'p':
            your_score += 1
            tries += 1
        elif your_choice == 's' and computer != 'r':
            your_score += 1
            tries += 1
        elif your_choice == 'p' and computer != 's':
            your_score += 1
            tries += 1
        else:
            cpu_score += 1
            tries += 1
        print(score.format(your_choice, computer, your_score, cpu_score, tries))


while your_choice not in choices:
    your_choice = input('Invaid answer.' + ' ' + play_prompt)


if tries >= 3:
    if your_score == cpu_score:
        your_choice = input('Tie Breaker!' + ' ' + play_prompt)
        computer = random.choice(choices)
        tries += 1
        print(score.format(your_choice, computer, your_score, cpu_score, tries))
    elif your_score == 2 and cpu_score < 2:
        print('{} wins!'.format(user_name))
    elif cpu_score == 2 and your_score < 2:
        print('Computer wins!')
    else:
        your_choice = input('No winner yet! One more round.' + ' ' + play_prompt)
        computer = random.choice(choices)
        tries += 1
        print(score.format(your_choice, computer, your_score, cpu_score, tries))
