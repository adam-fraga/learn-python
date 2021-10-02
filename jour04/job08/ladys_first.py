from os import error
import numpy as np


class Game:
    """Représentation du jeu de dames."""

    def __init__(self):
        self._size = 0
        self._board = np.zeros([self._size], [self._size])
        # Syntaxe de compréhension de listes voir mes notes (code doc Python)
        self._axe_X = [x for x in range(self._size)]
        self._axe_Y = [y for y in range(self._size)]
        self._dames = self._size

    # Récupère la taille global
    def _getsize(self):
        try:
            return self._size
        except Exception as e:
            print("La taille ne peut pas être retournée \n")
            raise e

    # Initialise la taille du plateau
    def _setsize(self, size):
        if int(size) > 2:
            try:
                self._size = size
            except Exception as e:
                print("Le plateau doit avoir une taille superieur a 2\n")
                raise e

    # Récupère le plateau du jeu (a afficher avec un print ou faire methode)
    def _getboard(self):
        try:
            return self._board
        except Exception as e:
            print("Le plateau de jeu doit être initialisé \n")
            raise e

    # Initialise le plateau du joueur avec un tableau numpy n*n
    def _setboard(self, board):
        try:
            self._board = board
        except Exception as e:
            print("Impossible de réinitialiser le plateau de jeu \n")
            raise e

    # Récupère l'axe des abscisses (sous forme de liste)
    def _getaxe_X(self):
        try:
            return self._axe_X
        except Exception as e:
            print("Impossible de récupéré l'axe X \n")
            raise e

    # initialise la liste des abscisses
    def _setaxe_X(self, axe_X):
        try:
            self._axe_X = axe_X
        except Exception as e:
            print("Impossible d'initialiser l'axe X \n")
            raise e

    # Récupère l'axe des ordinnées (sous forme de liste)
    def _getaxe_Y(self):
        try:
            return _setaxe_Y
        except Exception as e:
            print("Impossible de récupéré l'axe Y \n")
            raise e

    # initialise la liste des ordonnées
    def _setaxe_Y(self, axe_Y):
        try:
            self._axe_Y = axe_Y
        except Exception as e:
            print("Impossible d'initialiser l'axe Y \n")
            raise e

    # Récupère le nombre de dame = a la taille de l'input user
    def _getdames(self):
        try:
            return self._dames
        except Exception as e:
            print("Impossible de réxupérè le nombre de dames \n")
            raise e

    # Respect de l'ordre des parametres Voir Notes code doc Python property
    size = property(_getsize, _setsize)
    board = property(_getboard, _setboard)
    axe_X = property(_getaxe_X, _setaxe_X)
    axe_Y = property(_getaxe_Y, _setaxe_Y)
    dames = property(_getdames, _setdames)
