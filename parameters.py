from scipy.special import comb

Nbsymbole = 5
Nbrouleau = 5
e = 0.5

Pjackpot = (1/Nbsymbole)**(Nbrouleau-1)

Pmise = 0.2

Ppente = 1-Pjackpot-Pmise

k = ((-e+Ppente)/Pjackpot) + 1

total = k * 20
print(total)
