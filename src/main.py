from Game import Game

awale = Game(True)

turn = int(input('Tu joues quel trou batard : '))
color = input('et quelle couleur sale con : ')

awale._playTurn(turn, color)
