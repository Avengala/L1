stock = {"crayons": 43, "stylos": 22}
listepays = ["France", "Angleterre", "Allemagne"]


def nb_objets(commande):
    som = 0
    for x in commande.values():
        som += x
    return som


def aug_prix(prix):
    for x in prix:
        prix[x] *= 1.1
    return prix


def facture(commande, prix):
    res = 0
    for x in commande:
        res += commande[x] + prix
    return res


def maxi(commande):
    max = 0
    res = ""
    for x in commande:
        if commande[x] >= max:
            max = commande[x]
            res = x
    return res


def ote(stock, commande):
    for x in commande:
        if x in stock:
            if stock[x] >= commande[x]:
                print("Commande", x, "faite.")
                stock[x] -= commande[x]
            else:
                print("Il manque", commande[x] - stock[x], x)
                stock[x] = 0
        else:
            print("Pas de", x, "dans le stock")


def add_commande(commande1, commande2):
    commande = {}
    commande = commande1.copy()
    for x in commande2:
        if x in commande1:
            commande[x] = commande1[x] + commande2[x]
        else:
            commande[x] = commande2[x]
    return commande


def creation_dico(lst):
    dic = {}
    for x in lst:
        dic[x] = 0
    return dic


def encore_zero(scores):
    return [x for x in scores if scores[x] == 0]


def premiers(scores):
    res = []
    max = 0
    for x, y in scores.items():
        if y > max:
            max = y
            res = [x]
        elif y == max:
            res += [x]
    return res, max


def aff(scores):
    lst = scores.keys()
    lst.sort()
    for x in lst:
        print(x, " ", scores[x], "points")


def saisie(score, pays):
    i = 0
    vu = []
    while i <= 12:
        p = input("Quel pays", i, "points")
        if p in listepays and p not in vu and p != pays:
            score[p] += i
            vu += [p]
            if i < 8:
                i += 1
            else:
                i += 2
        elif p in vu:
            print("Pays déjà noté")
        elif p not in listepays:
            print("Pays n'existe pas")
        elif p == pays:
            print("Pas possible de se noter")


def concours(listepart):
    score = creation_dico(listepart)
    for x in listepart:
        saisie(score, x)
    pr, max = premiers(score)
    for p in pr:
        print(p)
    print(max)