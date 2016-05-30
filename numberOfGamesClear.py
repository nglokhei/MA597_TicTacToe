import numpy as np
from boardClass import *
from computerInput import *
from convert import *

board = Board(isVisual = False)

def makeMove(board, playerTurn,possibleSteps = []):
    getWin = board.checkTwo(playerTurn)
    if getWin > 0:
        #print(board.board)
        #print("player {0} win".format(playerTurn))
        return 1

    urgent = board.checkTwo(playerTurn % 2 + 1)
    if urgent > 0:
        (i,j) = poleCoord(urgent)
        (i,j,k) = board.findPutTokensLoc((i,j))
        #print((i,j))
        #print ((i,j,k))
        board.board[i][j][k] = playerTurn
        #print(board.board)
        retval = makeMove(board, (playerTurn % 2 + 1))
        board.board[i][j][k] = 0
        return retval

    retval = 0
    if possibleSteps == []:
        possibleSteps = getPossibleSteps(board, False)
    
    #print(possibleSteps)

    for step in possibleSteps:
        #print(step)
        (i,j,k) = board.findPutTokensLoc(step)
        #print((i,j,k))
        board.board[i][j][k] = playerTurn
        #print(board.board)
        retval = retval + makeMove(board, playerTurn%2+1)
        board.board[i][j][k] = 0
        #print(retval)
    return retval

count = makeMove(board,1,[(0,0),(0,1)])
print(count)
