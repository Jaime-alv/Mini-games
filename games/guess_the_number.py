# This is a guess the number game
# You have 5 tries or you'll lose the game
# The game tracks wins/loses ratio
# Copyright (C) 2021 Jaime Álvarez Fernández

import random

win_global = 0
lose_global = 0
name_global = ''


def main():
    global name_global
    print('Hi. What is your name?')
    name = input()
    while True:
        if name != '':
            print('Hello, ' + name + ". Nice to meet you!")
            print('Do you want to play a guessing game?(y/n)')
            name_global = name
            yes_no()
        else:
            print('That is not a valid name. Please, tell me your name')
            name = input()


def yes_no():
    yes = ['y', 'ja', 'yes', 'sí', 'si', 'oui']
    prime = input()
    prime = prime.lower()
    for i in yes:
        if i == prime:
            game()
        else:
            print('Have a nice day ' + name_global + '!')
            quit()


def check_input():
    while True:
        print('Can you guess it?')
        number = input()
        if number.isdigit():
            return int(number)


def game():
    global win_global
    global lose_global
    print("I'm thinking of a number between 1 and 50")
    guess_number = random.randint(1, 50)
    for tries in range(1, 6):
        guess = check_input()
        if guess > guess_number:
            print('Your guess is to high')
        elif guess < guess_number:
            print('Your guess is too low')
        else:
            break
    if guess == guess_number:
        print('Good job ' + name_global + '. You needed ' + str(tries) + ' tries.')
        win_global += 1
    else:
        print('Sorry. It was ' + str(guess_number))
        lose_global += 1
    restart()


def restart():
    print('This is the score:')
    print('Wins: ' + str(win_global))
    print('Loses: ' + str(lose_global))
    print('Do you want to play again?(y/n)')
    yes_no()


if __name__ == "__main__":
    main()
