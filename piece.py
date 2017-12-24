class Piece:
    def __init__(self, team, position):
        self.team = team
        self.position = position
        self.king = False

    def move (self, newpos):
        self.position = newpos

    def kingme(self):
        self.king = True

