from os import error
import numpy as np


class Game:
    """Représentation du jeu de dames."""

    def __init__(self):
        self._size = 0
        self._bord = np.zeros([self._size], [self._size])
        # Syntaxe de compréhension de listes voir mes notes (code doc Python)
        self._axe_X = [x for x in range(self._size)]
        self._axe_Y = [y for y in range(self._size)]
        self._dames = self._size

    def _getsize(self):
        try:
            return self.size
        except error:
            print("La taille ne peut pas être retournée")

    def _setsize(self, size):
        if int(size) > 2:
            try:
                self._size = size
            except AttributeError:
                print("Le plateau doit avoir une taille superieur a 2")

    # Respect de l'ordre des parametres Voir Notes code doc Python property
    size = property(_getsize, _setsize)
