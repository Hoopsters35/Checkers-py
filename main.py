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
    capture = board.possiblemoves(cmd.group(1))[cmd.group(2)]
    board.move(cmd.group(1), cmd.group(2))
    while capture == True:
        #add if statement for if another capture is possible, otherwise break
        anothercap = False
        posmoves = board.possiblemoves(cmd.group(2))
        #iterate through possible moves for the new square to see if there are any new capturing moves
        for i in posmoves.keys():
            if posmoves[i] == True:
                anothercap = True
        #if there is not, the turn ends
        if not anothercap: break
        else:
            #display board after first capture
            board.display(t1)
            ask = input('Make follow-up capture? [Y/N]: ')
            if ask.lower() == 'y':
                cmd2 = getvalidmove(t1)
                #after getting a traditional valid move, further restrict that move
                #must use same piece and capture again
                while not (cmd2.group(1) == cmd.group(2) and board.possiblemoves(cmd2.group(1))[cmd2.group(2)] == True):
                    print('You must use', cmd.group(2), 'to make a capturing move.')
                    cmd2 = getvalidmove(t1)
                #not sure if this redefinition of capture is necessary as the move must be a cap
                capture = board.possiblemoves(cmd2.group(1))[cmd2.group(2)]
                board.move(cmd2.group(1), cmd2.group(2))
                #makes the new move the old move in order to check for a next jump
                cmd = cmd2
            #end turn if they do not want additional capture
            else: break
    t1 = not t1
#display winner
if t1 == True:
    print('Congratulations team 2! You win!')
else:
    print('Congratulations team 1! You win!')

