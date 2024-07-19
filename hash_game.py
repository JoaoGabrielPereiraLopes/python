# in this code my objective is chalenge my knowledge make one hash game 
import pandas as pd

player1_points=0#points of player 1
player2_points=0#points of player 2
height=0
width=0

def generator():#create a board
    board=[]

    for depth in range(0,3):

        board.append(['_','_','_'])

    return board

board=generator()#received the list represent board

def hash():#check if is hash

    for line in range(0,3):

        for house in range(0,3):

            if board[line][house]!=" ":
                return False

            elif line==2 and house==2:
                return True

def vitoria_O(player1_points):#check if player 1 wins
    for line in board:

        if line[0]=='O' and line[1]=='O' and line[2]=='O':
            print(f'victory of player 1 in horizontal{ heigth}')
            print(f'player1-{ player1_points+1 }\nplayer2-{ player2_points }')
            return True
            
    for vertival in range(0,3):

        if board[0][vertival]=="O" and board[1][vertival]=="O" and board[2][vertival]=="O":
            print(f'victory of player 1 in vertical{width}')
            print(f'player1-{ player1_points+1 }\nplayer2-{ player2_points}')
            return True
    
    if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        print(f'victory of player 1 in diagonal1')
        print(f'player1-{ player1_points+1 }\nplayer2-{ player2_points}')
        return True
    
    elif board[2][0]=="O" and board[1][1]=="O" and board[0][2]=="O":
        print(f'victory of player 1 in diagonal2')
        print(f'player1-{ player1_points+1 }\nplayer2-{ player2_points}')
        return True
    
def vitoria_X(player2_points):#check if player 1 wins

    for line in board:

        if line[0]=='X' and line[1]=='X' and line[2]=='X':
            print(f'victory of player 2 in horizontal{ heigth}')
            print(f'player1-{ player1_points }\nplayer2-{ player2_points+1 }')
            return True
            
    for vertival in range(0,3):

        if board[0][vertival]=="X" and board[1][vertival]=="X" and board[2][vertival]=="X":
            print(f'victory of player 2 in vertical{width}')
            print(f'player1-{ player1_points }\nplayer2-{ player2_points+1}')
            return True
    
    if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        print(f'victory of player 2 in diagonal1')
        print(f'player1-{ player1_points}\nplayer2-{ player2_points+1 }')
        return True
    
    elif board[2][0]=="O" and board[1][1]=="O" and board[0][2]=="O":
        print(f'victory of player 2 in diagonal2')
        print(f'player1-{ player1_points+1 }\nplayer2-{ player2_points}')
        return True

rodada=0

while True:

    print(pd.DataFrame(board))
    width=int(input('inform a X cordenate: '))#colect the X cordenate the movie of player
    heigth=int(input('inform a Y cordenate: '))#colect the X cordenate the movie of player
    #the cordenate sistem starts at one to make it easier comprended for usuary

    if width>=0 and width<3 and height>=0 and height<3:

        if rodada%2==0 and board[heigth][width]=="_":
            board[heigth][width]='O'#if is player1 turn regist O in the case of board
            rodada+=1

        elif rodada%2==1 and board[heigth][width]=="_":
            board[heigth][width]='X'#if is player2 turn regist X in the case of board
            rodada+=1
        
        if vitoria_O(player1_points):#verifi if player 1 win
            board=generator()
            player1_points+=1

        elif vitoria_X(player1_points):#verifi if player 1 win
            board=generator()
            player2_points+=1

        elif hash():
            board=generator()
            print('hash')

    else:
        print('invalid cordenate')