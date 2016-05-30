from visual import *

from draw import *
from gameClass import *

drag_pos = None # no object picked yet
coord = (-1,-1)
retSteps = False

def grab(evt, token, ret, poles, board, game):
    global drag_pos
    global retSteps
    #scene.unbind('mousedown', grab)
    if evt.pick in token:
        drag_pos = evt.pickpos
        scene.bind('mousemove', move, token)
        scene.bind('mouseup', drop, token, poles, board, game)

    if evt.pick in ret:
        retSteps = True

def move(evt, objs):
    global drag_pos
    # project onto xy plane, even if scene rotated:
    new_pos = scene.mouse.project(normal=(0,0,1))
    if new_pos != drag_pos: # if mouse has moved
        # offset for where the ball was touched:
        for obj in objs:
            obj.pos += new_pos - drag_pos
        drag_pos = new_pos # update drag position

def drop(evt, token, poles, board, game):
    global coord
    scene.unbind('mousemove', move)
    scene.unbind('mouseup', drop)
    for obj in token:
        obj.visible = False
        obj.pos += vector(1000,1000,1000)
    sleep(0.000000000000000000000000000000000000000000000001)
    pick = scene.mouse.pick
    coord = coordinate(pick, poles)
    if coord == (-1,-1):
        for obj in token:
            obj.pos += vector(-1000, -1000, -1000)
            obj.visible = True
        
def putback(player):
    if player == 2:
        return vector(300 , 0, 290)
    else:
        return vector(-300, 0, 290)
    
def coordinate(pick, poles):
    for pole in poles:
        for obj in pole :
            if pick == obj :
                return pole[2]
    return (-1, -1)
            
# run once for each turn
def playerInput(game, board):

    global coord
    global retSteps
    coord = (-1,-1)
    scene.bind('mousedown',grab, board.tmpTokens[game.playerTurn - 1], board.button, board.poles, board.board, game)
    while coord == (-1, -1) :
        rate (10)
        
        # reverse
        if retSteps:
            if len(game.steps) < 2:
                l = label(pos=(0,0.25,0), text='Cannot return')
                sleep(1)
                l.visible = False
            else:
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

            retSteps = False

        if coord != (-1,-1):
            if board.validPut(coord, (game.steps == [])):
                for obj in board.tmpTokens[game.playerTurn - 1]:
                    obj.pos = putback(game.playerTurn)
                break
            else :
                for obj in board.tmpTokens[game.playerTurn - 1]:
                    obj.pos += vector(-1000, -1000, -1000)
                    obj.visible = True

                if game.steps == [] and coord == (1,1):
                    msg = 'Oops ! You cannot put it here for your first move.'
                    l = label(pos=(0,0.25,0), text = msg)
                    sleep(2)
                    l.visible = False
                    
                elif coord != (-1,-1):
                    l = label(pos=(0,0.25,0), text='Column is full')
                    sleep(1)
                    l.visible = False
                    
                coord = (-1, -1)
                
    scene.unbind('mousedown', grab)            
    return coord



        

    
