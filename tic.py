

#take input from the user





empty_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
test_board = ['#','X','O','X','O','X','O','X','O','X']


def display_board(board):
    
    print('   ' + "|" + '   ' + "|" + '   ')
    print(' '+ board[7] + " | " + board[8]  + " | " + board[9] + ' ')
    print('   ' + "|" + '   ' + "|" + '   ')
    print('-----------')
    print('   ' + "|" + '   ' + "|" + '   ')
    print(' '+ board[4] + " | " + board[5]  + " | " + board[6] + ' ')
    print('   ' + "|" + '   ' + "|" + '   ')
    print('-----------')
    print('   ' + "|" + '   ' + "|" + '   ')
    print(' '+ board[1] + " | " + board[2]  + " | " + board[3] + ' ')
    print('   ' + "|" + '   ' + "|" + '   ')


def player_input():
    
    player1='f'
    
    while player1 not in ('X','O'):
        player1 = input("Player1 pick a marker 'X' or 'O': ")
    return player1   


import random

def choose_first():
    choices=['p1','p2']
    first = random.choice(choices)
    return first




def place_marker(board, marker, position):
    print(board[position])
    while  board[position] != ' ':
        print("Already chosen - choose another position")
        position=int(input("choose postion from 1 - 9: "))
        
    board[position] = marker




def win_check(board, mark):
  
    if board[1] == mark and board[2] == mark and board[3] == mark or \
       board[4] == mark and board[5] == mark and board[6] == mark or \
       board[7] == mark and board[8] == mark and board[9] == mark or \
       board[1] == mark and board[4] == mark and board[7] == mark or \
       board[2] == mark and board[5] == mark and board[8] == mark or \
       board[3] == mark and board[6] == mark and board[9] == mark or \
       board[7] == mark and board[5] == mark and board[3] == mark or \
       board[1] == mark and board[5] == mark and board[9] == mark:            
        return True
    else:
        return False
    

# display_board(test_board)
# print("\n")
#display_board(empty_board)

print("WELCOME TO TIC TAC TOE!")

player1 = player_input()

if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'

first = choose_first()

# place_marker(empty_board,player1,1)
# display_board(empty_board)
# place_marker(empty_board,player1,3)
# display_board(empty_board)
display_board(empty_board)

if first =='p1':
    print("Player1 will start first")
else:
    print("Player2 will start first")

winner =False

while(winner==False):

    if first =='p1':
        pos=int(input("choose postion from 1 - 9: "))
        place_marker(empty_board,player1,pos)
        display_board(empty_board)
        winner = win_check(empty_board,player1)
        if winner==True:
            print("PLAYER 1 WINS!")
            break

        pos=int(input("choose postion from 1 - 9: "))
        place_marker(empty_board,player2,pos)
        display_board(empty_board)
        winner = win_check(empty_board,player2)
        if winner==True:
            print("PLAYER 2 WINS!")
            break
        
    else:   
        pos=int(input("choose postion from 1 - 9: "))
        place_marker(empty_board,player2,pos)
        display_board(empty_board)
        winner = win_check(empty_board,player2)
        if winner==True:
            print("PLAYER 2 WINS!")
            break
        pos=int(input("choose postion from 1 - 9: "))
        place_marker(empty_board,player1,pos)
        display_board(empty_board)
        winner = win_check(empty_board,player1)
        if winner==True:
            print("PLAYER 1 WINS!")
            break
       





print("GAME OVER !!!!")

