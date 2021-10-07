# A classic rock, paper, scissors game. Computer draws an option, you write another and compare results.
# Scissors wins paper, paper wins rock, rock wins scissors.
# You can exit the program at any time by typing 'q'
# Copyright (C) 2021 Jaime Álvarez Fernández

import random

Score = {'Wins': 0, 'Loses': 0, 'Ties': 0}
Config = {'Infinite_mode': True, 'Number_of_rounds': 0}
Options = {'r': 'rock', 'p': 'paper', 's': 'scissors'}


def game():
    wins = ['rock scissors', 'scissors paper', 'paper rock']
    pc = random.choice(list(Options.values()))
    print('I made my choice')
    print("Let's see yours!")
    player_input = Options[check_player()]
    if player_input != pc:
        if (player_input + ' ' + pc) in wins:
            print('You win! My choice was {}'.format(pc))
            Score['Wins'] += 1
        else:
            print('I win! My choice was {}'.format(pc))
            Score['Loses'] += 1
    else:
        print("It's a tie!")
        Score['Ties'] += 1


def check_player():
    while True:
        print('Choose an option: rock, paper or scissors [r/p/s]')
        player = input().lower()
        if player not in Options and player != 'q':
            print('Please, enter a valid input')
        elif player == 'q':
            goodbye()
        else:
            return player


def main():
    print('Welcome to the game!')
    print('This is the configuration center')
    while True:
        print('How many rounds do you want to play?')
        print('Input should be a number or type i for an infinite number of rounds')
        print('You can exit the program, at any time, by typing q')
        rounds = input().lower()
        if rounds == 'q':
            goodbye()
        if rounds != 'i' and not rounds.isdigit() or rounds == '0':
            print('Enter a valid input')
        else:
            break
    if rounds.isdigit():
        Config['Infinite_mode'] = False
        Config['Number_of_rounds'] = int(rounds)
    looping()


def score():
    print('\nScore: Wins = {} Loses = {} Ties = {}'.format(Score['Wins'], Score['Loses'], Score['Ties']))
    print('Ratio = ' + str(round(Score['Wins'] * 100 / (Score['Wins'] + Score['Loses'] + Score['Ties']), 2)) + '%')


def looping():
    y = 0
    while Config['Infinite_mode']:
        y += 1
        print('\nRound number ' + str(y) + '\n')
        game()
        score()
    for x in range(1, Config['Number_of_rounds'] + 1):
        print('\nRound number ' + str(x) + '\n')
        game()
        score()
    goodbye()


def goodbye():
    print('\nGoodbye! Have a nice day!')
    quit()


if __name__ == "__main__":
    main()
