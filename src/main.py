from Game import Game

from colorama import init, Fore, Back, Style
from Bcolors import bcolors

init()

def isGoodEntry(entry):
    if (isStarting == "premier" or isStarting == "Premier" or isStarting == "deuxieme" or isStarting == "Deuxieme"):
        return True
    else:
        print(Fore.RED+"Entree non valide.")
        return False

isStarting = input(bcolors.OKGREEN+"Voulez commencer ou jouer en deuxieme ? ")
while (isGoodEntry(isStarting) == False):
    isStarting = print(bcolors.OKGREEN+"Veuillez entrer un choix valide [premier] | [deuxieme] : \n")
    

awale = Game(isStarting)
turnId = 1

while ( awale.status != "Finished" ):
    turn = input(Fore.GREEN+'Quel est votre coup ? ')
    awale._playTurn(turn, turnId)
    turnId += 1