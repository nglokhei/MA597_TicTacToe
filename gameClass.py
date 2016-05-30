
class Game:
    def __init__(self):
        self.playerTurn = 1
        self.steps = []
        self.tokens = []
        self.win = 0

    def changePlayer(self):
        self.playerTurn = self.playerTurn % 2 + 1

    def clear(self):
        for obj in self.tokens:
            obj.visible(False)
        
    
