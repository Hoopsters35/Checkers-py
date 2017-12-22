import board, re

board = board.Board()
t1 = True

moveregex = re.compile('^([a-h][1-8]) ([a-h][1-8])$')

while board.hasmove(t1):
    if t1:
        board.display1()
        print('Team 1 to move.')
        inp = input('Enter move [ie. a3 b4] ')
        while not (moveregex.match(inp) and moveregex.group(1) in board.squares1 and moveregex.group(2) in board.possiblemoves(moveregex.group(1))):
            print('Error with move, please use format:a3 b4')
            inp = input('Enter move: ')
        board.move(moveregex.group(1), moveregex.group(2))
        t1 = !t1
    else:
        board.display2()
        print('Team 2 to move.')
        inp = input('Enter move [ie. a3 b4] ')
        while not (moveregex.match(inp) and moveregex.group(1) in board.squares2 and moveregex.group(2) in board.possiblemoves(moveregex.group(1))):
            print('Error with move, please use format:a3 b4')
            inp = input('Enter move: ')
        board.move(moveregex.group(1), moveregex.group(2))
        t1 = !t1
#TODO display winner

