# playerNum of player 'X' is 1
# playerNum of player 'O' is 2

def poleCoord(poleNum):
    poleNum = poleNum - 1
    return (poleNum//3,poleNum%3)

def playerName(playerNum):
    if playerNum == 1 :
        return 'X'
    else :
        return 'O'

def playerNum(playerName):
    if playerName == 'O':
        return 2
    else:
        return 1
