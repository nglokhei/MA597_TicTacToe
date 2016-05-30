from visual import *
import numpy as np

from playerInput import *
from computerInput import *
from gameClass import *
from boardClass import *
from draw import *

def setScene():
    scene.select()
    scene.forward = vector(0,-1,-1)
    scene.range = 600
    scene.background = (0,0.5,0.5)
    scene.userspin = True
    scene.userzoom = True

def showMsg(msg, l, time = 2):
    if len(msg) > 0:
        l.visible = True
        l.text = msg
        sleep(time)
        l.visible = False

def gameloop(game, board, playerx, playero, l):
    while game.win == 0:
        if not playerx and not playero :
            ins = 'Player ' + playerName(game.playerTurn) + ' plays'
            showMsg(ins, l)
            
        if (playerx and game.playerTurn == 1) or (playero and game.playerTurn == 2):
            for obj in board.tmpTokens[game.playerTurn - 1]:
                obj.visible = True
            (i,j) = playerInput(game, board)
        else:
            (i,j) = computerInput(board, game.playerTurn, (game.steps == []))

        pickedCoord = board.findPutTokensLoc((i,j)) 
        board.putTokens(pickedCoord, game, True)
        game.win = board.checkWin()
        game.changePlayer()
        
def threeDimTicTacToe(playerx, playero):

    #game initialize
    #setInstructionWindow()
    setScene()
    game = Game()
    l = label(pos=vector(0,0.25,0), text = "", visible = False)
    if not playerx and not playero :
        board = Board()
    else :
        s = "Return"
        board = Board(s)
        ins = "When it is your turn, drag your token and point your mouse to\nthe pole you want to drop the token into.\nYou can regret your previous move by clicking the return button."
        showMsg(ins, l, 6)
        ins = "And the first move of player X must not be the middle pole."
        showMsg(ins, l, 5)
        
        if playerx and not playero:
            ins = "Now I'm player O and you're player X."
            showMsg(ins, l)
        elif playero and not playerx:
            ins = "Now I'm player X and you're player O."
            showMsg(ins, l)
        
    gameloop(game, board, playerx, playero, l)


    ins = '                     Player ' + playerName(game.win) + ' wins !\nYou will be redirected to the main menu.'
    showMsg(ins, l, 3)
    board.clear()
    game.clear()
    l.visible = False
    scene.range = 50
    scene.forward = vector(0,0,-1)
    scene.userspin = False
    scene.userzoom = False
