from random import randint
from time import time

# Pour dessiner des courbes
from matplotlib.pyplot import plot, show, legend, xlabel, ylabel

def main():
    #test_gen_tab_int()
    #print("temps d'exec moyen: ", mesure_appartient(20, 1, 1, 100))
    mesures(100)
    mesures(10000)
    mesures(100000)

# Version naive
def inclus(tab1, tab2):
    i = 0
    j = 0
    n2 = len(tab2)
    n1 = len(tab1)

    while (i < n1):
        current = False
        while (j < n2):
            if (tab1[i] == tab2[j]):
                current = True
                break
            j += 1
        if (not current): return current
        i += 1
    return current

# O(2n + 2) -> linear complexity
def appartient(tab, k):
    i = 0
    n = len(tab)
    while (i < n):
        if (tab[i] == k):
            return True
        i += 1
    return False

# Generate pseudo random array of size n
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

def mesure_appartient(n, val, mini, max):
    i = 0
    res = 0
    # On souhaite tester 20 fois
    while (i < 20):
        test = gen_tab_int(n, mini, max)
        #print(test)
        start = time()
        result = appartient(test, 1)
        end = time()
        #print(val, " appartient ?", " oui" if result else " non")
        res += (end - start) 
        i += 1
    return (res/20)

# Input tableau de tailles de tableaux a tester 
# Output tableau de temps d'exec moyen sur 20 
# essais de la fonction appartient sur tableau 
# de taille taille[i]
def mesure_appartient_multiples(taille, val, mini, maxi):
    size = len(taille)
    res = [0] * size
    i = 0
    while (i < size):
        res[i] = mesure_appartient(taille[i], val, mini, maxi)
        i += 1
    return res

def mesures(n):
    tailles = [100, 1000, 10000, 20000, 50000]
    result = mesure_appartient_multiples(tailles, 1, 1, n)
    print("Tableau de nombres entre 1 et ", n, "\n")
    for i in range(len(result)):
        print("Tableau de taille ", tailles[i], " temps d'exec moyen: ", result[i])
        plot(tailles, result, label=("Valeurs entre 1 et test"))
        xlabel("Tailles d'array")
        ylabel("Temps d'exec")
    show()

main()
