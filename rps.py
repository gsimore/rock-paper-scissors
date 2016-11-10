'''
Rock paper scissors.
vs. the computer

rock > scissors ;
scissors > paper;
paper > rock
'''

import random

#dict_choices = {'r':'rock', 'p':'paper', 's':'scissors'}
choices = ('r', 'p', 's')
user_name = input('Enter your user name: ')
your_score = 0
cpu_score = 0

score = "Computer: {} \
        Your score: {} \
        Cpu score: {}."

while your_score < 3 and cpu_score < 3:
    your_choice = input('Enter (r)ock, (p)aper, or (s)cissors: ')
    computer = random.choice(choices)
    if your_choice == computer:
        print('Blank!')
    elif your_choice == 'r' and computer != 'p':
        your_score += 1
    elif your_choice == 's' and computer != 'r':
        your_score += 1
    elif your_choice == 'p' and computer != 's':
        your_score += 1
    elif your_choice not in choices:
        your_choice = input('Invalid choice. Enter r, p, or s')
    else:
        cpu_score += 1
    print(score.format(computer, your_score, cpu_score))


if your_score == 3:
    print('{} wins!'.format(user_name))
if cpu_score == 3:
    print('You lose!')
