class Hole:
    """ Classe qui gere les trous et les graines qui sont dedans """
    def __init__(self, id):
        self._id = id
        self.redSeeds = 2
        self.blueSeeds = 2
    
    def _get_redSeeds(self):
        return self.redSeeds
    
    def _get_blueSeeds(self):
        return self.blueSeeds
    
    def _add_redSeed(self):
        self.redSeeds = self.redSeeds + 1
    
    def _add_blueSeed(self):
        self.blueSeeds = self.blueSeeds + 1
    
    def _empty(self):
        res = self.blueSeeds + self.redSeeds
        self.blueSeeds = 0
        self.redSeeds = 0
        return res
    
    def _takeSeeds(self, color):
        if (color == "R"):
            res = { "R": self.redSeeds }
            self.redSeeds = 0
            return res
        elif (color == "B"):
            res = { "B": self.blueSeeds }
            self.blueSeeds = 0
            return res
        else:
            print("Coup non valable, cette couleur de graine n'existe pas")
    
    def __repr__(self):
        return "Trou: " + str(self._id) + ", graines bleues: " + str(self.blueSeeds) + ", graines rouges: " + str(self.redSeeds)
