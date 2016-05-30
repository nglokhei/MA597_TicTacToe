from visual import *
import numpy as np

coord = (-1,-1)

def win(board):
    for i in range(0,3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][1] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[1][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[0][2] != 0:
        return board[2][0]
    return 0

def putTokenAnim(token, grid):
    p = 3.141592
    t = 0
    s = 0.01

    f2 = token[0].axis[1]
    f = grid.axis[1]
    while t < 1:
        rate(100)
        grid.rotate(angle = p *0.02* t, axis = (1,0,0))
        for thing in token:
            thing.rotate(angle = p *0.02* t, axis = (1,0,0))
        if t > 0.7:
            for thing in token:
                thing.visible = True
        t = t + s


def playerName(playerNum):
    if playerNum == 1:
        return 'X'
    return 'O'

def grab(evt, grid):
    obj = evt.pick
    scene.bind('mouseup', drop, grid, obj)

def drop(evt, grid, obj):
    global coord
    scene.unbind('mouseup', drop)
    for i in range(0,3):
        for j in range(0,3):
            if obj == grid[i][j] and obj != None:
                coord = (i,j)
    
def score(board, player, depth) :
    if win(board) == player :
        return 30 - depth
    elif win(board) == player % 2 + 1 :
        return depth - 30
    else :
        return 0

def max_idx(arr):
    maxval = arr[0]
    maxidx = 0
    for i in range(1, len(arr)):
        if arr[i] > maxval:
            maxval = arr[i]
            maxidx = i
    return maxidx

def min_idx(arr):
    minval = arr[0]
    minidx = 0
    for i in range(1, len(arr)):
        if arr[i] < minval:
            minval = arr[i]
            minidx = i
    return minidx

def minmax(board, player, playerTurn, depth):
    if win(board) > 0 or depth == 10:
        return (-1,-1), score(board, player, depth)
    
    depth += 1
    scores = [] # an array of scores
    moves = []  # an array of moves

    # get available moves and its score
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == 0:
                moves.append((i,j))
                board[i][j] = playerTurn
                (p,q), scoreOfMove = minmax(board, player, playerTurn % 2 + 1, depth)
                scores.append(scoreOfMove)
                board[i][j] = 0

    if playerTurn == player:
        max_score_idx = max_idx(scores)
        return moves[max_score_idx], scores[max_score_idx]
    else :
        min_score_idx = min_idx(scores)
        return moves[min_score_idx], scores[min_score_idx]
    
def twoDimTicTacToe(playerx, playero):
    scene.userspin = False
    scene.userzoom = False
    scene.range = 50
        
    # vertical bound
    v1 = box(pos = vector(10,-9,0), length = 2, height = 61, width = 2)
    v2 = box(pos = vector(-10,-9,0), length = 2, height = 61, width = 2)
    ##
    ### horizontal bound
    h1 = box(pos = vector(0,1,0), length = 61, height = 2, width = 2)
    h2 = box(pos = vector(0,-19,0), length = 61, height = 2, width = 2)


    instruction = text(pos = vector(0,30,0), text = 'Player X, it\'s your turn.',align = 'center',height = 4,
                       width = 70, depth = -0.3, color = color.white, visible = True)
    board = np.zeros((3,3))
    player = 1
    posX = [-20, 0, 20]
    posY = [-29, -9, 11]
    turn = 0
    tokens = []
    global coord
    coord = (-1,-1)
    # grid
    grid=[None]*3
    for i in range(0,3) :
        tmp = [None]*3
        for j in range(0,3) :
            x = posX[i]
            y = posY[j]
            tmp[j] = box(pos = vector(x, y, 0), axis = (0, 1, 0), height = 17, width = 2, length = 17, color = color.yellow, material = materials.wood)
        grid[i] = tmp

    scene.bind('mousedown',grab, grid)
    while win(board) == 0 and turn < 9:
        turn = turn + 1
        
        # display message
        s = 'Player ' + playerName(player) + ',  it\'s your turn.'
        if (playerx and player == 1) or (playero and player == 2) :
            s = s + '\nClick on the grid.'
        instruction.text = s

        # player input
        if (playerx and player == 1) or (playero and player == 2) :
            while True:
                rate(30)
                if coord != (-1,-1):
                    i = coord[0]
                    j = coord[1]
                    if board[i][j] == 0:
                        break
        # computer input
        else :
            if turn == 1:
                (i,j) = (0,0)
            else :
                (i,j), sc = minmax(board, player, player, turn)

        # put token
        board[i][j] = player
        x = posX[i]
        y = posY[j]
        if player == 2:
            t = [ring(pos=(x, y, 0), axis=(0,0,1), radius=7, thickness=1.5, color = color.black, visible = False)]
        else :
            t = [box(pos = vector(x, y, 0), axis = (1,1,0), height = 20, width = 3, length = 2, color = color.black, visible = False),
                 box(pos = vector(x, y, 0), axis = (-1,1,0), height = 20, width = 3, length = 2, color = color.black, visible = False)]
        putTokenAnim(t, grid[i][j])
        tokens.append(t)
        player = player % 2 + 1

    if win(board):
        s = 'Player ' + playerName(player % 2 + 1) + ' wins\nYou will be redirected to the main menu.'
    else :
        s = '      Draw !\nYou will be redirected to the main menu.'
    instruction.text = s
    sleep(3)
    scene.unbind('mousedown',grab)
    v1.visible = False
    v2.visible = False
    h1.visible = False
    h2.visible = False
    instruction.visible = False
    for objs in grid:
        for obj in objs:
            obj.visible = False
    for objs in tokens:
        for obj in objs:
            obj.visible = False
