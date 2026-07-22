# ____________________________________________
#
# TRAVAUX PRATIQUES SUR LES ALGORITHMES DE TRI
# ____________________________________________


# Description :
#--------------

# Ce fichier comporte 3 "prototypes" de fonctions :
# - triSelectionHorsPlace(liste)
# - triSelectionEnPlace(liste)
# - triInsertion(liste)

# Le programme principal contient l'appel de 3 fonctions
# permettant de faire des jeux de tests sur les fonctions
# de tri développées.


# IMPORTS :
# ---------

from random import randint


# ---------------------------
# DEFINITIONS DES FONCTIONS :
# ---------------------------

# Fonction de génération d'une liste aléatoire de N entiers :
def createRandList(N):
    """Prend en argument le nombre d'entiers contenus dans la liste.
    La fonction retourne la liste de N entiers quelconques."""
    
    listRand = []
    for i in range(N):
        listRand.append(randint(0, N))
    return listRand


# Fonction de vérification d'une liste triée :
def testSortList(liste):
    """Prend en argument une liste retourne True si la liste est
    triée et False si non triée."""
    
    valPrec = liste[0]
    for val in liste:
        if val < valPrec:
            return False
        valPrec = val
    return True


# Fonction de test multiples :
def multiTest(idFoncTri, tailleListes, nbrTests):
    """Fonction prennant en argument : l'indentifiant de la fonction
    à test : triSelectionHorsPlace, triInsertion, triBulles, etc.
    Le 2e argument est la taille des listes aléatoires à trier et
    le 3ème argument est le nombre de listes à tester.
    La fonction retourne False au 1er échec et True si tous les tests
    réussissent."""
    
    for i in range(nbrTests):
        listeTest = createRandList(tailleListes)
        listeTest = idFoncTri(listeTest)
        if not testSortList(listeTest):
            return False
        
    return True


# Fonction de tri sélection hors place :
def triSelectionHorsPlace(liste):
    """Fonction appliquant le tri par sélection hors place à la
    liste donnée en argument et qui retourne une copie de la liste
    originale triée."""
    
    listeTriee = []
    copyListe = liste[:]
    
    while(len(copyListe) > 0):
        # Recherche de l'indice contenant la valeur minimale de liste :
        iValMin = 0
        # A COMPLETER
        
        # Transfert de la valeur minimale dans la liste triée :
        listeTriee.append(copyListe.pop(iValMin))
 
    return listeTriee


# Fonction de tri sélection en place :
def triSelectionEnPlace(liste):
    """Fonction appliquant le tri par sélection en place à la
    liste donnée en argument et qui retourne une copie de la liste
    originale triée."""
    
    copyListe = liste[:]
    N = len(copyListe)
    
    # Boucle générale (de ... à ...) :

        # Boucle de recherche de la valeur mini (de ... à ...) :

        # Permutation des valeurs :

    
    return copyListe


# Fonction de tri par insertion :
def triInsertion(liste):
    """Fonction appliquant le tri par insertion à la liste donnée en argument
    et qui retourne une copie de la liste originale triée."""
    
    copyListe = liste[:]
    N = len(copyListe)
    
    # Boucle principale (de ... à ...) :

        # Boucle des permutations (de ... à ... ET tant que l'on peut permuter les valeurs voisines):

    
    return copyListe


# BONUS : Fonction de tri à bulles :
def triBulles(liste):
    """Fonction appliquant le tri à bulles sur une copie de la liste donnée en
    argument. La copie de la liste est retournée à la fin du tri."""

    copyListe = liste[:]
    N = len(copyListe)
    
    # A faire
    
    

# ---------------------
# PROGRAMME PRINCIPAL :
# ---------------------

# TEST UNIQUE :
# -------------
testList = createRandList(20)
print("La liste test est :\t\t" + str(testList))
listeTriee = triSelectionHorsPlace(testList)
#listeTriee = triSelectionEnPlace(testList)
#listeTriee = triInsertion(testList)
print("La liste test après le tri :\t" + str(listeTriee))


# TEST MULTIPLE :
# ---------------
print("Multitests : ", multiTest(triSelectionHorsPlace, 50, 1000))


