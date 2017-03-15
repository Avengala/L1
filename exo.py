#!/usr/bin/python

d= {'Lyon': 491268, 'Strasbourg': 272222, 'Angers': 148803, 'Rennes': 208033, 'Bordeaux': 239399, 'Nice': 344064, 'Reims': 180752, 'Toulouse': 447340, 'Metz': 119962, 'Amiens': 133327, 'Brest': 140547, 'Limoges': 137758, 'Grenoble': 157424, 'Caen': 108793, 'Nantes': 287845}

def plushabitants(nb, dico):
    i = 0
    lst =[]
    while i < len(dico.values()):
        if dico.values()[i] >= nb:
            lst += (dico.keys()[i], dico.values()[i])
        i += 1
    return lst

print(plushabitants(250000, d))
