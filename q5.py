def     numerote(fichier):
    k = open("newconsigne.txt", "w")
    p = open(fichier, "r")
    i = 1
    k.write("On a dans le fichier " + fichier +":" + '\n')
    
    for line in p:
        k.write(str(i) + " " + line)
        i += 1

    k.close()
    p.close()

print(numerote("consigne.txt"))
