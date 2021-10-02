import numpy as np
from numpy.core.records import array


class Game(object):
    """Représentation du jeu de dames."""

    # Constructeur
    def __init__(self, size):
        self._size = size
        self._board = np.empty((self._size, self._size))
        # Syntaxe de compréhension de listes voir mes notes (code doc Python)
        self._axe_X = [x for x in range(self._size)]
        self._axe_Y = [y for y in range(self._size)]
        self._dames = self._size

    # Getter & setters

    # Récupère la taille global
    def _getsize(self):
        try:
            return self._size
        except Exception as e:
            print("La taille ne peut pas être retournée \n")
            raise e

    # Initialise la taille du plateau
    def _setsize(self, size):

        if int(size) > 2 and isinstance(size, int):
            try:
                self._size = size
            except Exception as e:
                print("Le plateau doit avoir une taille superieur a 2\n")
                raise e
        else:
            print("Les dimensions du jeu doivent être de 3 minimum")

    # Récupère le plateau du jeu (a afficher avec un print ou faire methode)
    def _getboard(self):
        try:
            return self._board
        except Exception as e:
            print("Le plateau de jeu doit être initialisé \n")
            raise e

    # Initialise le plateau du joueur avec un tableau numpy n*n
    def _setboard(self, board):
        if isinstance(board, list):
            try:
                self._board = board
            except Exception as e:
                print("Impossible de réinitialiser le plateau de jeu \n")
                raise e
        else:
            print("Le plateau de jeu doit être un tableau")

    # Récupère l'axe des abscisses (sous forme de liste)
    def _getaxe_X(self):
        try:
            return self._axe_X
        except Exception as e:
            print("Impossible de récupéré l'axe X \n")
            raise e

    # initialise la liste des abscisses
    def _setaxe_X(self, axe_X):
        if isinstance(axe_X, list):
            try:
                self._axe_X = axe_X
            except Exception as e:
                print("Impossible d'initialiser l'axe X \n")
                raise e
        else:
            ("L'axe X doit être une liste de valeur")

    # Récupère l'axe des ordinnées (sous forme de liste)
    def _getaxe_Y(self):
        try:
            return self._axe_Y
        except Exception as e:
            print("Impossible de récupéré l'axe Y \n")
            raise e

    # initialise la liste des ordonnées
    def _setaxe_Y(self, axe_Y):
        if isinstance(axe_Y, list):
            try:
                self._axe_Y = axe_Y
            except Exception as e:
                print("Impossible d'initialiser l'axe Y \n")
                raise e
        else:
            print("L'axe des Y doit être une liste")

    # Récupère le nombre de dame = a la taille de l'input user
    # Les dames sont une valeur constante egal à l'input user
    # La constante n'existant pas en python pas de setter
    def _getdames(self):
        try:
            return self._dames
        except Exception as e:
            print("Impossible de récupéré le nombre de dames \n")
            raise e

    # Respect de l'ordre des parametres Voir Notes code doc Python property
    size = property(_getsize, _setsize)
    board = property(_getboard, _setboard)
    axe_X = property(_getaxe_X, _setaxe_X)
    axe_Y = property(_getaxe_Y, _setaxe_Y)
    dames = property(_getdames)

    # Essaie de mouvement attaque allée et retour sur plateau par récursion
    def dame_attack(self, i):
        if i == 0:
            return True
        else:
            print(i)
            self.dame_attack(i - 1)
            print(i)


size = input("Entrez la taille du jeu\n")
size = int(size)
if size:
    print("\nDébut de la partie\n")
    print("Initialisation du tableau...\n")
    # Initialise le jeu
    Game1 = Game(size)
    print(f"Votre plateau fait {Game1._getsize()} * {Game1._getsize()} case\n")
    print(f"Nombre de dames: {Game1._getdames()} représenté par des X \n")
    print("Les cases vides sont représenté par la lettre O\n")
    # Avant de placer dame programmer ses attaques sur plateau en vu de définir les cases disponible?


else:
    print(
        "Vous devez entrer une valeur entière qui représentera la taille du plateau de jeu"
    )
