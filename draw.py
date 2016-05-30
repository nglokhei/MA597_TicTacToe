from visual import *

from convert import *

r = 50
s = 20
u = 2*r+s

base = box(pos = vector(0,0,0), length = 400, height = 400, width = 25,
           material = materials.wood, color = color.orange, visible = False)
class cross:
    def __init__(self, pos, visible = True):
        self.visi = visible
        self.position = pos
        self.box1 = box(pos = self.position,
                        length = 20,
                        height = 111,
                        width = 111,
                        axis = vector(-1,-1,0),
                        material = materials.blazed,
                        color = (1,0.7,0.2),
                        opacity = 1)
        self.box2 = box(pos = self.position,
                        length = 20,
                        height = 111,
                        width = 111,
                        axis = vector(1,-1,0),
                        material = materials.blazed,
                        color = (1,0.7,0.2),
                        opacity = 1)

    def pos(self, pos):
        self.position = pos
        self.box1.pos = self.position
        self.box2.pos = self.position

    def visible(self, v):
        self.visi = v
        self.box1.visible = v
        self.box2.visible = v

class ball:
    def __init__(self, pos, visible = True):
        self.visi = visible
        self.position = pos
        self.sph = sphere(pos = self.position,
                          radius = r,
                          material = materials.shiny)

    def pos(self, pos):
        self.position = pos
        self.sph.pos = self.position

    def visible(self, v):
        self.visi = v
        self.sph.visible = v


def drawBoard(hPoleNum = []):
    retval = []
    base = box(pos = vector(0,-100,0), length = 400, height = 25, width = 400,
           material = materials.wood, color = color.orange)

    hPole = []
    for poleNum in hPoleNum:
        hPole.append(poleCoord(poleNum))
                   
    for i in range(0,3) :
        for j in range(0,3) :
            if (i,j) in hPole :
                s = sphere(pos = vector(-u+u*i,220,-u+u*j), radius = 15.3,
                           material = materials.wood, color = color.yellow)
                c = cylinder(pos = vector(-u+u*i,-100,-u+u*j), axis = (0,320,0),
                             radius = 15, material = materials.wood,
                             color = color.yellow)
                retval.append((s, c, (i,j)))
            else :
                s = sphere(pos = vector(-u+u*i,220,-u+u*j), radius = 15.3, material = materials.wood, 
                           color = (1,0.9,0.8))
                c = cylinder(pos = vector(-u+u*i,-100, -u+u*j), axis = (0,320), radius = 15, 
                             material = materials.wood, color = (1,0.9,0.8), opacity = 1)
                retval.append((s, c, (i, j)))
    return (retval, base)

def drawButton(s):
    retval1 = box(pos = vector(0, -100, 300), length = 300, height = 25, width = 100,
                  color = color.red)
    retval2 = text(pos = vector(0,-110, 300), text = s, align = 'center',
                   color = color.black, height = 45, width = 300, axis = vector(1,0,0),
                   normal = vector(0,0,1), depth = 10)
    retval2.rotate(angle = -pi/2, axis = vector(1,0,0), origin = vector(0,-87,300))
    return [retval1, retval2]

def putTokensAnim(board1, pts,tokens = []):
    i = pts[0]
    j = pts[1]
    k = pts[2]
    z = 220 + r
    end = -2*r+2*r*k + 3*r + base.width/2 - 100
    if board1.board[i][j][k] == 2:
        tokens.append(ball(vector(-u+u*i,z,-u+u*j)))
    else:
        tokens.append(cross(vector(-u+u*i,z,-u+u*j)))
        
    while not z == end:
        z = z - 0.5
        rate(200)
        tokens[-1].pos(vector(-u+u*i,z,-u+u*j))

    sleep(0.1)
    return tokens

def drawTmpTokens():
    box1 = box(pos = vector(-300, 0, 290),
               length = 20,
               height = 111,
               width = 111,
               axis = vector(-1,-1,0),
               material = materials.blazed,
               color = (1,0.7,0.2),
               opacity = 1,
               visible = False)
    box2 = box(pos = vector(-300, 0, 290),
               length = 20,
               height = 111,
               width = 111,
               axis = vector(1,-1,0),
               material = materials.blazed,
               color = (1,0.7,0.2),
               opacity = 1,
               visible = False)
    sph = sphere(pos = vector(300 , 0, 290),
                 radius = r,
                 material = materials.shiny,
                 visible = False)
    return [[box1, box2],[sph]]
    
