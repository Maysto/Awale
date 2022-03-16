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

def defaultMove(playing):
    if playing == "player1":
        return "0B"
    elif playing == "player2" :
        return "1B"

def minimax(startingBoard, depth, isMax, turnId, playing) :
    score = evaluate(startingBoard, playing)
    if depth > 3:
        return score
    board = Game()
    board.board = startingBoard.board
    board.player1Bank = startingBoard.player1Bank
    board.player2Bank = startingBoard.player2Bank
    
    if (isMax) :    
        best = -1000
        if playing == "player1" :
            for i in range(0, 14, 2) :       
             
                if (board.board[i]._get_redSeeds() > 0) :
                    move  = str(i) + "R"
                    board._playTurn(parsed(move), turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId + 1, "player2") )
 
                    board.board = startingBoard.board
                    board.player1Bank = startingBoard.player1Bank
                    board.player2Bank = startingBoard.player2Bank
                if (board.board[i]._get_blueSeeds() > 0) :
                    move  = str(i) + "B"
                    board._playTurn(parsed(move), turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId + 1, "player2") )
 
                    board.board = startingBoard.board
                    board.player1Bank = startingBoard.player1Bank
                    board.player2Bank = startingBoard.player2Bank
            return best
        elif playing == "player2" :
            for i in range(1, 15, 2) :
                if (board.board[i]._get_redSeeds() > 0) :
                    move  = str(i) + "R"
                    board._playTurn(parsed(move), turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId + 1, "player1") )
 
                    board.board = startingBoard.board
                    board.player1Bank = startingBoard.player1Bank
                    board.player2Bank = startingBoard.player2Bank
                if (board.board[i]._get_blueSeeds() > 0) :
                    move  = str(i) + "B"
                    board._playTurn(parsed(move), turnId, playing)
 
                    best = max(best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId + 1, "player1"))
 
                    board.board = startingBoard.board
                    board.player1Bank = startingBoard.player1Bank
                    board.player2Bank = startingBoard.player2Bank
            return best
    else :
        best = 1000
        if playing == "player1":
            for i in range(0, 14, 2) :        
                if (board.board[i]._get_blueSeeds() > 0) :
                    move = str(i) + "B"
                    board._playTurn(parsed(move), turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player2"))
                    board.board = startingBoard.board
                    board.player1Bank = startingBoard.player1Bank
                    board.player2Bank = startingBoard.player2Bank
                if (board.board[i]._get_redSeeds() > 0):
                    move = str(i) + "R"
                    board._playTurn(parsed(move), turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player2"))
                    board.board = startingBoard.board
                    board.player1Bank = startingBoard.player1Bank
                    board.player2Bank = startingBoard.player2Bank
            return best
        elif playing == "player2" :
            for i in range(1, 15, 2) :        
                if (board.board[i]._get_blueSeeds() > 0) :
                    move = str(i) + "B"
                    board._playTurn(parsed(move), turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player1"))
                    board.board = startingBoard.board
                    board.player1Bank = startingBoard.player1Bank
                    board.player2Bank = startingBoard.player2Bank
                if (board.board[i]._get_redSeeds() > 0):
                    move = str(i) + "R"
                    board._playTurn(parsed(move), turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player1"))
                    board.board = startingBoard.board
                    board.player1Bank = startingBoard.player1Bank
                    board.player2Bank = startingBoard.player2Bank
            return best

def getTurn(startingBoard, playing, turnId):
    bestVal = -1000
    bestMove = defaultMove(playing)
    board = Game()
    board.board = startingBoard.board
    board.player1Bank = startingBoard.player1Bank
    board.player2Bank = startingBoard.player2Bank
    if playing == "player1":
        for i in range(0, 14, 2) :    
            if (board.board[i]._get_blueSeeds() > 0) :
                move = str(i) + "B"
                board._playTurn(parsed(move), turnId, playing)
                board.board = startingBoard.board
                board.player1Bank = startingBoard.player1Bank
                board.player2Bank = startingBoard.player2Bank
                moveVal = minimax(board, 0, False, turnId, playing)
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
            if (board.board[i]._get_redSeeds() > 0):
                move = str(i) + "R"
                board._playTurn(parsed(move), turnId, playing)
                board.board = startingBoard.board
                board.player1Bank = startingBoard.player1Bank
                board.player2Bank = startingBoard.player2Bank
                moveVal = minimax(board, 0, False, turnId, playing)
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
        return parsed(bestMove)
    elif playing == "player2" :
        for i in range(1, 15, 2) :    
            if (board.board[i]._get_blueSeeds() > 0) :
                move = str(i) + "B"
                board._playTurn(parsed(move), turnId, playing)
                board.board = startingBoard.board
                board.player1Bank = startingBoard.player1Bank
                board.player2Bank = startingBoard.player2Bank
                moveVal = minimax(board, 0, False, turnId, playing)
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
            if (board.board[i]._get_redSeeds() > 0):
                move = str(i) + "R"
                board._playTurn(parsed(move), turnId, playing)
                board.board = startingBoard.board
                board.player1Bank = startingBoard.player1Bank
                board.player2Bank = startingBoard.player2Bank
                moveVal = minimax(board, 0, False, turnId, playing)
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
        return parsed(bestMove)
