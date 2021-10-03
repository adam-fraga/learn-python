import random as rn
import numpy as np


class Game(object):
    """Représentation du jeu de dames."""

    # Constructeur
    def __init__(self, size):
        self._size = size
        # initialise un tableau de 0 a size * size dimension
        self._board = np.zeros(shape=(size, size))
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
    dames = property(_getdames)

    # Définit aléatoirement la position de la première dame sur le plateau et
    # Retourne sa position sous la forme d'un tuple (x,y)
    def __init_queen__(self):
        # -1 (index tableau demarre à 0) Pour placer la première dame
        posX = rn.randint(0, self._size - 1)
        posY = rn.randint(0, self._size - 1)
        self._getboard()[posX][posY] = 7
        return [posX, posY]

    # Essaie de mouvement attaque allée et retour sur plateau par récursion
    # La dame attaque à l'index x + 1 jusqu'a fin de recursion et reviens avec x-1
    def __check_path__(self, i, row, col, pos_first_queen):
        plateau = self._getboard()
        if i == 0:
            return True
        else:
            # Affiche l'indice allant de la fin de la taille a son début?
            # -1 car tab demarre à 0
            self.__check_path__(i - 1, 0, 0, 0)


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

    # Print Tableau avant chemion reine
    print(f"AVANT Dame Attaque\n {Game1._getboard()}")
    # Créer un nombre de dame équivalent à la taille du plateau
    print(Game1.__init_queen__())
    Game1.__check_path__(Game1._getsize(), 0, 0, 0)
    print(f"APRES Dame Attaque\n {Game1._getboard()}")
else:
    print(
        "Vous devez entrer une valeur entière qui représentera la taille du plateau de jeu"
    )
