status = '-'
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
turn = 0
winner = '-'


def display_board():
    print()
    print('-'*10)
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
    if turn % 2 == 0:
        print(f'Current player is X.                 Turn {turn + 1}')
    elif turn % 2 == 1:
        print(f'Current player is O.                  Turn {turn + 1}')


def check_win():
    # Checking rows
    global winner
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[1] == board[5] == board[8] != '-'
    diag1 = board[0] == board[4] == board[8] != '-'
    diag2 = board[2] == board[4] == board[6] != '-'
    if row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2:
        if turn % 2 == 0:
            winner = 'X'
        elif turn % 2 == 1:
            winner = 'O'
    else:
        pass


def check_tie():
    global winner
    if '-' not in board:
        winner = 'tie'


def handle_turn(turn):
    # Getting the move from player
    move = input('Choose a position from 1-9: ')
    # Converting the input into an integer an translating it into an index for the board list

    while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        move = input('Please choose a position from 1-9:')
    move = int(move) - 1
    if move > -1 and move < 9:
        if board[move] == '-':
            if turn % 2 == 0:
                board[move] = 'X'
            elif turn % 2 == 1:
                board[move] = 'O'
        else:
            print('Please choose a square that is not already chosen.')
            handle_turn(turn)
    else:
        print('Please choose a valid square number.')


def main_loop():
    global turn
    while winner == '-':
        display_board()
        handle_turn(turn)
        check_win()
        check_tie()
        turn += 1
    if winner != 'tie':
        print(f'{winner} won!')
    elif winner == 'tie':
        print('It is a tie!')


main_loop()
# Creating a board +
# Displaying said board +
# Choosing moves +
# Alternating players +
# Checking win and ties +
# Check rows +
# Check columns +
# Check diagonals +
