# In Bagels, a deductive logic game, you must guess a secret four-digit number based on clues.
# A version of this game is featured in the book "The Big Book of Small Python Projects" by Al Sweigart.
# Copyright (C) 2021 Jaime Álvarez Fernández

import random
import sys

Config = {'length': 4, 'num_tries': 18, 'sorting': True}
Player = {'Name': '', 'Wins': 0, 'Loses': 0, 'error_count': 0}
information = '''\nIn Bagels, a deductive logic game, you must guess a secret {}-digit number based on clues with no 
repeated digits.
\nThe game offers one of the following hints in response to your guess:
“Pico” when your guess has a correct digit in the wrong place 
“Fermi” when your guess has a correct digit in the correct place and
“Bagels” if your guess has no correct digits. 
For example, if the secret number was 2148 and your guess was 8439, the clues would be Fermi Pico.
\nYou have {} tries to guess the secret number.
\nHave fun!'''.format(str(Config['length']), str(Config['num_tries']))


def main():
    while True:
        print('Do you need information about the game, or want different rules?(y/n)')
        answer = questions()
        if answer == 'yes':
            icb()
        elif answer == 'no':
            print("Ok. Let's play!")
            game()
        else:
            error()


def icb():
    while True:
        print('Information [i], Configuration [c] or Both [b]')
        i_c_b = questions()
        if i_c_b == 'info':
            print(information)
            game()
        elif i_c_b == 'config':
            config()
        elif i_c_b == 'both':
            print(information)
            config()
        else:
            error()


def error():
    Player['error_count'] += 1
    if Player['error_count'] > 6:
        print("That's it. I quit!")
        sys.exit()
    else:
        print('That is not a valid answer')


def questions():
    yes = ['y', 'ja', 'yes', 'sí', 'si', 'oui', '(y)', '[y]']
    no = ['n', 'no', 'nein', 'non', 'nope', '(n)', '[n]']
    info = ['i', 'info', 'information', 'h', 'help', '[i]']
    configuration = ['c', 'configuration', 'config', '[c]']
    both = ['b', 'both', 'i + c', 'i+c', 'ic', '[b]']
    sort = ['s', 'sorted', 'sorting', 'y', 'yes', 'sort']
    unsort = ['u', 'unsorted', 'n', 'no', 'unsort']
    quit_in = ['quit', 'exit', 'q']
    prime = input().lower()
    if prime in yes:
        return 'yes'
    elif prime in no:
        return 'no'
    elif prime in configuration:
        return 'config'
    elif prime in info:
        return 'info'
    elif prime in both:
        return 'both'
    elif prime in sort:
        return 'sort'
    elif prime in unsort:
        return 'unsort'
    elif prime in quit_in:
        sys.exit()


def get_secret_number():
    secret_number = []
    while len(secret_number) < Config['length']:
        x = random.randint(0, 9)
        if str(x) not in secret_number:
            secret_number.append(str(x))
    return secret_number


def check_input():
    while True:
        player_input = input().lower()
        if player_input == 'quit' or player_input == 'q':
            sys.exit()
        elif not player_input.isdigit():
            print("Input must be a number")
        elif len(player_input) != Config['length']:
            print("Input should be {} digits long".format(Config['length']))
        else:
            break
    player_list = list(player_input)
    return player_list


def config():
    print('\nWelcome to the configuration center\n')
    print('How many numbers do you want for guessing?')
    print('Standard game is with 4 digits')
    while True:
        num_length = input()
        if num_length.isdigit() and (3 <= int(num_length) <= 10):
            Config['length'] = int(num_length)
            break
        else:
            error()
            print('Value must be between 3 and 10')
    min_tries = Config['length'] ** 2 - (Config['length'] // 2)
    max_tries = (Config['length'] ** 2) + Config['length']
    print('\nAnd how many number of tries do you want?')
    print('Game difficulty is based on how many guesses you have')
    print('Easy: {}'.format(max_tries))
    print('Medium: {}'.format(Config['length'] ** 2))
    print('Hard: {}'.format(min_tries))
    while True:
        num_tries = input()
        if num_tries.isdigit() and min_tries <= int(num_tries) <= max_tries:
            Config['num_tries'] = int(num_tries)
            break
        else:
            error()
            print('Value must be between {} and {}'.format(str(min_tries), str(max_tries)))
    print('''Do you want me to sort my answers?(s/u)
Sorted: "Fermi" and "Pico" will be sorted alphabetically (Fermi Fermi Pico Pico)
Unsorted: "Fermi" and "Pico" will appear in the same order correspondent to digits (Pico Fermi Fermi Pico)''')
    while True:
        sorted_input = questions()
        if sorted_input == 'sort':
            Config['sorting'] = True
            break
        elif sorted_input == 'unsort':
            Config['sorting'] = False
            break
        else:
            error()
    print('Perfect!')
    print('New values are:')
    print('Number of digits: ' + str(Config['length']))
    print('Number of tries: ' + str(Config['num_tries']))
    if Config['sorting']:
        print('Sorting option: Sorted')
    else:
        print('Sorting option: Unsorted')
    while True:
        print('Is this alright?(y/n)')
        answer = questions()
        if answer == 'yes':
            print("Let's play!")
            print('')
            game()
        elif answer == 'no':
            config()
        else:
            error()


def game():
    player = ''
    tries = 0
    secret = get_secret_number()
    print('\nI have thought up a number.')
    print('You have {} guesses to get it.'.format(Config['num_tries']))
    for tries in range(1, Config['num_tries'] + 1):
        answer = []
        answer_clean = []
        print('Guess #' + str(tries))
        player = check_input()
        if player != secret:
            for x in range(Config['length']):
                for i in player[x]:
                    if i not in secret:
                        answer.append('Bagels')
                    elif i in secret and player[x] == secret[x]:
                        answer.append('Fermi')
                    elif i in secret:
                        answer.append('Pico')
            if answer.count('Bagels') == Config['length']:
                print('Bagels')
            else:
                for choice in answer:
                    if choice != 'Bagels':
                        answer_clean.append(choice)
            if Config['sorting']:
                answer_clean.sort()
            answer_string = ' '.join(answer_clean)
            print(answer_string)
        else:
            break
    if player == secret:
        print('Good job. You needed ' + str(tries) + ' tries.')
        Player['Wins'] += 1
    else:
        print('Ohh! Sorry. I was thinking about ' + str(''.join(secret)) + '!')
        Player['Loses'] += 1
    restart()


def restart():
    print('This is the score:')
    print('Wins: ' + str(Player['Wins']))
    print('Loses: ' + str(Player['Loses']))
    Player['error_count'] = 0
    while True:
        print('Do you want to play again(y/n)? You can access configuration tool with [c]')
        answer = questions()
        if answer == 'yes':
            game()
        elif answer == 'config':
            config()
        elif answer == 'no':
            print('Have a nice day ' + Player['Name'] + '!')
            sys.exit()
        else:
            error()


if __name__ == "__main__":
    print('Hi. What is your name?')
    while True:
        Player['Name'] = input()
        if Player['Name'] != '':
            print('Hello, ' + Player['Name'] + ". Nice to meet you!")
            break
        else:
            error()
            print('Please, tell me your name.')
    main()
