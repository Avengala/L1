from random import *
from tkinter import *

n = 4
grille = []

#1
def     creeGrille(n, val):
    res = [0] * n
    for i in range(n):
        res[i] = [val] * n
    return res

#2
def     affiche(grille):
    for i in range(len(grille)):
        res = ""
        for j in range(len(grille[i])):
            res += ajout_espace(grille[i][j], 1000) + " "
        print(res)

#Fonction permettant le décalage pour les chiffres inférieur à 1000
def     ajout_espace(chiffre, quotient):
    res = str(chiffre)
    if chiffre // quotient == 0:
        if quotient // 10 != 0: 
            res = ajout_espace(chiffre, quotient / 10) + " "
    elif 0 == chiffre < 1000:
        res = str(chiffre) + " "
    return res

#3
def     appartient(val, grille):
    for i in range(len(grille)):
        for j in grille[i]:
            if j == val:
                return 1
    return 0

#3.1
def     gagnante(grille):
    return appartient(2048, grille)

#3.2
def     pleine(grille):
    if appartient(0, grille) == 1:
        return 0
    return 1

#4
def     max(grille):
    maxi = 0
    
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] >= maxi:
                maxi = grille[i][j]
    return maxi

#5.a
def     lescases(val, grille):
    liste = []

    for i in range(len(grille)):
        for j in range(len(grille[i])):
            newliste = []
            if val == grille[i][j]:
                newliste.extend((i,j))
                liste.append(newliste)
    return liste

#5.b
def     vides(grille):
     return lescases(0, grille)

#5.c
def     ajouteAlea(val, grille):
    nbr = randint(0, len(vides(grille)) - 1)
    pos = vides(grille)
    grille[pos[nbr][0]][pos[nbr][1]] = val
    return grille

#5.d
def     init(n):
    grille = creeGrille(n, 0)
    nbr1 = 2 ** randint(1, 2)
    nbr2 = 2 ** randint(1, 2)
    grille = ajouteAlea(nbr1, grille)
    grille = ajouteAlea(nbr2, grille)
    return grille

#6

#Fonction permettant de retirer tou les zéro d'une chaine
def     coupezero(liste):
    newliste = []
    for i in range(len(liste)):
        if liste[i] != 0:
            newliste.append(liste[i])
    return newliste

def     fusion(liste, i, j):
    liste[i] = liste[j] * 2
    liste[j] = 0
    return liste

def     haut(grille):
    global n
    for i in range(len(grille)):
        lst = []
        for j in range(len(grille[i])):
            total = 0
            lst.append(grille[j][i])
        x = 0
        while x < len(lst):
            if lst[x] != total:
                total = lst[x]
            elif lst[x] != 0:
                total = 0
                lst = fusion(lst, x, x-1)
            x += 1        
        ligne = coupezero(lst)
        size = len(ligne)
        for y in range(n - size):
                ligne.append(0)
        for y in range(len(grille)):
            grille[y][i] = ligne[y]
    return grille

def     bas(grille):
    global n
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
                lst = fusion(lst, x, x+1)
            x -= 1       
        ligne = coupezero(lst)
        size = len(ligne)
        for y in range(n - size):
            ligne.insert(y, 0)
        for y in range(len(grille[i])):
            grille[y][i] = ligne[y]

    return grille

def     droite(grille):
    global n
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
                lst = fusion(lst, x, x+1)
            x -= 1        
        ligne = coupezero(lst)
        size =len(ligne)
        for y in range(n - size):
            ligne.insert(y, 0)
        for y in range(len(grille[i])): 
            grille[i][y] = ligne[y]
    return grille

def     gauche(grille):
    global n
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
                lst = fusion(lst, x, x-1)
            x += 1
        ligne = coupezero(lst)
        size =len(ligne)
        for y in range(n - size):
            ligne.append(0)
        for y in range(len(grille[i])): 
            grille[i][y] = ligne[y]

    return grille
#7
def     partie(n):
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
            print("vous avez gagné")
        nbr1 = 2 ** randint(1, 2)
        nbr2 = 2 ** randint(1, 2)
        print(nbr1, nbr2)
        grille = ajouteAlea(nbr1, grille)
        grille = ajouteAlea(nbr2, grille)
        affiche(grille)
        if pleine(grille) == 1:
#            liste = lescases(2, grille)
#            limite = perdante(liste)
#            if limite == 0:
            print("vous avez perdu, votre score est de : ", max(grille))
            stop = 1

#fonction permettant de détection si il reste un coup jouable
def     perdante(liste):
    compt = -1
    total = -1
    for i in range(len(liste)):
        if liste[i][0] != compt:
            compt = liste[i][0]
        elif compt != -1:
            #print(i, (liste[i-1][1]+1), liste[i][1])
            if (liste[i-1][1]+1) == liste[i][1]:
                return 1
        if liste[i][1] != total:
            total = liste[i][1]
        elif total != -1:
            #print("e1", (liste[i-1][0]+1), liste[i][0])
            if (liste[i][0] ) == liste[i][0]:
                return 2
    return 0

#Q2
def     message(chaine):
    zone_texte.delete("0.0", END)
    zone_texte.insert(END, chaine)

#Q3
def     dessineGrille(grille):
    c = 40
    x0 = 100
    y0 = 100
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            x = grille[i][j]
            color = str(couleur(x))
            case = Frame(fram, bg=color, width=100, height=100)
            case.grid(row=i, column=j, padx=1, pady=1)
            if x != 0:
                text = Label(case, text=x, bg=color, width=4, height=2, justify=CENTER)
            else:
                text = Label(case, text="", bg=color, width=4, height=2, justify=CENTER)    
            text.grid()

#Q3.1
def     couleur(nbr):
    dico={0:"#FFFFFF", 2:"#91FFD2", 4:"#B2D8E7", 8:"#B2C4DF", 16:"#6FB8FF", 32:"#339ED7", 64:"#50EEEF", 128:"#6893EC", 256:"#0040EC", 512:"#6F40E0", 1024:"#7C0C59", 2048:"#C50CD1"}

    return dico[nbr]

#Q4
def     clavier(event):
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
    grille = ajouteAlea(nbr1, grille)
    grille = ajouteAlea(nbr2, grille)
    dessineGrille(grille)
    if gagnante(grille) == 1:
        message("Bravo vous avec gagné, vous pouvez recommencé")
    elif pleine(grille) == 1:
        msg = "Perdus votre score est de"
        msg.append(max(grille))
        message(msg)
 

def     fermer():
    plateau.quit()
    plateau.destroy()

def     jeu():
    global grille
    grille = init(n)
    dessineGrille(grille)

#Q1
plateau = Tk()
plateau.title("jeu 2048 -version L1 2017")

fram = Frame(plateau, bg="grey", width=500, height=500)
fram.grid(row=1, column=0)
bdep = Button(plateau, text="jouer", command=jeu, justify=CENTER,font=("Ubuntu", 20, "bold"))
bdep.grid(row=0, column=1)
zone_texte = Text(plateau, width = 40, height = 5)
zone_texte.grid(row=1, column=1)
bqui = Button(plateau, text="Quitter", command=fermer, font=("Ubuntu", 20, "bold"))
bqui.grid(row=2, column=1)

plateau.bind("<Up>", clavier)
plateau.bind("<Down>", clavier)
plateau.bind("<Right>", clavier)
plateau.bind("<Left>", clavier)

plateau.mainloop()
