



def addPrixMassique(objet):
    # Calcul des prix/massiques par objet, et ajout du prix massique à l'indice 0 de la liste
    # de définition de chaque objet.
    for i in range(len(objets)):
        objets[i] = [objets[i][1] / objets[i][0], objets[i][0], objets[i][1]]
        
    # Classemet dans l'ordre décroissant des objets selon leur prix/massique :
    objets.sort(reverse = True)
    

def sacAdos_v1(objets, masseMax):
    """ Fonction appliquant l'algorithme glouton pour le problème du sac à dos
        en mode AVEC remise des objets."""
    
    contenuSacAdos = []
    addPrixMassique(objets)
    masseSac = 0
    # Boucle de remplissage du sac :
    i = 0
    while masseSac < masseMax:
        for j in range (len(objets)) :
            if objets[i][1] + masseSac < masseMax:
                contenuSacAdo.append(objets)
                
    
    
    return contenuSacAdos


# Liste contenant les sous-listes associée à chaque objet au format :
# [[masse1, prix1], [masse2, prix2], ....[masseN, prixN]
objetsTest01 = [ [12, 40],
                 [9, 29],
                 [6, 6],
                 [3, 2]]

objetsTest02 = [[18,60],
                [9, 28],
                [6, 16],
                [3, 7]]

print(sacAdos_v1(objetsTest01, 30))