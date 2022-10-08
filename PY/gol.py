# gol.py
# Alise Braick
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: https://www.youtube.com/watch?v=k8SXsT5TLxQ&t=313s + stack overflow
#------------------------------------------------------------------------------------------------------------------#
# Survivals:
# * A living cell with 2 or 3 living neighbours will survive for the next generation.
   
# Deaths:
#  * Each cell with >3 neighbours will die from overpopulation.
#  * Every cell with <2 neighbours will die from isolation.
   
# Births:
# * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.
#------------------------------------------------------------------------------------------------------------------#

# //create, initialize, and return  empty board (all cells dead) Dead cells denoted by 'x'
#  using the concept of list comprehension and applying loop for list inside a list and hence creating a 2-D list.
 
dead = "-"
alive = "a"
 
def createBoard(rows, cols):
    board = [[dead for i in range(cols)] for j in range(rows)]
    
    #print ( board ) for testing
    return (board)

#print board function
def printBoard (board):
    for i in range (len(board)):
        for j in range (len(board[i])):
            print (board[i][j], end = "")
        print ()
        

# set cell (r,c) to value
def setCell(board, r, c, value):
    board [r][c] = value
    
# return number of living neigbours of board[r][c]
def countNeighbours (board, r, c):
    
    rows = len(board)
    cols = len(board[0])
    count = 0
    
    for i in range(r-1, r+2):# r+ 2 is not included
        for j in range (c-1, c+2):# c+2 is not included
            if j >=0 and j< cols and i >=0 and i < rows:
                if not (i == r and j== c):
                    if board[i][j]== alive:
                        count = count + 1
    return count

#precond: given a board and a cell
#postcond: return next generation cell state based on CGOL rules
#(alive 'a', dead '-')
                        
def getNextGenCell(board, r, c):
    liveNeighbors = countNeighbours(board, r, c)
    # survival 
    if board[r][c] == alive and (liveNeighbors == 2 or liveNeighbors == 3):
        return alive
    #birth
    if board[r][c]== dead and liveNeighbors == 3:
        return alive
    #death due to isolation or overcrowded
    return dead
        
#generate and return a new board representing next generation
def generateNextBoard(board):
    rows = len(board)
    cols = len(board[0])
    updateBoard = createBoard(rows, cols)
    for i in range(rows):
        for j in range(cols):
            updateBoard[i][j] = getNextGenCell(board, i, j)
    return updateBoard

#------------------------------------------------------------------#
 # testing  
board = createBoard (5, 5)
setCell(board,1,1,"a")
setCell(board,2,1,"a")
setCell(board,4,2,"a")
setCell(board,2,3,"a")
setCell(board,3,4,"a")

print(printBoard(board))


print(printBoard(generateNextBoard(board)))
#print( countNeighbours (board, 2,2))









        
   
    
      
   

        