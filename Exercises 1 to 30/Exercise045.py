# Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
from time import sleep

jokenpolist = [1,2,3]
computer = choice(jokenpolist)

print('---------- JOKENPO GAME: ----------')
print('Select:\n[1] for ROCK,\n[2] for SCISSORS or\n[3] for PAPER.')
playerinput = int(input('Chose your fighter: '))

sleep (0.5)

if playerinput == 1:
    print(f'You chose: ROCK')
elif playerinput == 2:
    print(f'You chose: SCISSORS')
elif playerinput == 3:
    print(f'You chose: PAPER')

sleep(0.5)

if computer == 1:
    print(f'The computer chose: ROCK')
elif computer == 2:
    print(f'The computer chose: SCISSORS')
elif computer == 3:
    print(f'The computer chose: PAPER')
print(f'-' * 15, 'RESULT','-' * 15)

sleep(1)

if computer == 1:
    if playerinput == 1:
        print(f'TIE! You chose the same.')
    elif playerinput == 2:
        print(f'DEFEAT! ROCK beats SCISSORS.')
    elif playerinput == 3:
        print(f'VICTORY!! PAPER beats ROCK.')

elif computer == 2:
    if playerinput == 1:
        print(f'VICTORY!! ROCK beats SCISSORS.')
    elif playerinput == 2:
        print(f'TIE! You chose the same.')
    elif playerinput == 3:
        print(f'DEFEAT! SCISSORS beats PAPER.')

elif computer == 3:
    if playerinput == 1:
        print(f'DEFEAT! PAPER beats ROCK')
    elif playerinput == 2:
        print(f'VICTORY!! SCISSORS beats PAPER')
    elif playerinput == 3:
        print(f'TIE! You chose the same.')