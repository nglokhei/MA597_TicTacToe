import numpy as np

from convert import *

def getPossibleSteps(board1, first):

    possibleSteps = []
    for i in range(0,3):
        for j in range(0,3):
            if board1.validPut((i,j), first):
                possibleSteps.append((i,j))

    return possibleSteps

def computerInput(board1, playerTurn, first):
    getWin = board1.checkTwo(playerTurn)
    if getWin > 0:
        return poleCoord(getWin)
    
    urgent = board1.checkTwo(playerTurn % 2 + 1)
    if urgent > 0:
        return poleCoord(urgent)

    possibleSteps = getPossibleSteps(board1, first)

    idx = np.random.randint(0, len(possibleSteps))
    return possibleSteps[idx]
            
