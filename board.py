import piece
class Board:
    def __init__(self):
        self.board = {}
        self.validsquares = []
        self.squares1 = set()
        self.squares2 = set()
        self.opensquares = set()

        #create board
        letters = 'abcdefgh'
        for letter in letters:
            for num in range(1, 9):
                #creates [letter][number] ID system
                key = '{0}{1}'.format(letter, num)
                #0 = unoccupied square, 1 = occupied by team 1, 2 = occupied by team 2, - = unoccupiable
                val = '0'
                if (letter in 'aceg' and num % 2 == 0) or (letter in 'bdfh' and num % 2 == 1):
                    val = '-'
                elif (num in [1,3] and letters.index(letter) % 2 == 0) or (num == 2 and letters.index(letter) % 2 == 1):
                    val = piece.Piece(True, key)
                elif (num in [6,8] and letters.index(letter) % 2 == 1) or (num == 7 and letters.index(letter)  % 2 == 0):
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
        self.squares1 = set()
        self.squares2 = set()
        self.opensquares = set()
        for square in self.validsquares:
            if self.board[square] == '-':
                pass
            elif self.board[square] == '0':
                self.opensquares.add(square)
            elif self.board[square].team == True:
                self.squares1.add(square)
            elif self.board[square].team == False:
                self.squares2.add(square)


    def display1(self):
        print('  ___________________')
        print(' |                   |')
        #print nums backwards to build board top down
        for num in '87654321':
            print(num, end = '|  ')
            for letter in 'abcdefgh':
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

    def display2(self):
        print('  ___________________')
        print(' |                   |')
        #print nums backwards to build board top down
        for num in '12345678':
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

    #TODO make hasmove - takes bool for team, returns bool for if that team has a move

    #TODO make possiblemoves - takes position id, returns set of possible moves for that piece
    def possiblemoves(self, id):
        moves = set()
        letters = 'abcdefgh'
        numbers = '12345678'
        sq = '{0}{1}'

        if self.board[id].team == True or self.board[id].king == True:
            newl = letters[letters.index(id[0]) + 1]
            newn = numbers[numbers.index(id[1]) + 1]
            if sq.format(newl, newn) in self.opensquares:
                moves.add(sq.format(newl, newn))
            elif sq.format(newl, newn) in self.squares2:
                newl = letters[letters.index(id[0]) + 2]
                newn = numbers[numbers.index(id[1]) + 2]
                if sq.format(newl, newn) in self.opensquares:
                    moves.add(sq.format(newl, newn))

            if letters.index(id[0]) - 1 >= 0 and numbers.index(id[1]) + 1 <= 7:
                newl = letters[letters.index(id[0]) - 1]
                newn = numbers[numbers.index(id[1]) + 1]
                if sq.format(newl, newn) in self.opensquares:
                    moves.add(sq.format(newl, newn))
                elif sq.format(newl, newn) in self.squares2 and letters.index(id[0]) - 2 >= 0 and numbers.index(id[1]) + 2 <= 7:
                    newl = letters[letters.index(id[0]) - 2]
                    newn = numbers[numbers.index(id[1]) + 2]
                    if sq.format(newl, newn) in self.opensquares:
                        moves.add(sq.format(newl, newn))
        if self.board[id].team == False or self.board[id].king == True:
            if numbers.index(id[1]) - 1 >= 0 and letters.index(id[0]) + 1 <= 7:
                newl = letters[letters.index(id[0]) + 1]
                newn = numbers[numbers.index(id[1]) - 1]
                if sq.format(newl, newn) in self.opensquares:
                    moves.add(sq.format(newl, newn))
                elif sq.format(newl, newn) in self.squares2 and numbers.index(id[1]) - 2 >= 0 and letters.index(id[0]) + 2 <= 7:
                    newl = letters[letters.index(id[0]) + 2]
                    newn = numbers[numbers.index(id[1]) - 2]
                    if sq.format(newl, newn) in self.opensquares:
                        moves.add(sq.format(newl, newn))

            if letters.index(id[0]) - 1 >= 0 and numbers.index(id[1]) - 1 >= 0:
                newl = letters[letters.index(id[0]) - 1]
                newn = numbers[numbers.index(id[1]) - 1]
                if sq.format(newl, newn) in self.opensquares:
                    moves.add(sq.format(newl, newn))
                elif sq.format(newl, newn) in self.squares2 and letters.index(id[0]) - 2 >= 0 and numbers.index(id[1]) - 2 >= 0:
                    newl = letters[letters.index(id[0]) - 2]
                    newn = numbers[numbers.index(id[1]) - 2]
                    if sq.format(newl, newn) in self.opensquares:
                        moves.add(sq.format(newl, newn))

        return moves

    #TODO make move - takes in piece position and new piece position
if __name__ == '__main__':
    board = Board()
    board.display1()
    board.display2()
    print('a3', board.possiblemoves('a3'))
    print('c3', board.possiblemoves('c3'))
    print('b6', board.possiblemoves('b6'))
    print('h6', board.possiblemoves('h6'))
