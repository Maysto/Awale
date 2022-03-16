from Game import Game
from Agent import getTurn
from Bcolors import bcolors
import copy

awale = Game()
turnId = 1
canContinue = True

while ( awale.status != "Finished" ):
    botBoard = copy.deepcopy(awale)
    if (canContinue and turnId % 2 == 0):
        minmaxTurn = getTurn(botBoard, "player2", turnId)
        print("L'ordinateur a joué : "+minmaxTurn)
        canContinue = awale._playTurn(minmaxTurn, turnId, "player2")
        print(bcolors.OKMAGENTA +"Fin du tour : " + str(awale.board))
        print("\n"+bcolors.OKMAGENTA +"Stocks des joueurs : " + bcolors.OKBLUE + "\nJoueur 2 : " + str(awale.player2Bank) + bcolors.OKRED+ "\nJoueur 1 : " + str(awale.player1Bank))
        if (canContinue):
            turnId += 1
    elif (canContinue and turnId % 2 != 0):
        turn = input(bcolors.OKGREEN+'JOUEUR 1 : Quel est votre coup ? ')
        canContinue = awale._playTurn(turn, turnId, "player1")
        print(bcolors.OKMAGENTA +"Fin du tour : " + str(awale.board))
        print("\n"+bcolors.OKMAGENTA +"Stocks des joueurs : " + bcolors.OKBLUE + "\nJoueur 2 : " + str(awale.player2Bank) + bcolors.OKRED+ "\nJoueur 1 : " + str(awale.player1Bank))
        if (canContinue):
            turnId += 1
    elif (not canContinue and turnId % 2 != 0):
        turn = input(bcolors.OKGREEN+'JOUEUR 1 : Quel est votre coup ? ')
        canContinue = awale._playTurn(turn, turnId, "player1")
        print(bcolors.OKMAGENTA +"Fin du tour : " + str(awale.board))
        print("\n"+bcolors.OKMAGENTA +"Stocks des joueurs : " + bcolors.OKBLUE + "\nJoueur 2 : " + str(awale.player2Bank) + bcolors.OKRED+ "\nJoueur 1 : " + str(awale.player1Bank))
        if (canContinue):
            turnId += 1
    elif (not canContinue and turnId % 2 == 0):
        minmaxTurn = getTurn(botBoard, "player2", turnId)
        print("L'ordinateur a joué : "+minmaxTurn)
        canContinue = awale._playTurn(minmaxTurn, turnId, "player2")
        print(bcolors.OKMAGENTA +"Fin du tour : " + str(awale.board))
        print("\n"+bcolors.OKMAGENTA +"Stocks des joueurs : " + bcolors.OKBLUE + "\nJoueur 2 : " + str(awale.player2Bank) + bcolors.OKRED+ "\nJoueur 1 : " + str(awale.player1Bank))
        if (canContinue):
            turnId += 1