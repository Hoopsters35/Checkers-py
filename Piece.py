from Board import Board
class Piece:
    def __init__(self, team, position):
        self.team = team
        self.position = position
        self.king = False
        self.pos_moves = set()

    def move (self, newpos):
        if newpos in self.pos_moves:
            self.position - newpos
        else:
            return False

    def get_pos_moves(self):
        return self.pos_moves

    def set_pos_moves(self, moves):
        self.pos_moves = set()
        for move in moves:
            self.pos_moves.add(move)

    def get_team (self):
        return self.team

    def get_king(self):
        return self.king

    def king(self):
        self.king = True

if __name__ == '__main__':
    board = Board()
    board.display1()
    board.display2()
