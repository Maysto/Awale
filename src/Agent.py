class Agent:
    """Minimax agent that will play against the other player"""

    def _evaluate(b, playing) :
        if playing % 2 == 0:

        else:

    def _getTurn(self, board, depth, isMax):
        score = self._evaluate(board, depth)

        if (score == 10):
            return score
        
        if (score == -10):
            return score
        
        if (isMax):
            best = -1000

            if (depth % 2 == 0):
                for (i in range(0, len(board), 2)):
                    
            else:        
                for (i in range(1, len(board), 2)):