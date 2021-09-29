# ************************************************************************************** #
#                                                                                        #
#                                                    :::     :::::::::    :::   :::      #
#    Personne.py                                    :+: :+:   :+:    :+:  :+:+: :+:+:    #
#                                                 +:+   +:+  +:+    +:+ +:+ +:+:+ +:+    #
#    By: adamfraga <adam.fraga@live.fr>         +#++:++#++: +#+    +:+ +#+  +:+  +#+     #
#                                              +#+     +#+ +#+    +#+ +#+       +#+      #
#    Created: 2021/09/29 10:34:33 by adam     #+#     #+# #+#    #+# #+#       #+#       #
#    Updated: 2021/09/29 17:54:28 by adam    ###     ### #########  ###       ###i       #
#                                                                                        #
# ************************************************************************************** #

# Créez une classe “Personne” avec les attributs “name”, “firstname”. Ajoutez
# une méthode “SePresenter()” qui affichera dans le terminal le name et le
# préname de la personne. Ajoutez aussi un constructeur prenant en
# paramètres de quoi donner des valeurs initiales aux attributs “name” et
# “firstname”. Instanciez plusieurs personnes avec les valeurs de construction
# de votre choix et faites appel à la méthode “SePresenter()” afin de vérifier
# que tout fonctionne correctement. Ajouter un “accesseur” et un “mutateur”
# pour chacun des attributs.

class Personne:
    """Class définissant une personne"""

#Constructeur définissant les atributs (Passé en parametre de l'objet)
# (Important en Python les attribut propre aux objet n'ont pas besoin d'être
# définit dans le contexte global de la class a leur création dans le
#  constructeur ceux-ci sont peristants)
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
            print("Aucun name n'a été renseigné pour cette personne")

    def _getfirstname(self):
        try:
            return self._firstname
        except AttributeError:
            print("Aucun name n'a été renseigné pour cette personne")
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

# Instancie des objet personne
# Adam = Personne("Adam","Fraga")
# Chuck = Personne("Chuck","Norris")
# Marie = Personne("Marie","Lou")

# firstname = Adam._getfirstname()
# name = Adam._getname()

# Adam.SePresenter()
# print("Mon prénom est {}".format(firstname))
# print("Mon nom est {}".format(name))
