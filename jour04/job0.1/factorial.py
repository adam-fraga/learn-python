nb = input("Entrez un entier en paramètre")
nb = int(nb)
result = nb


def factorial(n):
    test = "Avant facto"
    if n == 0:
        return True
    else:
        print("N Before {}".format(n))
        print(test)
        ft = factorial(n - 1)
        test = "Après Facto"
        print(test)
        print("N After{}".format(n))
        print("recursion de n:{} * ft:{} - 1 resultat -> {}".format(n, n, n * ft))
        return n * ft


print(factorial(nb))
