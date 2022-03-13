from Game import Game

awale = Game(True)


while (input("Voulez vous rejouez") == "oui" ):
    turn = int(input('Tu joues quel trou batard : '))
    color = input('et quelle couleur sale con : ')
    awale._playTurn(turn, color)



