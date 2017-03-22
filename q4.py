def teste(fichier):
    p = open(fichier, "r")

    for line in p:
        if line[-2] != ".":
            return False

    return True

print(teste("consigne.txt"))
