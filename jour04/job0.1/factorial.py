nb = input("Entrez un entier en paramètre")
nb = int(nb)
result = nb

# Memo Toujours définir une condition d'arret
# Une fois la fonction appelé le code en amont de celle ci est réalisé tant que la condition d'arret n'est pas atteinte
# Les fonctions s'empilent sur la stack FILO First in Last out(La première empilé sera la dernière depilé)
# Condition d'arret atteinte -> Le code en avale de la fonction est en respectant un sens sur la pile
# LIFO -> last in last out la dernière a être empilé est executé en 1ère


def factorial(n):
    if n == 0:
        return True
    else:
        # Executé FILO  que condition d'arret non respecté
        print("N Avant:{}".format(n))
        ft = factorial(n - 1)
        # Executé LIFO  si condition d'arrêt respecté
        print("N Après:{}".format(n))
        print("recursion de n:{} * ft:{} - 1 resultat -> {}".format(n, n, n * ft))
        return n * ft


if int(nb):
    print(factorial(nb))
else:
    print("vous devez entrer un entier \n")
