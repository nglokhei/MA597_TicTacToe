from visual import *
import numpy as np
import random


from draw import *
from convert import *
from boardClass import *
from gameClass import *

def warnMsg(defender):
    return 'Player ' + playerName(defender) + ' must put his token into the highlighted pole(s).'
       
def demGame(steps, msg, hpole, game, board, poles):

    for i in range(0,len(hpole)):
        game.changePlayer()
        # display messages
        if i < len(msg) and len(msg[i]) > 0 :
            l = label(pos=vector(0,0.25,0), text = msg[i])
            if len(hpole[i]) > 0 :
                for highlightedPole in hpole[i]:
                    poles[highlightedPole-1][0].color = color.yellow
                    poles[highlightedPole-1][1].color = color.yellow
            sleep(3)
            l.visible = False
            if len(hpole[i]) > 0 :
                for highlightedPole in hpole[i]:
                    poles[highlightedPole-1][0].color = (1,0.9,0.8)
                    poles[highlightedPole-1][1].color = (1,0.9,0.8)

        # put tokens
        if i < len(steps):
            coord = poleCoord(steps[i])
            coord = board.findPutTokensLoc(coord)
            board.putTokens(coord, game, True)
        
    l.visible = True
    l.text = 'But it is impossible to put 2 tokens at the same time.\nSo player X wins the game.'
    sleep(5)
    l.visible = False


def case1(board, game, poles):
    steps = [1,8,2,3,7,4,6,5,5,8]
    msg = ['Case 1 : Player O put his token into a corner.',
           'Player X is free to put his token.',
           warnMsg(0),
           warnMsg(1),
           warnMsg(0),
           warnMsg(1),
           warnMsg(0),
           'Player X is free to put his token.',
           warnMsg(0),
           'Player X is free to put his token.',
           warnMsg(0)]
    hpole = [[],[],[2],[3],[7],[4],[6],[],[5],[],[2,8]]
    demGame(steps, msg, hpole, game, board, poles)

def case2(board, game, poles):
    steps = [2,1,9,7]
    msg = ['Case 2 : Player O put his token into an edge.',
           'Player X is free to put his token.',
           warnMsg(0),
           'Player X is free to put his token.',
           warnMsg(0)]
    hpole = [[],[],[9],[],[3,4]]
    demGame(steps, msg, hpole, game, board, poles)

def case3(board, game, poles):
    steps = [5,1,9,2]
    msg = ['Case 3 : Player O put his token into the middle pole.',
           'Player X is free to put his token.',
           warnMsg(0),
           'Player X is free to put his token.',
           warnMsg(0)]
    hpole = [[],[],[9],[],[3,8]]
    demGame(steps, msg, hpole, game, board, poles)

def demThm():
    scene.range = 500
    scene.forward = vector(1,-1.5,-1)
    scene.userspin = True
    scene.userzoom = True
    board = Board()
    game = Game()
    poles, base = drawBoard()
    l = label(pos=vector(0,0.25,0), text ='Suppose player X put his first token into the middle pole.')
    sleep(2)
    l.visible = False
    board.board[1][1][0] = 1
    game.tokens = putTokensAnim(board, (1,1,0))
    l.text = 'Then player O can put his token into a corner,\nan edge or the middle pole.'
    l.visible = True
    sleep(3)
    l.visible = False

    # case 1
    case1(board, game, poles)

    # clean the board
    while len(game.steps) > 1:
        (i,j,k) = game.steps[-1]
        (p,q,r) = game.steps[-2]
        board.board[i][j][k] = 0
        board.board[p][q][r] = 0
                
        game.tokens[-1].visible(False)
        del game.tokens[-1]
        game.tokens[-1].visible(False)
        del game.tokens[-1]

        del game.steps[-1]
        del game.steps[-1]
    game.changePlayer()

    # case 2
    case2(board, game, poles)

    # clean the board
    while len(game.steps) > 1:
        (i,j,k) = game.steps[-1]
        (p,q,r) = game.steps[-2]
        board.board[i][j][k] = 0
        board.board[p][q][r] = 0
                
        game.tokens[-1].visible(False)
        del game.tokens[-1]
        game.tokens[-1].visible(False)
        del game.tokens[-1]

        del game.steps[-1]
        del game.steps[-1]
    game.changePlayer()

    case3(board, game, poles)
    l.visible = True
    l.text = 'All cases give player X winning the game Q.E.D.'
    sleep(3)
    l.visible = False
    game.clear()
    board.clear()
    scene.range = 50
    scene.forward = (0,0,-1)
    for pole in poles:
        pole[0].visible = False
        pole[1].visible = False
    base.visible = False
    
    
