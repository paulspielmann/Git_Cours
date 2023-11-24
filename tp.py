from random import randint
from time import time

# Pour dessiner des courbes
# from matplotlib.pyplot import plot, show, legend, xlabel, ylabel

def main():
    #test_gen_tab_int()
    # print("temps d'exec moyen: ", mesure_appartient(20, 1, 1, 100))
    # mesures(100, gen_tab_int(100, 1, 100), inclus, 50)
    # mesures(100, gen_tab_int(100, 1, 100), inclus_rapide, 50)
    # mesures(1000, gen_tab_int(1000, 1, 1000), inclus_rapide, 50)
    # mesures(100000)
    # mesures(100000)
    test_inclus()

def max(tab):
    res = tab[0]
    i = 1
    n = len(tab)

    while i < n:
        if tab[i] > res: res = tab[i]
        i += 1
    return res

# Test d'inclusion naif complexite quadratique
def inclus(tab1, tab2):
    size = len(tab1)
    i = 0
    # If either array is empty then its included in the other
    if size == 0 or len(tab2) == 0:
        return True

    while i < size:
        if not appartient(tab2, tab1[i]): return False
        i += 1
    return True

# On suppose qu' on teste pour tab1 inclus dans tab2
def inclus_rapide(tab1, tab2):
    size = len(tab2)
    print(size)
    aux = [False] * (size + 1)
    for i in tab2:
        print(i)
        aux[i] = True
    for i in tab1:
        if not aux[i]: return False
    return True

# O(2n + 2) -> complexite lineaire
def appartient(tab, k):
    i = 0
    n = len(tab)
    while i < n:
        if tab[i] == k:
            return True
        i += 1
    return False

def test_inclus():
    assert inclus([1, 2, 3], [3, 2, 1])
    assert inclus([], [])
    assert inclus([1, 1, 2, 1, 2], [3, 2, 1])
    assert not inclus([1], [2, 3, 4, 5, 6])
    assert not inclus([1, 10, 19, 20], [1, 19, 20, 19, 1, 20])
    print("Test de la fonction inclus : ok")

# Generate pseudo random array of size n with values in range [mini..maxi]
def gen_tab_int(n, mini, maxi):
    arr = [0] * n
    i = 0
    while(i < n):
        arr[i] = randint(mini, maxi)
        i += 1
    return arr

def test_gen_tab_int():
    assert gen_tab_int(0, 1, 10) == []
    assert gen_tab_int(1, 1, 1) == [1]
    assert gen_tab_int(6, 4, 4) == [4, 4, 4, 4, 4, 4]
    tab = gen_tab_int(400, 0, 1)
    assert len(tab) == 400
    i = 0
    while i < 400:
        assert tab[i] == 0 or tab[i] == 1
        i += 1

    print("Test de la fonction gen_tab_int : ok")

# prends en param
# func : fonction a tester
# n : la taille du tableau qui sera genere
# val : parametre qui sera passe a func
# mini, maxi : range pour les valeurs dans le tab
# tries : nb d'essais

def mesure(n, val, mini, maxi, func, tries):
    i = 0
    res = 0

    while i < tries:
        test = gen_tab_int(n, mini, maxi)
        #print(test)
        start = time()
        func(test, val)
        end = time()
        res += (end - start)
        i += 1

    return (res/tries)

def mesure_multiples(taille, val, mini, maxi, func, tries):
    size = len(taille)
    res = [0] * size
    i = 0

    while (i < size):
        res[i] = mesure(taille[i], val, mini, maxi, func, tries)
        i += 1
    return res

def mesures(n, val, func, tries):
    tailles = [100, 1000, 10000, 20000, 50000]
    result = mesure_multiples(tailles, val, 1, n,
                              func, tries)
    print("Tableau de nombres entre 1 et ", n, "\n")
    for i in range(len(result)):
        print("Tableau de taille ", tailles[i], " temps d'exec moyen: ", result[i])
    #     plot(tailles, result, label=("Valeurs entre 1 et test"))
    #     xlabel("Tailles d'array")
    #     ylabel("Temps d'exec")
    # show()

main()
