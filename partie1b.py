from random import *
from tkinter import *

nbr = 4
grille = []


# 1
def cree_grille(n, val):
    res = [0] * n
    for i in range(n):
        res[i] = [val] * n
    return res


# 2
def affiche_grille(g):
    for i in range(len(g)):
        res = ""
        for j in range(len(g[i])):
            res += ajout_espace(g[i][j], 1000) + " "
        print(res)


# Fonction permettant le décalage pour les chiffres inférieur à 1000
def ajout_espace(chiffre, quotient):
    res = str(chiffre)
    if chiffre // quotient == 0:
        if quotient // 10 != 0:
            res = ajout_espace(chiffre, quotient / 10) + " "
    elif 0 == chiffre < 1000:
        res = str(chiffre) + " "
    return res


# 3
def appartient(val, g):
    for x in g:
        for y in x:
            if y == val:
                return True
    return False


# 3.1
def gagnante(g):
    return appartient(2048, g)


# 3.2
def pleine(g):
    return not appartient(0, g)


# 4
def valeur_max(g):
    maxi = 0

    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] >= maxi:
                maxi = g[i][j]
    return maxi


# 5.a
def les_cases(g, val):
    liste = []

    for i in range(len(g)):
        for j in range(len(g[i])):
            newliste = []
            if val == g[i][j]:
                newliste.extend((i, j))
                liste.append(newliste)
    return liste


# 5.b
def vides(g):
    return les_cases(g, 0)


# 5.c
def ajoute_alea(g, val):
    pos = choice(vides(g))
    g[pos[0]][pos[1]] = val
    return g


# 5.d
def init(n):
    global grille
    grille = cree_grille(n, 0)
    nbr1 = 2 ** randint(1, 2)
    nbr2 = 2 ** randint(1, 2)
    grille = ajoute_alea(grille, nbr1)
    grille = ajoute_alea(grille, nbr2)
    return grille


# 6

# Fonction permettant de retirer tou les zéro d'une chaine
def coupezero(liste):
    newliste = []
    for i in range(len(liste)):
        if liste[i] != 0:
            newliste.append(liste[i])
    return newliste


def fusion(liste, i, j):
    liste[i] = liste[j] * 2
    liste[j] = 0
    return liste


def haut(g):
    global nbr
    total = 0
    for i in range(len(g)):
        lst = []
        for j in range(len(g[i])):
            total = 0
            lst.append(g[j][i])
        x = 0
        while x < len(lst):
            if lst[x] != total:
                total = lst[x]
            elif lst[x] != 0:
                total = 0
                lst = fusion(lst, x, x - 1)
            x += 1
        ligne = coupezero(lst)
        size = len(ligne)
        for y in range(nbr - size):
            ligne.append(0)
        for y in range(len(g)):
            g[y][i] = ligne[y]
    return g


def bas(g):
    global nbr
    total = 0
    for i in range(len(g)):
        lst = []
        for j in range(len(g[i])):
            total = 0
            lst.append(g[j][i])
        x = len(lst) - 1
        while x >= 0:
            if lst[x] != total:
                total = lst[x]
            elif lst[x] != 0:
                total = 0
                lst = fusion(lst, x, x + 1)
            x -= 1
        ligne = coupezero(lst)
        size = len(ligne)
        for y in range(nbr - size):
            ligne.insert(y, 0)
        for y in range(len(g[i])):
            g[y][i] = ligne[y]

    return g


def droite(g):
    global nbr
    total = 0
    for i in range(len(g)):
        lst = []
        for j in range(len(g[i])):
            total = 0
            lst.append(g[i][j])
        x = len(lst) - 1
        while x >= 0:
            if lst[x] != total:
                total = lst[x]
            elif lst[x] != 0:
                total = 0
                lst = fusion(lst, x, x + 1)
            x -= 1
        ligne = coupezero(lst)
        size = len(ligne)
        for y in range(nbr - size):
            ligne.insert(y, 0)
        for y in range(len(g[i])):
            g[i][y] = ligne[y]
    return g


def gauche(g):
    global nbr
    for i in range(len(g)):
        lst = []
        for j in range(len(g[i])):
            lst.append(g[i][j])
        total = 0
        x = 0
        while x < len(lst):
            if lst[x] != total:
                total = lst[x]
            elif lst[x] != 0:
                total = 0
                lst = fusion(lst, x, x - 1)
            x += 1
        ligne = coupezero(lst)
        size = len(ligne)
        for y in range(nbr - size):
            ligne.append(0)
        for y in range(len(g[i])):
            g[i][y] = ligne[y]

    return g


# 7
def partie(n):
    global grille
    grille = init(n)
    affiche_grille(grille)
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
            print("vous avez gagné")
        nbr1 = 2 ** randint(1, 2)
        nbr2 = 2 ** randint(1, 2)
        print(nbr1, nbr2)
        grille = ajoute_alea(nbr1, grille)
        grille = ajoute_alea(nbr2, grille)
        affiche_grille(grille)
        if pleine(grille) == 1:
            # liste = les_cases(grille, 2)
            # limite = perdante(liste)
            # if limite == 0:
            print("vous avez perdu, votre score est de : ", valeur_max(grille))
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


# Q2
def message(chaine):
    zone_texte.delete("0.0", END)
    zone_texte.insert(END, chaine)


# Q3
def dessine_grille(g):
    c = 40
    x0 = 100
    y0 = 100
    n = len(g)
    for i in range(n):
        for j in range(n):
            x = g[i][j]
            color = str(couleur(x))
            case = Frame(fond, width=100, height=100)
            case.grid(row=i, column=j, padx=2, pady=2)
            if x != 0:
                text = Label(case, text=x, width=8, height=4, bg=color,
                             font=("Ubuntu", 20, "bold"), justify=CENTER)
            else:
                text = Label(case, text="", width=8, height=4, bg=color,
                             font=("Ubuntu", 20, "bold"), justify=CENTER)
            text.grid()


# Q3.1
def couleur(n):
    dico = {0: "#FFFFFF", 2: "#91FFD2", 4: "#B2D8E7", 8: "#B2C4DF",
            16: "#6FB8FF", 32: "#339ED7", 64: "#50EEEF", 128: "#6893EC",
            256: "#0040EC", 512: "#6F40E0", 1024: "#7C0C59", 2048: "#C50CD1"}
    return dico[n]


# Q4
def clavier(event):
    global grille
    event = event.keysym
    if event == "Up":
        grille = haut(grille)
    elif event == "Down":
        grille = bas(grille)
    elif event == "Left":
        grille = gauche(grille)
    elif event == "Right":
        grille = droite(grille)
    nbr1 = 2 ** randint(1, 2)
    nbr2 = 2 ** randint(1, 2)
    grille = ajoute_alea(grille, nbr1)
    grille = ajoute_alea(grille, nbr2)
    dessine_grille(grille)
    if gagnante(grille) == 1:
        message("Bravo vous avec gagné, vous pouvez recommencer")
    elif pleine(grille) == 1:
        msg = "Perdu ! Votre score est de " + str(valeur_max(grille)) + ", vous pouvez recommencer"
        msg += (valeur_max(grille))
        message(msg)


def fermer():
    plateau.quit()
    plateau.destroy()


def jeu():
    global nbr
    global grille
    grille = init(nbr)
    dessine_grille(grille)


# Q1
plateau = Tk()
plateau.title("2048 - Version L1 2017")

# Cadre blanc pour pouvoir y appliquer une marge
cadre = Frame(plateau, padx=20, pady=20, bg="blue")
fond = Frame(cadre, bg="gray", padx=2, pady=2,
             width=300, height=300)
fond.grid()
cadre.grid(row=0, rowspan=3)

bJouer = Button(plateau, text="Jouer", command=jeu,
                justify=CENTER, font=("Ubuntu", 20))
bJouer.grid(row=0, column=1)

zone_texte = Text(plateau, width=40, height=5)
zone_texte.grid(row=1, column=1)
bQuitter = Button(plateau, text="Quitter", command=fermer,
                  font=("Ubuntu", 20))
bQuitter.grid(row=2, column=1)

plateau.bind("<Up>", clavier)
plateau.bind("<Down>", clavier)
plateau.bind("<Right>", clavier)
plateau.bind("<Left>", clavier)

plateau.mainloop()
