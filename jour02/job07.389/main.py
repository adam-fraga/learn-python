# ************************************************************************************** #
#                                                                                        #
#                                                    :::     :::::::::    :::   :::      #
#    main.py                                        :+: :+:   :+:    :+:  :+:+: :+:+:    #
#                                                 +:+   +:+  +:+    +:+ +:+ +:+:+ +:+    #
#    By: adamfraga <adam.fraga@live.fr>         +#++:++#++: +#+    +:+ +#+  +:+  +#+     #
#                                              +#+     +#+ +#+    +#+ +#+       +#+      #
#    Created: 2021/09/29 13:54:36 by adam     #+#     #+# #+#    #+# #+#       #+#       #
#    Updated: 2021/09/29 20:38:12 by adam    ###     ### #########  ###       ###i       #
#                                                                                        #
# ************************************************************************************** #

class Personne:
    """Class définissant une personne"""
    def __init__(self, firstname, name):
        self._firstname = firstname
        self._name = name

# Fonction se présenter
    def SePresenter(self):
        print("{} {}".format(self._name, self._firstname))

#Getter
    def _getname(self):
        try:
            return self._name
        except AttributeError:
            print("Aucun nom n'a été renseigné pour cette personne")

    def _getfirstname(self):
        try:
            return self._firstname
        except AttributeError:
            print("Aucun prénom n'a été renseigné pour cette personne")
#Setter
    def _setname(self, newname):
            self._name = newname
            return self._name

    def _setfirstname(self, newfirstname):
            self._firstname = newfirstname
            return self._firstname

#property permet de définir les getter setter deleter et helper
    name = property(_getname, _setname)
    firstname = property(_getfirstname, _setfirstname)

class Livre:

    def __init__(self, title):
        self._title = title

    def print_title(self):
        print("Le titre du livre est {}".format(self._title))

class Auteur (Personne):
      # Appel constructeur de la classe mère (Personne)
    def __init__(self, oeuvre, Book):
        # La methode super permet de faire référence à la class parente et
        # permet ainsi de récuperer ses Attributs et methodes
        super().__init__(name, firstname)
        self._oeuvre = oeuvre
        self._Book = Book

    def __listerOeuvre__(self):
        print("Liste des livres: {}".format(self._oeuvre))
    
    def __ecrireUnLivre__(self, title):
        self._Book = title
        self._oeuvre.append(self._Book)


class Client (Personne):
    def __init__(self, collection):
        Personne.__init__(self, name, firstname)
        self._collection = collection

    def _getcollection(self):
        return self._collection

    def _setcollection(self,newcollection):
        try:
            self._collection = newcollection
        except AttributeError:
            print("Impossible d'enregistrer la collection")
    
    collection = property(_getcollection, _setcollection) 

class Bibliotheque:

    def __init__(self, nom, catalogue):
        self.__nom = nom
        self._catalogue = catalogue
    
    def __acheterLivre__(self, Auteur, title, qte):
        if title in Auteur._oeuvre:
            self._catalogue = {qte:title}
        else:
            print("Désolé ce livre n'éxiste pas")

    def __inventaire__(self):
        for key,item in self._catalogue.items():
            print("Il reste {} éxemplaires de {}.".format(item,key))

    # - louer: Cette méthode reçoit en paramètres une instance d’objet
# “Client” ainsi que le nom d’un livre. Si le livre existe et est en stock,
# ajouter ce livre à la collection de livre du client et tenez à jour la
# quantité de ce livre dans la bibliothèque.
    def louer(Client, title):
        if title in self._catalogue:
    # def rendreLivres():
Client = Client("Jean","Lebret","lol")
Livre = Livre("Niourk")
Auteur = Auteur("Lulu","Jack",["LivreZ","LivreX","Niourk"],Livre)
maliste = {'LivreA':3, 'LivreB':2,'Niourk':4}

Bib = Bibliotheque("Mabibli", maliste)
# Bib.acheterLivre(Auteur,"Niourk",2)
Bib.inventaire()

