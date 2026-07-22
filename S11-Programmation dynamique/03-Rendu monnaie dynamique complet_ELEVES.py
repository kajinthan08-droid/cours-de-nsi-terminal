from math import inf

def renduMonnaieDetaille(somme, listeValeursFaciales):
    """Fonction retournant une liste contennant la valeur faciale des billets
       nécessaires au rendu de la somme donnée en 1er argument."""
    
    # Création des tableaux de travail :
    tabRendus = [0] * (somme + 1)
    tabResteDu = [0] * (somme + 1)
    
    # Boucle de parcours des tableaux de travail :
    for sousRendu in range(1, somme + 1):
        mini = inf
        for valeur in listeValeursFaciales:
            if valeur <= sousRendu:
                # Recherche et validation de l'opération optimale (nombre de pièces minimal) :
                if 1 + tabRendus[sousRendu - valeur] < mini :
                    mini = 1 + tabRendus[sousRendu - valeur]
                    tabResteDu[sousRendu] = sousRendu - valeur       # Mémorisation de la somme (et donc de l'indice) assurant le rendu de monnaie en lui ajout x.
        tabRendus[sousRendu] = mini

    # Boucle de parcours qui remonte l'ensemble des sommes intermédiaire du rendu de monnaie :
    monnaie = []
    resteDu = somme    
    while resteDu > 0 : 
        # CODE A COMPLETER
        # CODE A COMPLETER
        
    return monnaie


# Exemple d'exploitation de la fonction :
# ---------------------------------------

Sn = [5, 2, 1]
somme = 8
print("Pour donner " + str(somme) + " €, on va donner les pièces/billets suivants : " + str(renduMonnaieDetaille(somme, Sn)))

Sn = [5, 3, 2]
somme = 7
print("Pour donner " + str(somme) + " €, on va donner les pièces/billets suivants : " + str(renduMonnaieDetaille(somme, Sn)))

Sn = [4, 3, 2]
somme = 9
print("Pour donner " + str(somme) + " €, on va donner les pièces/billets suivants : " + str(renduMonnaieDetaille(somme, Sn)))

Sn = [6, 4, 2]
somme = 13
print("Pour donner " + str(somme) + " €, on va donner les pièces/billets suivants : " + str(renduMonnaieDetaille(somme, Sn)))