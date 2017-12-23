class Piece:
    def __init__(self, team, position):
        self.team = team
        self.position = position
        self.king = False

    def move (self, newpos):
        if newpos in self.pos_moves:
            self.position - newpos
        else:
            return False

    def king(self):
        self.king = True

