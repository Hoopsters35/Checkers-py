import Piece
class Board:
    def __init__(self):
        self.board = {}
        self.validsquares = set()
        self.squares1 = set()
        self.squares2 = set()

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
                    val = '1'
                elif (num in [6,8] and letters.index(letter) % 2 == 1) or (num == 7 and letters.index(letter)  % 2 == 0):
                    val = '2'
                self.board[key] = val

        #define validsquares
        for key in self.board.keys():
            if self.board[key] != '-':
                self.validsquares.add(key)

        #populate squares1 and squares2
        for square in self.board.keys():
            if self.board[square] ==  '1':
                self.squares1.add(square)
            elif self.board[square] == '2':
                self.squares2.add(square)

    def display1(self):
        print('  ___________________')
        print(' |                   |')
        #print nums backwards to build board top down
        for num in '87654321':
            print(num, end = '|  ')
            for letter in 'abcdefgh':
                key = '{0}{1}'.format(letter, num)
                print(self.board[key], end = ' ')
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
                print(self.board[key], end = ' ')
            print(' |')
        print(' |___________________|')
        print('    h g f e d c b a')

if __name__ == '__main__':
    board = Board()
    board.display1()
    board.display2()
    print(board.squares1)
    print(board.squares2)
