import random
import copy
random.seed()


print("Use W to move up\nUse S to move down\nUse A to move left\nUse D to move right\n")


def compine(x,y):
    return x+y

def printBoard(board):
    for row in board:
        print(row)

def generateTwo(board):
    place = -1
    while(place != 0):
        i = random.randint(0,3)
        j = random.randint(0,3)
        place = board[i][j]  
    board[i][j] = 2
    return board
        
def moveLeft(board):
    for i,row in enumerate(board):
        for j,element in enumerate(board[i]):
            if(element != 0):
                x = j
                while(x-1 != -1 and (board[i][x-1] == element or board[i][x-1] == 0)):
                    board[i][x] = 0
                    x -= 1
                    board[i][x] = compine(element,board[i][x])
                    
    return board


#Can be replaced with a flag in moveLeft() to detrmine whether or not to reverse
def moveRight(board):
    for i,row in enumerate(board):
        row.reverse()
        for j,element in enumerate(board[i]):
            if(element != 0):
                x = j
                while(x-1 != -1 and (board[i][x-1] == element or board[i][x-1] == 0)):
                    board[i][x] = 0
                    x -= 1
                    board[i][x] = compine(element,board[i][x])
        row.reverse()
        board[i] = row
    return board

"""
def moveDown(board):
    for i, 
"""


def start():
    board = [[32,0,0,32],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    game = True
    
    board = generateTwo(board)
    printBoard(board)

    while(game):
        state = copy.deepcopy(board)
        cmd = input("Enter your move: ")

        if(cmd.lower() == "a"):
            board = moveLeft(board)
        elif(cmd.lower() == "d"):
            board = moveRight(board)
        elif(cmd.lower()=="w"):
            pass
        elif(cmd.lower()=="s"):
            pass
        else:
            print("Wrong input")
            continue
        
        if(state != board):
            board = generateTwo(board)
        printBoard(board)




if __name__ == "__main__":
    start()
