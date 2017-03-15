#!/usr/bin/python3

d= {'Lyon': 491268, 'Strasbourg': 272222, 'Angers': 148803, 'Rennes': 208033, 'Bordeaux': 239399, 'Nice': 344064, 'Reims': 180752, 'Toulouse': 447340, 'Metz': 119962, 'Amiens': 133327, 'Brest': 140547, 'Limoges': 137758, 'Grenoble': 157424, 'Caen': 108793, 'Nantes': 287845}

def milliers(dico):

    for i in dico:
        dico[i] = dico[i] // 1000 

    return dico

print(milliers(d))
