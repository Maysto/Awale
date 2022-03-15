from Game import Game

from Bcolors import bcolors

awale = Game()
turnId = 1
canContinue = True

while ( awale.status != "Finished" ):
    if (canContinue and turnId % 2 == 0):
        minmaxTurn = aiAgent._getTurn(awale.board)
        canContinue = awale._playTurn(minmaxTurn, turnId, "player2")
        if (canContinue):
            turnId += 1
    elif (canContinue and turnId % 2 != 0):
        turn = input(bcolors.OKGREEN+'JOUEUR 1 : Quel est votre coup ? ')
        canContinue = awale._playTurn(turn, turnId, "player1")
        if (canContinue):
            turnId += 1
    elif (not canContinue and turnId % 2 != 0):
        turn = input(bcolors.OKGREEN+'JOUEUR 1 : Quel est votre coup ? ')
        canContinue = awale._playTurn(turn, turnId, "player1")
        if (canContinue):
            turnId += 1
    elif (not canContinue and turnId % 2 == 0):
        minmaxTurn = aiAgent._getTurn(awale.board)
        canContinue = awale._playTurn(minmaxTurn, turnId, "player2")
        if (canContinue):
            turnId += 1