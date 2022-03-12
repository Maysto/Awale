from Board import Board

class Game:
    """ Classe qui gere les evenments de la partie, fonction pour jouer, etc.... TODO faire la fonction pour jouer un tour de jeu  """
    def __init__(self, isStarting):
        self.board = Board()
        self.player1 = isStarting                                              ## True if it is my turn to play esle turn it to false
    
    def _playTurn(self, holePlayed, playedColor):                              ## played is what we receive form the other player ex:(16B)
        hand = self.board[holePlayed]._empty(playedColor)
        if playedColor == "B":
            self._playeBlueSeeds(hand["B"], holePlayed)
        else:
            self._playeRedSeeds(hand["R"], holePlayed)
    
    def _playeRedSeeds(seeds, holePlayed):
        starting = (holePlayed + 1) % 16
        for i in range(seeds):
            sel.board[starting]._add_redSeed()
            starting = (starting + 1) % 16
    
    def _playeBlueSeeds(seeds, holePlayed):
        starting = (holePlayed + 1) % 16
        for i in range(seeds):
            sel.board[starting]._add_blueSeed()
            starting = (starting + 2) % 16
