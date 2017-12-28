import board, re

def getvalidmove(team):
    moveregex = re.compile('^([a-h][1-8]) ([a-h][1-8])$')
    inp = input('Enter move [ie. a3 b4] ')
    cmd = moveregex.match(inp)
    while not (cmd and cmd.group(1) in board.squares[t1] and cmd.group(2) in board.possiblemoves(cmd.group(1)).keys()):
        print('Error with move, please use format:a3 b4')
        if not cmd:
            print('Does not match format')
        elif cmd.group(1) not in board.squares[t1]:
            print(cmd.group(1), 'not in your camp')
        elif cmd.group(2) not in board.possiblemoves(cmd.group(1)).keys():
            print(cmd.group(2), 'is not a possible square for', cmd.group(1))
        inp = input('Enter move: ')
        cmd = moveregex.match(inp)
    return cmd

board = board.Board()
t1 = True

while board.hasmove(t1):
    board.display(t1)
    if t1:
        print('Team 1 to move.')
    else:
        print('Team 2 to move.')
    cmd = getvalidmove(t1)
    board.move(cmd.group(1), cmd.group(2))
    while board.possiblemoves(cmd.group(1))[cmd.group(2)] == True:
        ask = input('Make follow-up capture? [Y/N]: ')
        if ask.lower() == 'y':
            cmd2 = getvalidmove(t1)
            while not (cmd2.group(1) == cmd.group(2) and board.possiblemoves(cmd2.group(2))[cmd2.group(2)] == True):
                print('You must use', cmd.group(2), 'to make a capturing move.')
                cmd2 = getvalidmove(t1)
            board.move(cmd2.group(1), cmd2.group(2))
            cmd = cmd2
        else: break
    t1 = not t1
#TODO display winner
if t1 == True:
    print('Congratulations team 2! You win!')
else:
    print('Congratulations team 1! You win!')

