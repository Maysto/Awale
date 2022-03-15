from Game import Game
from Agent import Agent
from Bcolors import bcolors

awale = Game()
agent = Agent()
turnId = 1
canContinue = True

while ( awale.status != "Finished" ):
    if (canContinue and turnId % 2 == 0):
        minmaxTurn = agent._getTurn(awale.board, "player2")
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
        minmaxTurn = agent._getTurn("player2")
        canContinue = awale._playTurn(minmaxTurn, turnId, "player2")
        if (canContinue):
            turnId += 1