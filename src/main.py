from Game import Game

def isGoodEntry(entry):
    if (isStarting == "premier" or isStarting == "Premier" or isStarting == "deuxieme" or isStarting == "Deuxieme"):
        return True
    else:
        print("Entree non valide.")
        return False

isStarting = input("Voulez commencer ou jouer en deuxieme ? ")
while (isGoodEntry(isStarting) == False):
    isStarting = input("Veuillez entrer un choix valide [premier] | [deuxieme] : \n")

awale = Game(isStarting)
turnId = 1

while ( awale.status != "Finished" ):
    turn = int(input('Tu joues quel trou batard : '))
    color = input('et quelle couleur sale con : ')
    awale._playTurn(turn, color, turnId)
    turnId += 1