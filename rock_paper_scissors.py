import random
from colorama import Fore, Back, Style
counter_player = 0
counter_computer = 0
counter_draw = 0
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
flag = True
while flag:
    while True:
        player_move = input(Fore.YELLOW + "Chose [r]ock, [p]aper or [s]cissors: ")
        print(Style.RESET_ALL)
        if player_move == 'r':
            player_move = rock
        elif player_move == 'p':
            player_move = paper
        elif player_move == 's':
            player_move = scissors
        else:
            print(Back.RED + 'Invalid Input. Try again ...')
            print(Style.RESET_ALL)
            #raise SystemExit('Invalid Input. Try again ...')
            break
        random_number = random.randint(1, 3)
        computer_move = ''
        if random_number == 1:
            computer_move = rock
        elif random_number == 2:
            computer_move = paper
        else:
            computer_move = scissors
        print(Fore.YELLOW + f'The computer chose {computer_move}.')
        print(Style.RESET_ALL)
        if (player_move == rock and computer_move == scissors) or \
                (player_move == paper and computer_move == rock) or \
                (player_move == scissors and computer_move == paper):
            counter_player += 1
            print(Fore.GREEN + "You win!")
        elif player_move == computer_move:
            counter_draw += 1
            print(Fore.BLUE + "Draw!")
        else:
            counter_computer += 1
            print(Fore.RED + 'You lose!')
        print(Fore.BLACK, Back.RED + f"Player`s score: {counter_player}\nComputer`s score: {counter_computer}\nDraws: {counter_draw}")
        chose = input(Back.RED + f"Chose [yes] to Play Again or [no] to quit: ")
        print(Style.RESET_ALL)
        if chose == 'yes':
            flag = True
        elif chose == 'no':
            print(Fore.YELLOW + f"Thank you for playing!")
            flag = False
            break