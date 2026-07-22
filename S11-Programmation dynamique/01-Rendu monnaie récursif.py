from math import inf # Importation de la valeur infini.

def renduRecursif(somme, listeValeursFaciales):
    """Fonction récursive retournant le nombre minimal/optimal de billets/pièces contenu dans listeValeursFaciales,
       pour la somme donnée en 1er argument."""
    
    # Condition de sortie de la récursivité, on s'arrête de rendre, quand la somme à rendre devien nulle :
    if somme == 0:
        return 0 
    
    # Cycle récursif de recherche du nombre de pièces/billets à rendre :
    mini = inf # Cette variable retient le nombre mini de pièces à retourner par la/les combinaisons optimale(s).
    
    for valeur in listeValeursFaciales:
        # On ne sélectionne que les valeurs inférieures à la somme à rendre
        # Par exemple on n'utilise pas 5€ pour rendre une somme de 3€ !
        if valeur <= somme:
            nbrPieces = 1 + renduRecursif( (somme - valeur), listeValeursFaciales )
            if mini > nbrPieces:
                mini = nbrPieces
    return mini

# Exemple :
# ---------
Sn = [5, 2, 1]
somme = 8
print("Pour donner/rendre " + str(somme) + " € il faut " + str(renduRecursif(somme, Sn)) + " billets/pièces.")