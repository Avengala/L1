# Vincent de Menezes
# Maël Querré

d = {"Lyon": 491268, "Strasbourg": 272222, "Angers": 148803, "Rennes": 208033, "Bordeaux": 239399, "Nice": 344064, "Reims": 180752, "Toulouse": 447340, "Metz": 119962, "Amiens": 133327, "Brest": 140547, "Limoges": 137758, "Grenoble": 157424, "Caen": 108793, "Nantes": 287845}

departements = {"Lyon": 69, "Strasbourg": 67, "Angers": 45, "Rennes": 35, "Bordeaux": 33, "Nice": 6, "Reims": 51, "Metz": 57, "Amiens": 80, "Brest": 29, "Grenoble": 38, "Caen": 14, "Nantes": 44}


def moyenne(dico):
    res = 0
    for x in dico.values():
        res += x
    res = res / len(dico)
    return res


def plushabitants(nb, dico):
    lst =[]
    for x in dico:
        if dico[x] >= nb:
            lst += (x, dico[x])
    return lst


def affichage(dico):
    lst = list(dico.keys())
    lst.sort()
    for x in lst:
        print(x, dico[x], "habitants")


def milliers(dico):
    for i in dico:
        dico[i] = dico[i] // 1000
    return dico


def maximini(dico):
    max = 0
    res, resmin = (), ()
    for x in dico:
        if dico[x] >= max:
            max = dico[x]
            res = (x,)
    min = max
    for y in dico:
        if dico[y] <= min:
            min = dico[y]
            resmin = (y,)
    res += resmin
    return res


def affichage_departements(dico, depart):
    lst = list(dico.keys())
    lst.sort()
    lst2 = list(depart.keys())
    lst2.sort()
    for x in range(len(lst)):
       for y in range(len(lst2)):
            if lst[x] == lst2[y]:
                print(lst[x], dico[lst[x]], "habitants.", " ", "Numéro du département :", depart[lst[x]])


print(moyenne(d))
print(plushabitants(250000, d))
affichage(d)
print(maximini(d))
affichage_departements(d, departements)
print(milliers(d))