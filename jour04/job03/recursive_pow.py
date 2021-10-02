nb = int(input("Entre un votre nombre"))


def ft_pow_recursive(nb):
    if nb == 0:  # Condition d'arrêt fixé si input user = 0
        print("test2")
        return True
    else:
        print("Avant")  # (Ordre d'empilage FILO)
        ft_pow_recursive(nb - 1)  # Décrémeente l'entrée utilisateur
        print("Après")
        nb = pow(
            nb, nb
        )  # ordre dépilage LIFO  La dernière valeur a être popé sur la stack
        # est la première a être dépile donc élève celle ci puissance elle même
        print("Pow:{}".format(nb))


ft_pow_recursive(nb)
