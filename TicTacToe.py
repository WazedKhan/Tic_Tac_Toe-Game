board = {'Top-L': ' ', 'Top-M': ' ', 'Top-R': ' ',
         'Mid-L': ' ', 'Mid-M': ' ', 'Mid-R': ' ',
         'Low-L': ' ', 'Low-M': ' ', 'Low-R': ' '}


def winner(board):
    # Colunm 
    if board['Mid-R'] == board['Top-R'] == board['Low-R'] != ' ':
        return 'win'
    elif board['Mid-M'] == board['Top-M'] == board['Low-M'] != ' ':
        return 'win'
    elif board['Mid-L'] == board['Top-L'] == board['Low-L'] != ' ':
        return 'win'

    # Row
    elif board['Top-L'] == board['Top-M'] == board['Top-R'] != ' ':
        return 'win'
    elif board['Mid-L'] == board['Mid-M'] == board['Mid-R'] != ' ':
        return 'win'
    elif board['Low-L'] == board['Low-M'] == board['Low-R'] != ' ':
        return 'win'

    #Cros
    elif board['Top-L'] == board['Mid-M'] == board['Low-R'] != ' ':
        return 'win'
    elif board['Top-R'] == board['Mid-M'] == board['Low-L'] != ' ':
        return 'win'
    


def print_Theboard(board):
    print(board['Top-L'] + '|' + board['Top-M'] + '|'  +  board['Top-R'] )
    print('-+-+-')
    print(board['Mid-L'] + '|' + board['Mid-M'] + '|'  +  board['Mid-R'] )
    print('-+-+-')
    print(board['Low-L'] + '|' + board['Low-M'] + '|'  +  board['Low-R'] )


turn = 'X'
time_to_run = len(board)
while time_to_run != 0:
    print_Theboard(board)
    move = input(f'Enter Place no for {turn} :')
    if board.get(move) != ' ':
        time_to_run += 1
        print(f'This place taken by {board.get(move)}, Plz choose another place! ')
    else:      
        board[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    result = winner(board)
    if result == 'win':
        print('We have winner!')
        break
    
    time_to_run -= 1
    print(f'It is the {time_to_run-1} turn: ')
print_Theboard(board)