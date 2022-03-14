from Board import Board

class Game:
    """ Classe qui gere les evenments de la partie, fonction pour jouer, etc.... TODO faire la fonction pour jouer un tour de jeu  """
    def __init__(self, isStarting):
        self.board = Board()
        self.player1 = isStarting                                              ## True if it is my turn to play esle turn it to false
        self.status = "Initialised"                                           
    
    def _playTurn(self, holePlayed, playedColor):                              ## played is what we receive form the other player ex:(16B)
        self.status = "Playing"
        print("Debut du tour : " + str(self.board))
        hand = self.board[holePlayed - 1]._empty(playedColor)
        if playedColor == "B":
            harvestStart = self._playBlueSeeds(hand["B"], holePlayed)
            self._harvest(harvestStart)
        else:
            harvestStart = self._playRedSeeds(hand["R"], holePlayed)
            self._harvest(harvestStart)
        print("Fin du tour : " + str(self.board))
        return self.board
    
    def _playRedSeeds(self, seeds, holePlayed):
        if (holePlayed % 16 != 0):
            starting = holePlayed
        else :
            starting = 0
        for i in range(seeds):
            print(self.board[starting])
            self.board[starting]._add_redSeed()
            starting = (starting + 1) % 16
        return starting
    
    def _playBlueSeeds(self, seeds, holePlayed):
        if (holePlayed % 16 != 0):
            starting = holePlayed
        else :
            starting = 0
        for i in range(seeds):
            
            self.board[starting ]._add_blueSeed()
            starting = (starting + 2) % 16
        return starting
    
    def _harvest(self, start):
        if (start < 0):
            start = 15
        total = 0
        hole = self.board[start]
        blueSeeds = hole._get_blueSeeds()
        redSeeds = hole._get_redSeeds()
        while (blueSeeds + redSeeds == 2 or blueSeeds + redSeeds == 3):
            print(" Je suis dedans")
            
            total += hole._empty("R") + hole._empty("B")
            start = start - 1
            hole = self.board[start]
            blueSeeds = hole._get_blueSeeds()
            redSeeds = hole._get_redSeeds() 
        else:
            print ("Total du harvest : "+ str(total))
            return total

