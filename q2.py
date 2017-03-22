def ajoute(consigne, fichier):
    try:
        p = open(fichier, "r")
    except IOError:
        print("Erreur du nom du fichier")
    else:
        c = open(fichier, "a")
        c.write(consigne)
        c.close()

ajoute("surtout chute !!", "consige.txt")
