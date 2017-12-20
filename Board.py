#from Piece.py import Piece
class Board:
    def __init__(self):
        self.board = {}
        for letter in ['a','b','c','d','e','f','g','h']:
            for num in range(1, 9):
                key = '{0}{1}'.format(letter, num)
                val = 0
                if (letter in ['a', 'c', 'e', 'g'] and num % 2 == 0) or (letter in ['b', 'd', 'f', 'h'] and num % 2 == 1):
                    val = '-'
                elif (letter in ['a','c'] and num % 2 == 1) or (letter == 'b' and num % 2 == 0):
                    val = 1
                elif (letter in ['f','h'] and num % 2 == 0) or (letter == 'g' and num % 2 == 1):
                    val = 2
                self.board[key] = val

    def display(self):
        print('  ___________________')
        print(' |                   |')
        for letter in ['h','g','f','e','d','c','b','a']:
            print(letter, end = '|  ')
            for num in range(1, 9):
                key = '{0}{1}'.format(letter, num)
                print(self.board[key], end = ' ')
            print(' |')
        print(' |___________________|')
        print('    1 2 3 4 5 6 7 8')

board = Board()
board.display()

