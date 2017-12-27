import piece
class Board:
    def __init__(self):
        self.board = {}

        self.letters = 'abcdefgh'
        self.numbers = '12345678'

        self.validsquares = []
        self.squares = {True : set(), False : set()}
        self.opensquares = set()

        #create board
        for letter in self.letters:
            for num in range(1, 9):
                #creates [letter][number] ID system
                key = '{0}{1}'.format(letter, num)
                #0 = unoccupied square, 1 = occupied by team 1, 2 = occupied by team 2, - = unoccupiable
                val = '0'
                if (letter in 'aceg' and num % 2 == 0) or (letter in 'bdfh' and num % 2 == 1):
                    val = '-'
                elif (num in [1,3] and self.letters.index(letter) % 2 == 0) or (num == 2 and self.letters.index(letter) % 2 == 1):
                    val = piece.Piece(True, key)
                elif (num in [6,8] and self.letters.index(letter) % 2 == 1) or (num == 7 and self.letters.index(letter)  % 2 == 0):
                    val = piece.Piece(False, key)
                self.board[key] = val

        #define validsquares
        for key in self.board.keys():
            if self.board[key] != '-':
                self.validsquares.append(key)

        #populates initial occupied and unoccupied square sets
        self.updateboard()

    #updates occupied and unoccupied squre sets
    def updateboard(self):
        #must reset each set before updating
        self.squares[True] = set()
        self.squares[False] = set()
        self.opensquares = set()
        for square in self.validsquares:
            if self.board[square] == '-':
                pass
            elif self.board[square] == '0':
                self.opensquares.add(square)
            elif self.board[square].team == True:
                self.squares[True].add(square)
            elif self.board[square].team == False:
                self.squares[False].add(square)


    def display(self, team):
        if team == True:
            print('  ___________________')
            print(' |                   |')
            #print nums backwards to build board top down
            for num in '87654321':
                print(num, end = '|  ')
                for letter in self.letters:
                    key = '{0}{1}'.format(letter, num)
                    if self.board[key] == '-' or self.board[key] == '0':
                        print(self.board[key], end = ' ')
                    elif self.board[key].team == True:
                        print('1', end = ' ')
                    elif self.board[key].team == False:
                        print('2', end = ' ')
                print(' |')
            print(' |___________________|')
            print('    a b c d e f g h')

        elif team == False:
            print('  ___________________')
            print(' |                   |')
            #print nums backwards to build board top down
            for num in self.numbers:
                print(num, end = '|  ')
                for letter in 'hgfedcba':
                    key = '{0}{1}'.format(letter, num)
                    if self.board[key] == '-' or self.board[key] == '0':
                        print(self.board[key], end = ' ')
                    elif self.board[key].team == True:
                        print('1', end = ' ')
                    elif self.board[key].team == False:
                        print('2', end = ' ')
                print(' |')
            print(' |___________________|')
            print('    h g f e d c b a')

    #hasmove - takes bool for team, returns bool for if that team has a move
    def hasmove(self, team):
        if self.squares[team] == set():
            return False
        for piece in [squares for squares in self.validsquares if squares in self.squares[team]]:
            if not self.possiblemoves(piece) == {}:
                return True
        return False

    #make possiblemoves - takes position id, returns set of possible moves for that piece
    def possiblemoves(self, id):
        moves = {}

        #move from team 1 to team 2 side
        if self.board[id].team == True or self.board[id].king == True:
            for i in [-1, 1]:
                square = self.getrelsquare(id, i, 1)
                if square:
                    if square in self.opensquares:
                        moves[square] = False
                    elif square in self.squares[not self.board[id].team]:
                        square2 = self.getrelsquare(id, 2 * i, 2)
                        if square2:
                            if square2 in self.opensquares:
                                moves[square2] = True

        #move from team 2 to team 1 side
        if self.board[id].team == False or self.board[id].king == True:
            for i in [-1, 1]:
                square = self.getrelsquare(id, i, -1)
                if square:
                    if square in self.opensquares:
                        moves[square] = False
                    elif square in self.squares[not self.board[id].team]:
                        square2 = self.getrelsquare(id, 2 * i, -2)
                        if square2:
                            if square2 in self.opensquares:
                                moves[square2] = True

        return moves

    #take a piece, a letter index change, a number index change, return a touple of (square, piece)
    def getrelsquare(self, piece, ac, nc):
        if self.letters.index(piece[0]) + ac in range(8) and self.numbers.index(piece[1]) + nc in range(8):
            sq = '{0}{1}'
            newl = self.letters[self.letters.index(piece[0]) + ac]
            newn = self.numbers[self.numbers.index(piece[1]) + nc]
            return sq.format(newl, newn)

    #make move - takes in piece position and new piece position
    def move(self, start, end):
        #regular move
        if abs(int(end[1]) - int(start[1])) == 1:
            self.board[end] = self.board[start]
            self.board[start] = '0'
            self.board[end].move(end)
        #code for capture
        elif abs(int(end[1]) - int(start[1])) == 2:
            self.board[end] = self.board[start]
            self.board[start] = '0'
            self.board[end].move(end)
            #get rid of the piece in middle
            newl = ''
            newn = ''
            if self.letters.index(start[0]) < self.letters.index(end[0]): newl = 1
            else: newl = -1
            if self.numbers.index(start[1]) < self.numbers.index(end[1]): newn = 1
            else: newn = -1
            self.board[self.getrelsquare(start, newl, newn)] = '0'

        self.checkking(end)
        self.updateboard()
        #TODO code for multicapture
        #make the possible moves into dictionaries with a True False on whether its a capture move

        #check per team if they are on final square
    def checkking(self, id):
        if self.board[id].team == True and id[1] == '8':
            self.board[id].kingme()
        elif self.board[id].team == False and id[1] == '1':
            self.board[id].kingme()


if __name__ == '__main__':
    board = Board()
    #board.display(1)
    #board.display(0)
