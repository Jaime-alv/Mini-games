# Copyright (C) 2021 Jaime Álvarez Fernández
from games import bagels, guess_the_number, rock_paper_scissors

games = {'bagels': bagels, 'guess the number': guess_the_number, 'rock, paper, scissors': rock_paper_scissors}


def main():
    print("Welcome!")
    print("What's your name?")
    while True:
        name = input('@: ')
        if name != '':
            break
    print(f"Nice to meet you {name}")
    print("Which game do you want to play?")
    while True:
        game = input().lower()
        if game != '':
            break
        elif game in games:
            games[game].main()
            break
        else:
            print('Please, enter a valid input!')
    print('Choose a game you want to play')


# print(games['bagels'])
if __name__ == "__main__":
    main()
