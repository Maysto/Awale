from Game import Game
import copy

def evaluate(board, playing) :
    if playing == "player1":
        if board.player1Bank >= 33:
            return 100
        elif board.player2Bank >= 33:
            return -100
        elif board.player1Bank == board.player2Bank:
            return 0
        elif board.player1Bank > board.player2Bank and board.player1Bank > 0:
            return 75
        elif board.player1Bank > board.player2Bank or board.player1Bank > 0:
            return 50
        else :
            return -100
    else :
        if board.player2Bank >= 33:
            return 100
        elif board.player1Bank >= 33:
            return -100
        elif board.player1Bank == board.player2Bank:
            return 0
        elif board.player2Bank > board.player1Bank and board.player2Bank > 0:
            return 75
        elif board.player2Bank > board.player1Bank or board.player2Bank > 0:
            return 50
        else :
            return -100


def minimax(startingBoard, depth, isMax, turnId, playing) :
    score = evaluate(startingBoard, playing)
    board = copy.copy(startingBoard)

    if (score >= 50 or score == -100):
        return score
    
    if (isMax) :    
        best = -1000
        if playing == "player1" :
            for i in range(0, 14, 2) :       
             
                if (board.board[i]._get_redSeeds() != 0) :
                    move  = str(i+1) + "R"
                    isValid = board._playTurn(move, turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId + 1, "player2"))
 
                    board = copy.copy(startingBoard)
                if (board.board[i]._get_blueSeeds() != 0) :
                    move  = str(i+1) + "B"
                    board._playTurn(move, turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId + 1, "player2") )
 
                    board = copy.copy(startingBoard)
            return best
        elif playing == "player2" :
            for i in range(1, 15, 2) :
                if (board.board[i]._get_redSeeds() != 0) :
                    move  = str(i+1) + "R"
                    board._playTurn(move, turnId, playing)
 
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax, turnId + 1, "player1") )
 
                    board = copy.copy(startingBoard)
                if (board.board[i]._get_blueSeeds() != 0) :
                    move  = str(i+1) + "B"
                    board._playTurn(move, turnId, playing)
 
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
                    move = str(i+1) + "B"
                    board._playTurn(move, turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player2"))
                    board = copy.copy(startingBoard)
                if (board.board[i]._get_redSeeds() != 0):
                    move = str(i+1) + "R"
                    board._playTurn(move, turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player2"))
                    board = copy.copy(startingBoard)
            return best
        elif playing == "player2" :
            for i in range(1, 15, 2) :        
                if (board.board[i]._get_blueSeeds() != 0) :
                    move = str(i+1) + "B"
                    board._playTurn(move, turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player1"))
                    board = copy.copy(startingBoard)
                if (board.board[i]._get_redSeeds() != 0):
                    move = str(i+1) + "R"
                    board._playTurn(move, turnId, playing)
                    best = min(best, minimax(board, depth + 1, not isMax, turnId + 1, "player1"))
                    board = copy.copy(startingBoard)
            return best

def getTurn(startingBoard, playing, turnId):
    bestVal = -1000
    bestMove = ""
    board = copy.copy(startingBoard)
    if playing == "player1":
        for i in range(0, 14, 2) :    
            if (board.board[i]._get_blueSeeds() != 0) :
                move = str(i+1) + "B"
                board._playTurn(move, turnId, playing)
                board = copy.copy(startingBoard)
                moveVal = minimax(board, 0, False, turnId, playing)
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
            if (board.board[i]._get_redSeeds() != 0):
                move = str(i+1) + "R"
                board._playTurn(move, turnId, playing)
                board = copy.copy(startingBoard)
                moveVal = minimax(board, 0, False, turnId, playing)
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
        return bestMove
    elif playing == "player2" :
        for i in range(1, 15, 2) :    
            if (board.board[i]._get_blueSeeds() != 0) :
                move = str(i+1) + "B"
                board._playTurn(move, turnId, playing)
                board = copy.copy(startingBoard)
                moveVal = minimax(board, 0, False, turnId, playing)
                print("MOVE : " + move + " " + str(moveVal))
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
            if (board.board[i]._get_redSeeds() != 0):
                move = str(i+1) + "R"
                board._playTurn(move, turnId, playing)
                board = copy.copy(startingBoard)
                moveVal = minimax(board, 0, False, turnId, playing)
                if (moveVal > bestVal) :               
                    bestMove = move
                    bestVal = moveVal
        return bestMove
