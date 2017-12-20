#from Piece.py import Piece
class Board:
    def __init__(self):
        self.board = {}
        letters = 'abcdefgh'
        for letter in letters:
            for num in range(1, 9):
                #creates [letter][number] ID system
                key = '{0}{1}'.format(letter, num)
                #0 = unoccupied square, 1 = occupied by team 1, 2 = occupied by team 2, - = unoccupiable
                val = 0
                if (letter in 'aceg' and num % 2 == 0) or (letter in 'bdfh' and num % 2 == 1):
                    val = '-'
                elif (num in [1,3] and letters.index(letter) % 2 == 0) or (num == 2 and letters.index(letter)  == 1):
                    val = 1
                elif (num in [6,8] and letters.index(letter) % 2 == 1) or (num == 7 and letters.index(letter)  % 2 == 0):
                    val = 2
                self.board[key] = val

    def display(self):
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

board = Board()
board.display()
