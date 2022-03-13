from Hole import Hole

class Board:
    """ Classe qui gere le plateau de jeu, TODO fonctions pour distribuer les garines dans les trous """
    def __init__(self):
        self._holes = []
        for i in range(1, 17):
            hole = Hole(i)
            self._holes.append(hole)
    
    def __getitem__(self, position):
        return self._holes[position]

    def __repr__(self):
        return str(self._holes)
