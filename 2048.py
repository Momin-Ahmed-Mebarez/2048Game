import random
import copy
random.seed()


print("Use W to move up\nUse S to move down\nUse A to move left\nUse D to move right\n")

#A simple addition function
def compine(x,y):
    return x+y

#A function to print the board
def printBoard(board):
    for row in board:
        print(row)

#A function to add two at a random place
def generateTwo(board):
    place = -1
    #The loop will search for a random place that doesn't have a zero to change it to two
    while(place != 0):
        i = random.randint(0,3)
        j = random.randint(0,3)
        place = board[i][j]  
    board[i][j] = 2
    return board


#Moving functions section -----------Start----------------

#There is probably a way to merge all this methodes into one

#I will only comment the first one since they all share the same logic with small tweaks

def moveLeft(board):
    for i,row in enumerate(board):
        for j,element in enumerate(board[i]):
            #Skipping any zeros
            if(element != 0):
                x = j
                #Only moving if the next square is empty or can be merged
                while(x-1 != -1 and (board[i][x-1] == element or board[i][x-1] == 0)):
                    #Replacing the old square with zero before moving
                    board[i][x] = 0
                    x -= 1
                    #Moving our element to the new square by adding it's value to the new square value
                    board[i][x] = compine(element,board[i][x])      
    return board



def moveUp(board):
    for i,row in enumerate(board):
        for j,element in enumerate(board[i]):
            if(element != 0):
                y = i
                while(y-1 != -1 and (board[y-1][j] == element or board[y-1][j] == 0)):
                    board[y][j] = 0
                    y -= 1
                    board[y][j] = compine(element,board[y][j])
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

#Can be replaced with a flag in moveUp() to detrmine whether or not to reverse
def moveDown(board):
    board.reverse()
    for i,row in enumerate(board):
        for j,element in enumerate(board[i]):
            if(element != 0):
                y = i
                while(y-1 != -1 and (board[y-1][j] == element or board[y-1][j] == 0)):
                    board[y][j] = 0
                    y -= 1
                    board[y][j] = compine(element,board[y][j])
    board.reverse()
    return board
    
# -------------------------END---------------------------




#Checking whether or not the game ended
def gameCheck(board):
    elements = []
    for i,row in enumerate(board):
        for j,element in enumerate(board[i]):
            elements.append(element)
            
    #Searching for 2048 to consider the game as a win
    if(2048 in elements): return "W"

    #Checking if there is no more zeros left 
    if(0 not in elements):
        #Checking if the player can no longer compine any square by moving horizontally or vertically
        for i,element in enumerate(elements):
            if(i != len(elements)-1):
                if(elements[i+1] == element): break
            if(not(i+4 >= len(elements)-1)):
                if(elements[i+4] == element): break
        else:
            return "L"
        
    return "C"


#Game logic
def start():
    
    #Creating the board
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
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
            board = moveUp(board)
        elif(cmd.lower()=="s"):
            board = moveDown(board)
        else:
            print("Wrong input")
            continue
        #Checking if the player made a move last turn
        if(state != board):
            board = generateTwo(board)
        
        decision = gameCheck(board)
        
        if decision == "W": game = False
        elif decision == "L": break
        

        printBoard(board)
    else:
        print("WOW you did it you win!!!\n")
        input("Press any key to exit")
        exit(1)
        
    printBoard(board)    
    print("Sadly you lost gl next time\n")
    input("Press any key to exit")
    exit(1)
        


if __name__ == "__main__":
    start()
