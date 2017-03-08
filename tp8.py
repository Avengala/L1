from tkinter import *


def afficher_grille():
    d = 40
    for i in range(10 + 1):
        grille.create_line(d * i + d, d, d * i + d, d * 10 + d)
        grille.create_line(d, d * i + d, d * 10 + d, d * i + d)

    # grille.create_line(50, 50, 200, 50)
    # grille.create_line(50, 50, 50, 200)
    # grille.create_line(50, 50 + 50, 200, 50 + 50)
    # grille.create_line(50 + 50, 50, 50 + 50, 200)
    # grille.create_oval(70, , 75, 65)
    # grille.create_line(60, 60, 70, 75)


def quitter():
    jeu.quit()
    jeu.destroy()


jeu = Tk()
jeu.title("Petit jeu sympa")

grille = Canvas(jeu, width=500, height=500, bg="white")
grille.pack(side=LEFT)

startButton = Button(jeu, text="Départ", command=afficher_grille)
startButton.pack(side=TOP)

Hbutton = Button(jeu, text="H")
Hbutton.pack(side=TOP)

buttonsFrame = Frame(jeu)
Gbutton = Button(buttonsFrame, text="G")
Gbutton.pack(side=LEFT)
Dbutton = Button(buttonsFrame, text="D")
Dbutton.pack()

Bbutton = Button(jeu, text="H")
Bbutton.pack(side=TOP)

scoreFrame = Frame(jeu)
scoreFrame.pack(side=BOTTOM)

scoreLabel = Label(scoreFrame, text="Votre score")
scoreLabel.pack(side=LEFT)

scoreText = Text(scoreFrame, width=10, height=10)
scoreText.pack()

quitButton = Button(jeu, text="Quitter", command=quitter)
quitButton.pack(side=BOTTOM)

jeu.mainloop()