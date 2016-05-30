import numpy as np

from draw import *

class Board:
    def __init__(self, buttonString = "", isVisual = True, arr = np.zeros((3,3,3))):
        self.board = np.copy(arr)
        self.isVisual = isVisual
        if isVisual:
            (self.poles, self.base) = drawBoard()
            self.tmpTokens = drawTmpTokens()
            self.hasButton = (len(buttonString) > 0)
            if self.hasButton:
                self.button = drawButton(buttonString)

    def putTokens(self, pickedCoord, game, anim = False):
        (i,j,k) = pickedCoord
        self.board[i][j][k] = game.playerTurn
        game.steps.append((i,j,k))
        if anim:
            game.tokens = putTokensAnim(self, (i,j,k), game.tokens)

        return


    def checkTwo(self, playerTurn):
        for pole in range(1,10):
            tmpBoard = Board("", False, self.board)
            coord = poleCoord(pole)
            if tmpBoard.validPut(coord):
                (i,j,k) = tmpBoard.findPutTokensLoc(coord)
                tmpBoard.board[i][j][k] = playerTurn
                if tmpBoard.checkWin():
                    return pole

        return 0

    def checkWin(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j][0] == self.board[i][j][1] and self.board[i][j][0] == self.board[i][j][2] and self.board[i][j][2] != 0:
                    return self.board[i][j][0]
                if self.board[i][0][j] == self.board[i][1][j] and self.board[i][0][j] == self.board[i][2][j] and self.board[i][2][j] != 0:
                    return self.board[i][0][j]
                if self.board[0][i][j] == self.board[1][i][j] and self.board[0][i][j] == self.board[2][i][j] and self.board[2][i][j] != 0:
                    return self.board[0][i][j]
            if self.board[i][0][0] == self.board[i][1][1] and self.board[i][0][0] == self.board[i][2][2] and self.board[i][2][2] != 0:
                return self.board[i][0][0]
            if self.board[i][2][0] == self.board[i][1][1] and self.board[i][1][1] == self.board[i][0][2] and self.board[i][0][2] != 0:
                return self.board[i][2][0]
            if self.board[0][i][0] == self.board[1][i][1] and self.board[0][i][0] == self.board[2][i][2] and self.board[2][i][2] != 0:
                return self.board[0][i][0]
            if self.board[2][i][0] == self.board[1][i][1] and self.board[1][i][1] == self.board[0][i][2] and self.board[0][i][2] != 0:
                return self.board[2][i][0]
            if self.board[0][0][i] == self.board[1][1][i] and self.board[0][0][i] == self.board[2][2][i] and self.board[2][2][i] != 0:
                return self.board[0][0][i]
            if self.board[2][0][i] == self.board[1][1][i] and self.board[1][1][i] == self.board[0][2][i] and self.board[0][2][i] != 0:
                return self.board[2][0][i]
        if self.board[0][0][0] == self.board[1][1][1] and self.board[1][1][1] == self.board[2][2][2] and self.board[2][2][2] != 0:
            return self.board[0][0][0]
        if self.board[0][2][2] == self.board[1][1][1] and self.board[1][1][1] == self.board[2][0][2] and self.board[2][0][2] != 0:
            return self.board[0][2][2]
        if self.board[2][2][0] == self.board[1][1][1] and self.board[1][1][1] == self.board[0][0][2] and self.board[2][2][0] != 0:
            return self.board[2][2][0]
        return 0

    def findPutTokensLoc(self, coord):
        i = coord[0]
        j = coord[1]
        k = 0

        for l in range(0,3): 
            if self.board[i][j][l] == 0 :
                k = l
                break
        return (i,j,k)

    def validPut(self, coord, first = False) :
        i = coord[0]
        j = coord[1]

        if i < 0 or i > 2 or j < 0 or j > 2:
            return False

        if first and (i,j) == (1,1):
            return False
            
        for k in range(0,3) :
            if self.board[i][j][k] == 0 :
                return True
        return False

    def clear(self):
        if self.isVisual :
            self.base.visible = False
            for obj in self.poles:
                obj[0].visible = False
                obj[1].visible = False
            for objs in self.tmpTokens:
                for obj in objs:
                    obj.visible = False
            if self.hasButton :
                for obj in self.button:
                    obj.visible = False
