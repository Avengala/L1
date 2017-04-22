from random import *


# 1
def cree_grille(n, val):
    res = [0] * n
    for i in range(n):
        res[i] = [val] * n
    return res


# 2
def affiche(grille):
    for i in range(len(grille)):
        res = ""
        for j in range(len(grille[i])):
            res += ajout_espace(grille[i][j], 1000) + " "
        print(res)


# Fonction permettant le décalage pour les chiffres inférieurs à 1000
def ajout_espace(chiffre, quotient):
    res = str(chiffre)
    if chiffre // quotient == 0:
        if quotient // 10 != 0:
            res = ajout_espace(chiffre, quotient / 10) + " "
    elif 0 == chiffre < 1000:
        res = str(chiffre) + " "
    return res


# 3
def appartient(val, grille):
    for x in grille:
        for y in x:
            if y == val:
                return True
    return False


# 3.1
def gagnante(grille):
    return appartient(2048, grille)


# 3.2
def pleine(grille):
    return not appartient(0, grille)


# 4
def valeur_max(grille):
    res = 0
    for x in grille:
        for y in x:
            if y > res:
                res = y
    return res


# 5.a
def les_cases(grille, val):
    liste = []
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == val:
                liste.append([i, j])
    return liste


# 5.b
def vides(grille):
    return les_cases(grille, 0)


# 5.c
def ajoute_alea(grille, val):
    pos = choice(vides(grille))
    grille[pos[0]][pos[1]] = val
    return grille


# 5.d
def init(n):
    grille = cree_grille(n, 0)
    val1, val2 = randrange(2, 5, 2), randrange(2, 5, 2)
    grille = ajoute_alea(grille, val1)
    grille = ajoute_alea(grille, val2)
    return grille


# 6

# Fonction permettant de retirer tou les zéro d'une chaine
def coupe_zero(liste):
    newliste = []
    for x in liste:
        if x != 0:
            newliste.append(x)
    return newliste


def fusion(liste, i, j):
    liste[i] = liste[j] * 2
    liste[j] = 0
    return liste


def haut(grille):
    for i in range(len(grille)):
        lst = []
        for j in range(len(grille[i])):
            lst.append(grille[j][i])
        x = 0
        total = 0
        while x < len(lst):
            if lst[x] != total:
                total = lst[x]
            elif lst[x] != 0:
                total = 0
                lst = fusion(lst, x, x - 1)
            x += 1
        ligne = coupe_zero(lst)
        size = len(ligne)
        for y in range(4 - size):
            ligne.append(0)
        for y in range(len(grille)):
            grille[y][i] = ligne[y]


def bas(grille):
    for i in range(len(grille)):
        lst = []
        for j in range(len(grille[i])):
            total = 0
            lst.append(grille[j][i])
        x = len(lst) - 1
        while x >= 0:
            if lst[x] != total:
                total = lst[x]
            elif lst[x] != 0:
                total = 0
                lst = fusion(lst, x, x + 1)
            x -= 1
        ligne = coupe_zero(lst)
        size = len(ligne)
        for y in range(4 - size):
            ligne.insert(y, 0)
        for y in range(len(grille[i])):
            grille[y][i] = ligne[y]


def droite(grille):
    for i in range(len(grille)):
        lst = []
        for j in range(len(grille[i])):
            lst.append(grille[i][j])
        total = 0
        x = len(lst) - 1
        while x >= 0:
            if lst[x] != total:
                total = lst[x]
            elif lst[x] != 0:
                total = 0
                lst = fusion(lst, x, x + 1)
            x -= 1
        ligne = coupe_zero(lst)
        size = len(ligne)
        for y in range(4 - size):
            ligne.insert(y, 0)
        for y in range(len(grille[i])):
            grille[i][y] = ligne[y]


def gauche(grille):
    for i in range(len(grille)):
        lst = []
        for j in range(len(grille[i])):
            lst.append(grille[i][j])
        total = 0
        x = 0
        while x < len(lst):
            if lst[x] != total:
                total = lst[x]
            elif lst[x] != 0:
                total = 0
                lst = fusion(lst, x, x - 1)
            x += 1
        ligne = coupe_zero(lst)
        size = len(ligne)
        for y in range(4 - size):
            ligne.append(0)
        for y in range(len(grille[i])):
            grille[i][y] = ligne[y]


# 7
def partie(n):
    grille = init(n)
    affiche(grille)
    stop = 0
    limite = 0
    while stop != 1:
        coup = input("action ?('h', 'b', 'd', 'g')")
        if coup == "h" and limite != 2:
            haut(grille)
        elif coup == "b" and limite != 2:
            bas(grille)
        elif coup == "d" and limite != 1:
            droite(grille)
        elif coup == "g" and limite != 1:
            gauche(grille)
        stop = gagnante(grille)
        if stop == 1:
            print("Vous avez gagné")
        nbr1 = 2 ** randint(1, 2)
        nbr2 = 2 ** randint(1, 2)
        grille = ajoute_alea(grille, nbr1)
        grille = ajoute_alea(grille, nbr2)
        affiche(grille)
        if pleine(grille) == 1:
            #            liste = les_cases(2, grille)
            #            limite = perdante(liste)
            #            if limite == 0:
            print("Vous avez perdu, votre score est de : ", valeur_max(grille))
            stop = 1


# fonction permettant de détection si il reste un coup jouable
def perdante(liste):
    compt = -1
    total = -1
    for i in range(len(liste)):
        if liste[i][0] != compt:
            compt = liste[i][0]
        elif compt != -1:
            # print(i, (liste[i-1][1]+1), liste[i][1])
            if (liste[i - 1][1] + 1) == liste[i][1]:
                return 1
        if liste[i][1] != total:
            total = liste[i][1]
        elif total != -1:
            # print("e1", (liste[i-1][0]+1), liste[i][0])
            if (liste[i][0]) == liste[i][0]:
                return 2
    return 0


g1 = [[0, 0, 2, 2], [4, 2, 2, 8], [0, 2, 32, 0], [128, 2, 1024, 2048]]
g2 = [[4, 2, 16, 8], [8, 2, 4, 2], [2, 2, 2, 4], [4, 4, 4, 2]]
partie(4)
