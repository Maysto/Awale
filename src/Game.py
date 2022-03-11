from Board import Board

class Game:
    """ Classe qui gere les evenments de la partie, fonction pour jouer, etc.... TODO faire la fonction pour jouer un tour de jeu  """
    def __init__(self, first):
        self.board = Board()
        self.player1 = first ## True if it is my turn to play esle turn it to false
    
    def _playTurn(self, played):  ## played is what we receive form the other player or from our decision AI ex:(16B)
        hand = self.board[played]._empty()  ## TODO played is like 16B we need to parse to retrieve only the int and the color (seperated)
        if hand["R"] == 0:
            self._playeBlueSeeds(hand["B"])
        else:
            self._playeRedSeeds(hand["R"])