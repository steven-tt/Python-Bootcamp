import random

def display_board(board):
    '''
    This displays the 3x3 board and takes a list, that is of length 10 with place [0] being whatever as a place holder, as an input.
    '''
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print(f'-----------')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print(f'-----------')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    
def first_player_marker():
    '''
    This picks the first players marker
    '''
    marker =''
    while marker != 'X' and marker !='O':
        marker = str(input(f'{first} please pick "X" or "O" : ')).upper()
        if marker != 'X' and marker !='O':
            print('Can you not read or type?')
    else:
        print(f'Congratulations {first} you chose {marker}.')
        return marker
        
def second_player_marker():
    '''
    This picks the second players marker. It uses the variable local to the game instead of an input.
    '''
    if first_marker == 'X':
        print(f'{second} you are O')
        return 'O'
    else:
        print(f'{second} you are X')
        return 'X'
    
def choose_first():
    '''
    This chooses which of the two players as an inpur
    '''
    choice = random.randint(0,1)
    if choice == 0:
        return player1
    if choice == 1:
        return player2

def choose_second(player1,player2):
    '''
    Uses the input from the first player function
    '''
    if first == player1:
        return player2
    else:
        return player1
        
def place_marker(board, marker, position):
    board[position]=marker
    
def win_check(board, marker):
    if board[9]==board[8]==board[7]==marker.upper():
        return True
    elif board[6]==board[5]==board[4]==marker.upper():
        return True
    elif board[1]==board[2]==board[3]==marker.upper():
        return True
    elif board[9]==board[6]==board[3]==marker.upper():
        return True
    elif board[8]==board[5]==board[2]==marker.upper():
        return True
    elif board[7]==board[4]==board[1]==marker.upper():
        return True
    elif board[9]==board[5]==board[1]==marker.upper():
        return True
    elif board[7]==board[5]==board[3]==marker.upper():
        return True
    else:
        return False
    
def space_check(board,position):
    return board[position] == ' '
    
def full_board_check(board):
    for i in board[1:9]:
        if i == ' ':
            return False
    return True

def player_choice(board,marker):
    while True:
        place = int(input("Please choose an open position: "))
        if board[place] != ' ':
            print('Use your eyes the place you chose is not blank')
            continue
        else:
            board[place] = marker
            break
        
def replay():
    Pass

########## The Game ##########

print('Welcome to Tic Tac Toe!')
print('')

#Players picking their name
player1 = input("Please choose a name for Player 1 : ")
player2 = input('Please choose a name for Player 2 : ')
print('')

#The start of the game
while True:
    
    #Rules
    board = ['#'] + list(range(1,10))
    display_board(board)
    print('')
    print('Please pay attention to the numbers. This is how you will be choosing your moves.')
    
    #Choosing player order and their markers
    first = choose_first()
    second = choose_second(player1,player2)
    print('')
    print(f'{first} will be going first\n{second} will be going second')
    print('')
    first_marker = first_player_marker()
    second_marker = second_player_marker()
    
    #Setting up clear board to start game
    input('Ready? (type in anything)')
    board = ['#'] + [' '] * 9
    print('\n' * 100) 
    #Game 
    while True:
        
        #Player ones turn
        print(f"It is {first}'s turn. Please place an {first_marker} in an open position.")
        print('')
        display_board(board)
        player_choice(board,first_marker)
        if win_check(board,first_marker):
            print(f'{first} wins!')
            display_board(board)
            break
        if full_board_check(board):
            print('Tie Game')
            display_board(board)
            break
        print('\n' * 100)
            
        #Player two's turn
        print(f"It is {second}'s turn. Please place an {second_marker} in an open position.")
        display_board(board)
        player_choice(board,second_marker)
        if win_check(board,second_marker):
            print(f'{second} wins!')
            display_board(board)
            break
        if full_board_check(board):
            print('Tie Game')
            display_board(board)
            break
        print('\n' * 100)
    
    break