from Board import Board
from Bcolors import bcolors
def parseTurnInput(s):
    array = list(s)
    color = array[-1]
    arrayHole = array[:-1]
    hole = int(''.join(arrayHole))
    return hole, color

class Game:
    """ Classe qui gere les evenments de la partie, fonction pour jouer, etc..."""
    def __init__(self):
        self.board = Board()                                           
        self.status = "Initialised"
        self.player1Bank = 0
        self.player2Bank = 0                                              
    
    def _playTurn(self, turnPlayed, turnId, whosPlaying):                              ## played is what we receive form the other player ex:(16B)
        self.status = "Playing"
        holePlayed, playedColor = parseTurnInput(turnPlayed)
        if ((whosPlaying == "player1" and turnId % 2 != 0 and holePlayed % 2 != 0) or (whosPlaying == "player2" and turnId % 2 == 0 and holePlayed % 2 == 0)):
            hand = self.board[holePlayed - 1]._takeSeeds(playedColor)
            if (type(hand) is str):
                print(hand)
                return False
            elif (hand[playedColor] == 0) :
                print(bcolors.WARNING + "Tu ne peux pas jouer ce coup, le trou n'a plus de graines de cette couleur")
                return False
        else:
            print(bcolors.WARNING + "Tu ne peux pas jouer ce coup, le joueur 1 possede les trous impairs")
            
            return False
       
        if playedColor == "B":
            harvestStart = self._playBlueSeeds(hand["B"], holePlayed)
            harvested = self._harvest(harvestStart)
            if (whosPlaying == "player2" and turnId % 2 != 0):
                self.player2Bank += harvested
            elif (whosPlaying == "player2" and turnId % 2 == 0):
                self.player2Bank += harvested
            else:
                self.player1Bank += harvested

        else:
            harvestStart = self._playRedSeeds(hand["R"], holePlayed)
            harvested = self._harvest(harvestStart)
            if (whosPlaying == "player2" and turnId % 2 != 0):
                self.player2Bank += harvested
            elif (whosPlaying == "player2" and turnId % 2 == 0):
                self.player2Bank += harvested
            else:
                self.player1Bank += harvested
        
        limit = 0
        limit = self._checkend(limit)
        if (limit < 8 or self.player1Bank > 32 or self.player2Bank > 32):
            self.status = "Finished"
        return self.board
    
    def _playRedSeeds(self, seeds, holePlayed):
        if (holePlayed % 16 != 0):
            starting = holePlayed
        else :
            starting = 0
        for i in range(seeds):
           
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
        hole = self.board[start - 1]
        blueSeeds = hole._get_blueSeeds()
        redSeeds = hole._get_redSeeds()
        if (blueSeeds + redSeeds == 2 or blueSeeds + redSeeds == 3):
            total += hole._empty()
            total += self._harvest(start - 1)
        return total

    def _checkend(self,limit):
        
        for i in range(0, 16):
            limit += self.board[i]._get_redSeeds()
            limit += self.board[i]._get_blueSeeds()

        
        
        return limit


    


