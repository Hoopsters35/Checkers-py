import board
board = board.Board()
t1 = True
while board.hasmove(t1):
    if t1:
        board.display1()
        print('Team 1 to move.')
        inp = input('Enter move [ie. a3 b4] ')
        while not (len(inp) == 5 and inp[:2] in board.squares1 and inp[2] == ' ' and inp[3:5] in board.possiblemoves(inp[:2])):
            print('Error with move, please use format:a3 b4')
            inp = input('Enter move: ')
        board.move(inp[:2], inp[3:5])
        t1 = !t1
    else:
        board.display2()
        print('Team 2 to move.')
        inp = input('Enter move [ie. a3 b4] ')
        while not (len(inp) == 5 and inp[:2] in board.squares2 and inp[2] == ' ' and inp[3:5] in board.possiblemoves(inp[:2])):
            print('Error with move, please use format:a3 b4')
            inp = input('Enter move: ')
        board.move(inp[:2], inp[3:5])
        t1 = !t1
#TODO display winner

