# ************************************************************************************** #
#                                                                                        #
#                                                    :::     :::::::::    :::   :::      #
#    main.py                                        :+: :+:   :+:    :+:  :+:+: :+:+:    #
#                                                 +:+   +:+  +:+    +:+ +:+ +:+:+ +:+    #
#    By: adamfraga <adam.fraga@live.fr>         +#++:++#++: +#+    +:+ +#+  +:+  +#+     #
#                                              +#+     +#+ +#+    +#+ +#+       +#+      #
#    Created: 2021/09/29 11:32:31 by adam     #+#     #+# #+#    #+# #+#       #+#       #
#    Updated: 2021/09/29 13:53:37 by adam    ###     ### #########  ###       ###i       #
#                                                                                        #
# ************************************************************************************** #

# Créer une classe “Livre” avec comme attribut un “titre” qu’elle reçoit en
# paramètre à la construction et une référence vers une classe “Auteur”.
# Ajouter une méthode “print” permettant d’afficher dans le terminal le titre du
# livre. Créer une classe “Auteur” héritant de la classe “Personne” recevant
# un nom et un prenom en paramètre de construction. La classe auteur
# devra posséder une collection de livres nommé “oeuvre” en attribut ainsi
# qu’une méthode “listerOeuvre” affichant dans le terminal la liste des livres
# écrits par l’auteur. Ajouter à la classe Auteur une méthode “ecrireUnLivre”
# prenant en paramètre un titre de livre à écrire et générer une instance de la
# classe livre avec ce titre. Ajouter ce nouveau livre à l’oeuvre de l’auteur.

# Importe le chemin en absolu afin d'éviter de réecrire la class
import sys
sys.path.insert(1,'/Users/adamfraga/Projets/Python/runtrack-python/jour02/job01')

from Personne import Personne

Adam = Personne("Adam","Fraga")
print(Adam)

class Livre:

    def __init__(self, title):
        self._title = title

    def print_title(self):
        print("Le titre du livre est {}".format(self._title))

class Auteur (Personne):
      # Appel constructeur de la classe mère (Personne)
    def __init__(self, name, firstname, oeuvre, Book):
        # La methode super permet de faire référence à la class parente et
        # permet ainsi de récuperer ses Attributs et methode
        super().__init__(name, firstname)
        self._oeuvre = oeuvre
        self._Book = Book

    def listerOeuvre(self):
        print("Liste des livres: {}".format(self._oeuvre))
    
    def ecrireUnLivre(self, title):
        self._Book = title
        self._oeuvre.append(self._Book)

Niourk = Livre("Niourk")
Niourk.print_title()

Auteur = Auteur("Stefan","Wul",["La mort vivante","Piège sur Zarkass","Odyssée sous contrôle"], Niourk)

Auteur.SePresenter()
Auteur.listerOeuvre()

Auteur.ecrireUnLivre("Rayon pour Sidar")
Auteur.listerOeuvre()
