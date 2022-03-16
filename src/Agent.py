from Game import Game
import copy

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
    if playing == "player1":
        mySeeds = 0
        opponentSeeds = 0
        for hole in board.board:
            if (hole._get_Id() % 2 != 0):
                mySeeds += hole._get_blueSeeds() + hole._get_redSeeds()
            else :
                opponentSeeds += hole._get_blueSeeds() + hole._get_redSeeds()
        if board.player1Bank == board.player2Bank or mySeeds == opponentSeeds:
            return 0
        elif board.player1Bank > board.player2Bank and mySeeds > opponentSeeds :
            return 2
        elif board.player1Bank > board.player2Bank or mySeeds > opponentSeeds :
            return 1
        else :
            return -1
    else :
        mySeeds = 0
        opponentSeeds = 0
        for hole in board.board:
            if (hole._get_Id() % 2 == 0):
                mySeeds += hole._get_blueSeeds() + hole._get_redSeeds()
            else :
                opponentSeeds += hole._get_blueSeeds() + hole._get_redSeeds()
        if board.player1Bank == board.player2Bank or mySeeds == opponentSeeds:
            return 0
        elif board.player2Bank > board.player1Bank and mySeeds > opponentSeeds :
            return 2
        elif board.player2Bank > board.player1Bank or mySeeds > opponentSeeds :
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
    if depth > 10:
        return score
    board = copy.copy(startingBoard)
    
    if (isMax) :    
        best = -1000
        if playing == "player1" :
            for i in range(0, 14, 2) :       
             
                if (board.board[i]._get_redSeeds() != 0) :
                    move  = str(i) + "R"
                    isValid = board._playTurn(parsed(move), turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId + 1, "player2") )
 
                    board = copy.copy(startingBoard)
                if (board.board[i]._get_blueSeeds() != 0) :
                    move  = str(i) + "B"
                    board._playTurn(parsed(move), turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId + 1, "player2") )
 
                    board = copy.copy(startingBoard)
            return best
        elif playing == "player2" :
            for i in range(1, 15, 2) :
                if (board.board[i]._get_redSeeds() != 0) :
                    move  = str(i) + "R"
                    board._playTurn(parsed(move), turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId + 1, "player1") )
 
                    board = copy.copy(startingBoard)
                if (board.board[i]._get_blueSeeds() != 0) :
                    move  = str(i) + "B"
                    board._playTurn(parsed(move), turnId, playing)
 
                    best = max(best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId + 1, "player1"))
 
                    board = copy.copy(startingBoard)
            return best
    else :
        best = 1000
        if playing == "player1":
            for i in range(0, 14, 2) :        
                if (board.board[i]._get_blueSeeds() != 0) :
                    move = str(i) + "B"
                    board._playTurn(parsed(move), turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player2"))
                    board = copy.copy(startingBoard)
                if (board.board[i]._get_redSeeds() != 0):
                    move = str(i) + "R"
                    board._playTurn(parsed(move), turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player2"))
                    board = copy.copy(startingBoard)
            return best
        elif playing == "player2" :
            for i in range(1, 15, 2) :        
                if (board.board[i]._get_blueSeeds() != 0) :
                    move = str(i) + "B"
                    board._playTurn(parsed(move), turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player1"))
                    board = copy.copy(startingBoard)
                if (board.board[i]._get_redSeeds() != 0):
                    move = str(i) + "R"
                    board._playTurn(parsed(move), turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player1"))
                    board = copy.copy(startingBoard)
            return best

def getTurn(startingBoard, playing, turnId):
    bestVal = -1000
    bestMove = defaultMove(playing)
    board = copy.copy(startingBoard)
    if playing == "player1":
        for i in range(0, 14, 2) :    
            if (board.board[i]._get_blueSeeds() != 0) :
                move = str(i) + "B"
                board._playTurn(parsed(move), turnId, playing)
                board = copy.copy(startingBoard)
                moveVal = minimax(board, 0, False, turnId, playing)
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
            if (board.board[i]._get_redSeeds() != 0):
                move = str(i) + "R"
                board._playTurn(parsed(move), turnId, playing)
                board = copy.copy(startingBoard)
                moveVal = minimax(board, 0, False, turnId, playing)
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
        return parsed(bestMove)
    elif playing == "player2" :
        for i in range(1, 15, 2) :    
            if (board.board[i]._get_blueSeeds() != 0) :
                move = str(i) + "B"
                board._playTurn(parsed(move), turnId, playing)
                board = copy.copy(startingBoard)
                moveVal = minimax(board, 0, False, turnId, playing)
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
            if (board.board[i]._get_redSeeds() != 0):
                move = str(i) + "R"
                board._playTurn(parsed(move), turnId, playing)
                board = copy.copy(startingBoard)
                moveVal = minimax(board, 0, False, turnId, playing)
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
        return parsed(bestMove)
