def recherche(nom, prenom, bottin):
    file = open(bottin, "r")
    for line in file:
        x = line.split()
        if x[0] == nom and x[1] == prenom:
            file.close()
            return x[2][:-1]
    return []


def reherche_nom(nom, bottin):
    file = open(bottin, "r")
    lst = []
    for line in file:
        x = line.split()
        if x[0] == nom:
            lst.append(line[:-1])
    file.close()
    return lst


def combien(fic, pre):
    file = open(fic, "r")
    i = 0
    for line in file:
        x = line.split()
        if x[2][:len(pre)] == pre
            i += 1
    file.close()
    return i


def ressemble(num, ref):
    i = 0
    while i < len(num):
        if num[i] != ref[i] and num[i] != "*":
            return False
        i += 1
    return True


def compatible(ref, bottin):
    file = open(bottin, "r")
    for line in file:
        x = line.split()
        if ressemble(ref, x[2]):
            print(line)
    file.close()


def interne_fac(bottin):
    fileName = "Fac" + bottin
    file = open(fileName, "r")
    bottinFile = open(bottin, "r")
    for line in bottinFile:
        x = line.split()
        if x[2][0:6] == "023156":
            file.write(x[0] + " " + x[1] + " " + x[2][6:])
    bottinFile.close()
    file.close()


def ajoute_0(nom, prenom, num, fic):
    file = open(fic, "a")
    file.write(nom + " " + prenom + " " + num + '\n')
    file.close()


def ajoute(nom, prenom, num, fic):
    file = open(fic, "a")
    lines = file.readlines()
    file.close()
    file2 = open(fic, "w")
    for line in lines:
        x = line.split()
        if x[0] == nom and x[1] == prenom and x[2] != num:
            g = input("Même nom et prénom. Voulez-vous l'ajouter ?")
            if g == 0:
                file2.write(nom + " " + prenom + " " + num + '\n')
            else:
                file2.write(line)
        else:
            file2.write(line)
    file2.close()


def commun(bot1, bot2):
    file = open(bot1, "r")
    for line in file:
        x = line.split()
        r = recherche(x[0], x[1], bot2)
        if r and r == x[2]:
            res += [(x[0], x[1])]


def creer_dico(fic):
    file = open(fic, "r")
    dic = {}
    for line in file:
        x = line.split()
        dic[(x[0], x[1])] = x[2]
    return dic


def suavegarde(dico, fic):
    file = open(fic, "w")
    for (x, y) in dico.items():
        file.write(x + " " + y + " " + dico[(x, y)] + '\n')
    file.close()


print(ressemble("0231**4556", "0231534556"))