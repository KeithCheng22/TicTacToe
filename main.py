import os
import random


board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


def clear_console(): return os.system('clear')


# How to identify a win or a draw
def all_spaced_used():
    if board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[1][0] != ' ' and board[1][
        1] != ' ' and board[1][2] != ' ' and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' ':
        return True


def victory():
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or board[0][0] == 'O' and board[1][0] == 'O' and \
            board[2][0] == 'O':
        return True
    elif board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or board[0][0] == 'O' and board[0][
        1] == 'O' and board[0][2] == 'O':
        return True
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' or board[2][0] == 'O' and board[2][
        1] == 'O' and board[2][2] == 'O':
        return True
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X' or board[0][2] == 'O' and board[1][
        2] == 'O' and board[2][2] == 'O':
        return True
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or board[1][0] == 'O' and board[1][
        1] == 'O' and board[1][2] == 'O':
        return True
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or board[0][1] == 'O' and board[1][
        1] == 'O' and board[2][1] == 'O':
        return True
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or board[0][0] == 'O' and board[1][
        1] == 'O' and board[2][2] == 'O':
        return True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X' or board[0][2] == 'O' and board[1][
        1] == 'O' and board[2][0] == 'O':
        return True


# Styling Board
def show_board():
    num = 1
    rows = len(board)
    print("     1    2    3")
    print("   ----+-----+----")
    for row in range(rows):
        x = str(board[row])
        x = x.replace("[","")
        x = x.replace("]","")
        x = x.replace(",", ' |')
        x = x.replace("' '", ' _ ')
        print(f"{num}  {x}")
        num += 1
        print("   ----+-----+----")

play_again = True
print('Welcome to Tic-Tac-Toe!')
while play_again:
    choice = input('Do you want to play? Y or N: ').upper()
    clear_console()
    # Decide who is X and O
    if choice == 'Y':
        for pieces in board:
            for spot in pieces:
                if spot == 'X':
                    pieces[pieces.index('X')] = ' '
                if spot == 'O':
                    pieces[pieces.index('O')] = ' '

        player_1_name = input('Player 1\'s Name: ')
        player_2_name = input('Player 2\'s Name: ')
        players = [player_2_name, player_1_name]
        choice = random.choice(players)
        clear_console()
        while True:


            # PLAYER1_PIECE = input('Player 1 - Do you want to be "X" or "O"?: ').upper()
            f'{choice}'
            PLAYER1_PIECE = input(f'{choice} - Do you want to be "X" or "O"?: ').upper()
            if PLAYER1_PIECE == "X":
                PLAYER2_PIECE = "O"
                break
            elif PLAYER1_PIECE == 'O':
                PLAYER2_PIECE = "X"
                break
            else:
                print('Please choose either "X" or "O"!')

        clear_console()
        print('Instructions: \nEach spot on the board is based on a row and column.\nWhen placing a piece on the board, type the row number followed by the column number. \nFor example, a middle spot would have the position of 22.')
        show_board()

        # Gameplay Code
        game_continues = True
        # Allow Players to put their pieces on the board
        while game_continues:
            while True:
                try:
                    player1 = int(input(f'{player_1_name}\'s Turn: '))
                    last_digit = player1 % 10 - 1
                    first_digit = int((player1 - last_digit) / 10) - 1

                    if 0 <= last_digit <= 2 and 0 <= first_digit <= 2:
                        if board[first_digit][last_digit] == ' ':
                            board[first_digit][last_digit] = PLAYER1_PIECE
                            clear_console()
                            show_board()
                            break
                        else:
                            print('Spot has been taken, please choose another spot!')
                    else:
                        print('Please input a valid spot!')
                except ValueError:
                    print('Please input a valid spot!')

            if victory():
                game_continues = False
                print(f'{player_1_name} Wins. Game Over.')
            elif victory() != True and all_spaced_used():
                print("It's a Draw")
                game_continues = False
            else:
                while True:
                    try:
                        player2 = int(input(f'{player_2_name}\'s Turn: '))
                        last_digit = player2 % 10 - 1
                        first_digit = int((player2 - last_digit) / 10) - 1

                        if 0 <= last_digit <= 2 and 0 <= first_digit <= 2:
                            if board[first_digit][last_digit] == ' ':
                                board[first_digit][last_digit] = PLAYER2_PIECE
                                clear_console()
                                show_board()
                                break
                            else:
                                print('Spot has been taken, please choose another spot!')
                        else:
                            print('Please input a valid spot!')
                    except ValueError:
                        print('Please input a valid spot!')

                if victory():
                    game_continues = False
                    print(f'{player_2_name} Wins. Game Over.')

                elif victory() != True and all_spaced_used():
                    print("It's a Draw")
                    game_continues = False
    elif choice == 'N':
        print('Goodbye! Thanks for playing!')
        play_again = False
    else:
        print('Please input Y or N')

