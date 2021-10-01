nb = int(input("Entre un votre nombre"))

# Créer un programme demandant à l’utilisateur de renseigner un nombre
# entier. Votre programme devra calculer x^n, ou n est le nombre fourni par
# l’utilisateur, sans utiliser de fonction autre que les vôtres. Attention, vous ne
# devez utiliser ni while, ni for, ni foreach ni ... boucle. Seulement de la
# récursivité.


def ft_pow_recursive(nb):
    if nb == 0:  # Condition d'arrêt fixé si input user = 0
        print("test2")
        return True
    else:
        print("Avant")
        ft_pow_recursive(nb - 1)  # Décrémeente l'entré utilisateur
        print("Après")
        nb = pow(
            nb, nb
        )  # LIFO  La dernière valeur a être popé étant la même que l'entré utilisateur pow -> elle même
        print("Pow:{}".format(nb))


ft_pow_recursive(nb)
