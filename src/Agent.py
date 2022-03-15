from Game import Game

def parsed(turn):
    array = list(turn)
    color = array[-1]
    arrayHole = array[:-1]
    hole = int(''.join(arrayHole))
    hole += 1
    unparsedTurn = [str(hole), color]
    parsedTurn = ''.join(unparsedTurn)
    return parsedTurn

def evaluate(board, playing) :
    if board.player1Bank == board.player2Bank :
        return 0
    if playing == "player1":
        if board.player1Bank > board.player2Bank :
            return 1
        else :
            return -1
    else :
        if board.player2Bank > board.player1Bank :
            return 1
        else :
            return -1

def minimax(startingBoard, depth, isMax, turnId, playing, depthLimit) :
    score = evaluate(startingBoard, playing)
    if depthLimit > depth:
        return score
    board = startingBoard
    if (score == 1) :
        return score
 
    if (score == -1) :
        return score
    
    if (isMax) :    
        best = -1000
        if playing == "player1":
            for i in range(0, len(board.board._holes), 2) :       
             
                if (board.board[i]._get_redSeeds() > 0) :
                    move  = str(i) + "R"
                    board._playTurn(move, turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId, playing, depthLimit) )
 
                    board = startingBoard
                if (board.board[i]._get_blueSeeds() > 0) :
                    move  = str(i) + "B"
                    board._playTurn(move, turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId, playing, depthLimit) )
 
                    board = startingBoard
            return best
        else:
            for i in range(0, len(board.board._holes), 2) :
                if (board.board[i]._get_redSeeds() > 0) :
                    move  = str(i) + "R"
                    board._playTurn(move, turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId, playing, depthLimit) )
 
                    board = startingBoard
                if (board.board[i]._get_blueSeeds() > 0) :
                    move  = str(i) + "B"
                    board._playTurn(move, turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId, playing, depthLimit))
 
                    board = startingBoard
    else :
        best = 1000
        if playing == "player1":
            for i in range(0, len(board.board._holes), 2) :        
                if (board.board[i]._get_blueSeeds() > 0) :
                    move = str(i) + "B"
                    board._playTurn(move, turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId, playing, depthLimit))
                    board = startingBoard
                if (board.board[i]._get_redSeeds() > 0):
                    move = str(i) + "R"
                    board._playTurn(move, turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId, playing, depthLimit))
                    board = startingBoard
            return best
        else:
            for i in range(0, len(board.board._holes), 2) :        
                if (board.board[i]._get_blueSeeds() > 0) :
                    move = str(i) + "B"
                    board._playTurn(move, turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId, playing, depthLimit))
                    board = startingBoard
                if (board.board[i]._get_redSeeds() > 0):
                    move = str(i) + "R"
                    board._playTurn(move, turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId, playing, depthLimit))
                    board = startingBoard
            return best

def getTurn(startingBoard, playing, turnId):
    bestVal = -1000
    bestMove = ""
    board = startingBoard
    if playing == "player1":
        for i in range(0, len(board.board._holes), 2) :    
            if (board.board[i]._get_blueSeeds() > 0) :
                move = str(i) + "B"
                board._playTurn(move, turnId, playing)
                moveVal = minimax(board, 0, False, turnId, playing, 10)
                board = startingBoard
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
            if (board.board[i]._get_redSeeds() > 0):
                move = str(i) + "R"
                board._playTurn(move, turnId, playing)
                moveVal = minimax(board, 0, False, turnId, playing, 10)
                board = startingBoard
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
        return bestMove
    else:
        for i in range(0, len(board.board._holes), 2) :    
            if (board.board[i]._get_blueSeeds() > 0) :
                move = str(i) + "B"
                board._playTurn(move, turnId, playing)
                moveVal = minimax(board, 0, False, turnId, playing, 10)
                board = startingBoard
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
            if (board.board[i]._get_redSeeds() > 0):
                move = str(i) + "R"
                board._playTurn(move, turnId, playing)
                moveVal = minimax(board, 0, False, turnId, playing, 10)
                board = startingBoard
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
        return parsed(BestMove)
