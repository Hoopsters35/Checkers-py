import board, re

def get_valid_move(team):
    moveregex = re.compile('^([a-h][1-8]) ([a-h][1-8])$') #Checks for a3 b4 pattern
    proposedMove = input('Enter move [ie. a3 b4] ')
    confirmedMove = moveregex.match(proposedMove)
    while not (confirmedMove and confirmedMove.group(1) in board.squares[t1] and confirmedMove.group(2) in board.possible_moves(confirmedMove.group(1)).keys()):
        print('Error with move, please use format:a3 b4')
        if not confirmedMove:
            print(proposedMove, 'does not match format: a3 b4')
        elif confirmedMove.group(1) not in board.squares[t1]:
            print(confirmedMove.group(1), 'is not one of your pieces!')
        elif confirmedMove.group(2) not in board.possible_moves(confirmedMove.group(1)).keys():
            print(confirmedMove.group(2), 'is not a possible square for', confirmedMove.group(1))
        proposedMove = input('Enter move: ')
        confirmedMove = moveregex.match(proposedMove)
    return confirmedMove

board = board.Board()
t1 = True

while board.has_move(t1):
    board.display(t1)
    if t1:
        print('Team 1 to move.')
    else:
        print('Team 2 to move.')
    currentUserMove = get_valid_move(t1)
    isCaptureMove = board.possible_moves(currentUserMove.group(1))[currentUserMove.group(2)]
    board.move(currentUserMove.group(1), currentUserMove.group(2))
    while isCaptureMove == True:
        #Add if statement for if another capture is possible, otherwise break
        anothercap = False
        possibleFollowupMoves = board.possible_moves(currentUserMove.group(2))
        #Iterate through possible moves for the new square to see if there are any new capturing moves
        for i in possibleFollowupMoves.keys():
            if possibleFollowupMoves[i] == True:
                anothercap = True
        #If there is not, the turn ends
        if not anothercap: break
        else:
            #Display board after first capture
            board.display(t1)
            askForMulticapture = input('Make follow-up capture? [Y/N]: ')
            if askForMulticapture.lower() == 'y':
                nextUserMove = get_valid_move(t1)
                #After getting a traditional valid move, further restrict that move
                #Must use same piece and capture again
                while not (nextUserMove.group(1) == currentUserMove.group(2) and board.possible_moves(nextUserMove.group(1))[nextUserMove.group(2)] == True):
                    print('You must use', currentUserMove.group(2), 'to make a capturing move.')
                    nextUserMove = get_valid_move(t1)
                board.move(nextUserMove.group(1), nextUserMove.group(2))
                #Makes the new move the old move in order to check for a next jump
                currentUserMove = nextUserMove
            #End turn if they do not want additional capture
            else: break
    t1 = not t1
#Display winner
board.display(not t1)
if t1 == True:
    print('Congratulations team 2! You win!')
else:
    print('Congratulations team 1! You win!')

