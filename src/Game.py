from Board import Board
from colorama import init, Fore, Back, Style
from Bcolors import bcolors
def parseTurnInput(s):
    array = list(s)
    color = array[-1]
    arrayHole = array[:-1]
    hole = int(''.join(arrayHole))
    return hole, color

class Game:
    """ Classe qui gere les evenments de la partie, fonction pour jouer, etc.... TODO faire la fonction pour jouer un tour de jeu  """
    def __init__(self, isStarting):
        self.board = Board()
        self.isAIStarting = isStarting                                              ## True if it is my turn to play esle turn it to false
        self.status = "Initialised"
        self.playerBank = 0
        self.botBank = 0                                              
    
    def _playTurn(self, turnPlayed, turnId):                              ## played is what we receive form the other player ex:(16B)
        self.status = "Playing"
        holePlayed, playedColor = parseTurnInput(turnPlayed)
        print(holePlayed, playedColor)
        hand = self.board[holePlayed - 1]._takeSeeds(playedColor)
        if (type(hand) is str):
            print(hand)
            return
        if playedColor == "B":
            harvestStart = self._playBlueSeeds(hand["B"], holePlayed)
            harvested = self._harvest(harvestStart)
            if (self.isAIStarting and turnId % 2 != 0):
                self.botBank += harvested
            elif (not self.isAIStarting and turnId % 2 == 0):
                self.botBank += harvested
            else:
                self.playerBank += harvested

        else:
            harvestStart = self._playRedSeeds(hand["R"], holePlayed)
            harvested = self._harvest(harvestStart)
            if (self.isAIStarting and turnId % 2 != 0):
                self.botBank += harvested
            elif (not self.isAIStarting and turnId % 2 == 0):
                self.botBank += harvested
            else:
                self.playerBank += harvested
        print(bcolors.OKMAGENTA +"Fin du tour : " + str(self.board))
        print("\n"+bcolors.OKMAGENTA +"Stocks des joueurs : " + bcolors.OKBLUE + "\nBot : " + str(self.botBank) + bcolors.OKRED+ "\nJoueur : " + str(self.playerBank))
        limit = 0
        limit = self._checkend(limit)
        if (limit < 8):
            self.status = "Finished"
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


    


