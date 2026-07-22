def sacADos1(objValeurs, objMasses, masseMaxiSac):
    """Fonction calculant et retournant la valeur maximale transportable par un sac de masse
       masseMaxiSac avec les objets décris en valeur par la liste objValeurs et la liste objMasses"""
    
    nbrObj = len(objMasses)
    
    # Création du tableau (liste) de mémorisation des résultats intermédiaires :
    # (Le tableau comporte une ligne par objet et une colonne par kilo transportable par le sac)
    tabValSacAdos = []
    for i in range(nbrObj):
        tabValSacAdos.append( [0]*(masseMaxiSac + 1) ) # On initialise toutes les valeurs du tableau à 0.
    
    # Initialisation de la première ligne au format [0, 0, ..., valeurs[0], valeurs[0],...]
    for m in range(objMasses[0], masseMaxiSac + 1): # On complète la partie de droite de la 1ère ligne
        tabValSacAdos[0][m] = objValeurs[0]
 
    # Boucle de parcours de tabValSacAdos :
    for i in range(1, nbrObj):
        # Boucle de copie de la ligne précédente de la colonne de masse nulle jusqu'à la masse de l'objet courant :
        for m in range(objMasses[i]):
            tabValSacAdos[i][m] = tabValSacAdos[i - 1][m]
        
        # Boucle de calcul de la valeur optimale :        
        for m in range(objMasses[i], masseMaxiSac + 1):
            valMaxi = tabValSacAdos[i - 1][m]
            if valMaxi <  # A COMPLETER :
                valMaxi = # A COMPLETER
            tabValSacAdos[i][m] = valMaxi
        
    return tabValSacAdos[nbrObj - 1][masseMaxiSac]


# Exemples d'application des fonctions :
# --------------------------------------

massesObj = [1, 2, 5, 6, 7]
valeursObj = [1, 6, 18, 22, 28]

print(sacADos1(valeursObj, massesObj, 11))


