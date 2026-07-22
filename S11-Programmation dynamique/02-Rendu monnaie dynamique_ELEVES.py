from math import inf # Importation de la valeur infini.


def renduDynamique(somme, listeValeursFaciales):
    """Fonction récursive retournant le nombre minimal/optimal de billets/pièces contenu dans listeValeursFaciales,
       pour la somme donnée en 1er argument."""
    
    # Création et initialisation du tableau de mémorisation des sous-rendus :
    tabRendus = [0] * (somme + 1)
    
    # Boucle de calcul des différents sous-rendus :
    for sousRendu in range(1, somme + 1):
        # Boucle de recherche du sous rendu optimal :
        mini = inf
        for valeur in listeValeursFaciales:
            if valeur <= sousRendu:
                if ():
                  
                  
        tabRendus[sousRendu] = 
                
    # On retourne la ligne du rendu optimal de la somme étudiée :            
    return tabRendus[somme]

# Exemples :
# ----------
Sn = [5, 2, 1]
somme = 8
print("Pour donner/rendre " + str(somme) + " € il faut " + str(renduDynamique(somme, Sn)) + " billets/pièces.")

Sn = [5, 3, 2]
somme = 7
print("Pour donner/rendre " + str(somme) + " € il faut " + str(renduDynamique(somme, Sn)) + " billets/pièces.")

Sn = [4, 3, 2]
somme = 9
print("Pour donner/rendre " + str(somme) + " € il faut " + str(renduDynamique(somme, Sn)) + " billets/pièces.")

Sn = [6, 4, 2]
somme = 13
print("Pour donner/rendre " + str(somme) + " € il faut " + str(renduDynamique(somme, Sn)) + " billets/pièces.")

