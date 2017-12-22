import board, re

board = board.Board()
t1 = True

moveregex = re.compile('^([a-h][1-8]) ([a-h][1-8])$')

while True: #board.hasmove(t1):
    if t1:
        board.display1()
        print('Team 1 to move.')
        inp = input('Enter move [ie. a3 b4] ')
        cmd = moveregex.match(inp)
        while not (cmd and cmd.group(1) in board.squares1 and cmd.group(2) in board.possiblemoves(cmd.group(1))):
            print('Error with move, please use format:a3 b4')
            inp = input('Enter move: ')
        board.move(cmd.group(1), cmd.group(2))
        t1 = not t1
    else:
        board.display2()
        print('Team 2 to move.')
        inp = input('Enter move [ie. a3 b4] ')
        cmd = moveregex.match(inp)
        while not (cmd and cmd.group(1) in board.squares2 and cmd.group(2) in board.possiblemoves(cmd.group(1))):
            print('Error with move, please use format:a3 b4')
            inp = input('Enter move: ')
        board.move(cmd.group(1), cmd.group(2))
        t1 = not t1
#TODO display winner
#TODO get rid of repetition by using .format
