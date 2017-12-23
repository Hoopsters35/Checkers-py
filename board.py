import piece
class Board:
    def __init__(self):
        self.board = {}
        self.validsquares = []
        self.squares = {True : set(), False = set()}
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

    #hasmove - takes bool for team, returns bool for if that team has a move
    def hasmove(self, team):
        if team:
            if self.squares[True] == set():
                return False
            #check team1 possible moves
            for piece in [squares for squares in self.validsquares if squares in self.squares[True]]:
                if not self.possiblemoves(piece) == set():
                    return True

        elif not team:
            if self.squares[False] == set():
                return False
            #check team2 possible moves
            for piece in [squares for squares in self.validsquares if squares in self.squares[False]]:
                if not self.possiblemoves(piece) == set():
                    return True
        return False

    #make possiblemoves - takes position id, returns set of possible moves for that piece
    def possiblemoves(self, id):
        moves = set()
        letters = 'abcdefgh'
        numbers = '12345678'
        sq = '{0}{1}'
       #TODO currently king will not work, as checking for other team is hard coded
        #move from team 1 to team 2 side
        if self.board[id].team == True or self.board[id].king == True:
            if letters.index(id[0]) + 1 <= 7 and numbers.index(id[1]) + 1 <= 7:
                newl = letters[letters.index(id[0]) + 1]
                newn = numbers[numbers.index(id[1]) + 1]
                if sq.format(newl, newn) in self.opensquares:
                    moves.add(sq.format(newl, newn))
                elif sq.format(newl, newn) in self.squares[False]:
                    if letters.index(id[0]) + 2 <= 7 and numbers.index(id[1]) + 2 <= 7:
                        newl = letters[letters.index(id[0]) + 2]
                        newn = numbers[numbers.index(id[1]) + 2]
                        if sq.format(newl, newn) in self.opensquares:
                            moves.add(sq.format(newl, newn))

            if letters.index(id[0]) - 1 >= 0 and numbers.index(id[1]) + 1 <= 7:
                newl = letters[letters.index(id[0]) - 1]
                newn = numbers[numbers.index(id[1]) + 1]
                if sq.format(newl, newn) in self.opensquares:
                    moves.add(sq.format(newl, newn))
                elif sq.format(newl, newn) in self.squares[False]:
                    if letters.index(id[0]) - 2 >= 0 and numbers.index(id[1]) + 2 <= 7:
                        newl = letters[letters.index(id[0]) - 2]
                        newn = numbers[numbers.index(id[1]) + 2]
                        if sq.format(newl, newn) in self.opensquares:
                            moves.add(sq.format(newl, newn))

        #move from team 2 to team 1 side
        if self.board[id].team == False or self.board[id].king == True:
            if numbers.index(id[1]) - 1 >= 0 and letters.index(id[0]) + 1 <= 7:
                newl = letters[letters.index(id[0]) + 1]
                newn = numbers[numbers.index(id[1]) - 1]
                if sq.format(newl, newn) in self.opensquares:
                    moves.add(sq.format(newl, newn))
                elif sq.format(newl, newn) in self.squares[True]:
                    if numbers.index(id[1]) - 2 >= 0 and letters.index(id[0]) + 2 <= 7:
                        newl = letters[letters.index(id[0]) + 2]
                        newn = numbers[numbers.index(id[1]) - 2]
                        if sq.format(newl, newn) in self.opensquares:
                            moves.add(sq.format(newl, newn))

            if letters.index(id[0]) - 1 >= 0 and numbers.index(id[1]) - 1 >= 0:
                newl = letters[letters.index(id[0]) - 1]
                newn = numbers[numbers.index(id[1]) - 1]
                if sq.format(newl, newn) in self.opensquares:
                    moves.add(sq.format(newl, newn))
                elif sq.format(newl, newn) in self.squares[True]:
                    if letters.index(id[0]) - 2 >= 0 and numbers.index(id[1]) - 2 >= 0:
                        newl = letters[letters.index(id[0]) - 2]
                        newn = numbers[numbers.index(id[1]) - 2]
                        if sq.format(newl, newn) in self.opensquares:
                            moves.add(sq.format(newl, newn))

        return moves

    #make move - takes in piece position and new piece position
    def move(self, start, end):
        letters = 'abcdefgh'
        numbers = '12345678'
        #regular move
        if abs(int(end[1]) - int(start[1])) == 1:
            tmp = self.board[end]
            self.board[end] = self.board[start]
            self.board[start] = '0'
            self.board[end].move(end)
        #code for capture
        elif abs(int(end[1]) - int(start[1])) == 2:
            tmp = self.board[end]
            self.board[end] = self.board[start]
            self.board[start] = '0'
            self.board[end].move(end)
            #get rid of the piece in middle
            sq = '{0}{1}'
            newl = ''
            newn = ''
            if letters.index(start[0]) < letters.index(end[0]):
                newl = letters[letters.index(start[0]):letters.index(end[0])][1]
            else:
                newl = letters[letters.index(end[0]):letters.index(start[0])][1]
            if numbers.index(start[1]) < numbers.index(end[1]):
                newn = numbers[numbers.index(start[1]):numbers.index(end[1])][1]
            else:
                newn = numbers[numbers.index(end[1]):numbers.index(start[1])][1]
            self.board[sq.format(newl, newn)] = '0'

        self.checkking(end)
        self.updateboard()
        #TODO code for multicapture

        #check per team if they are on final square
    def checkking(self, id):
        if id in self.squares[True] and id[1] == '8':
            self.board[id].king()
        elif id in self.squares[False] and id[1] == '1':
            self.board[id].king()


if __name__ == '__main__':
    board = Board()
    board.display1()
    board.display2()
