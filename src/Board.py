from Hole import Hole

class Board:
    """ Classe qui gere le plateau de jeu, TODO fonctions pour distribuer les garines dans les trous """
    def __init__(self):
        self._holes = []
        for i in range(16):
            hole = Hole(i)
            self._holes.append(hole)
    
