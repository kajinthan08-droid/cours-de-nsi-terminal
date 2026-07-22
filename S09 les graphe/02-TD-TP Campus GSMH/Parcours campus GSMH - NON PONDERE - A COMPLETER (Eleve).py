# -------------------------------------------------------------------------------- 
#  TD : Parcours Pédestre du Domaine Universitaire de Grenoble St Martin d'Hères
# --------------------------------------------------------------------------------


# Description du campus :
# -----------------------

# Pour plus d'informations : https://fr.wikipedia.org/wiki/Domaine_universitaire_de_Grenoble

# Le domaine/campus de la ville de Grenoble est localisé dans une ancienne zone marécageuse de 2 villes limitrophes
# de la ville de Grenoble (Gières et St Martin d'Hères). Ce campus accueil 35 000 étudiants et 3 000 enseignants.
# Sa superfice est de 186 hectares et dispose d'un milieu naturel favorable avec de nombreux arbres (3 000), d'espaces
# verts et la proximité d'élements naturels : le fleuve de l'Isère en bordure et le massif de la Chartreuse à l'horizon
# nord et la chaîne de Beldonne à l'horizon est.
# La présence de 3 tramways permettant un accès aisé au campus, ainsi que la présence de pistes cyclables et sentiers
# incite au déplacements soit pédestres, soit en vélo.

# Un graphe a été élaboré afin de pouvoir de choisir son itinéraire et d'estimer le temps de déplacement soit en vélo
# ou à pied.


# Description du graphe sous la forme d'une liste d'adjacence :
# -------------------------------------------------------------

# Le campus est modélisé sous la forme d'un graphe pondéré et non orienté.
# Nous le décrivons ci-dessous sous la forme d'une liste d'adjacence.

CAMP_GSMD_LSTADJ = {"BUJF": ["PISC", "STAP", "BIOL", "BUDL", "DIDE", "DLST"],
                    "PISC": ["STAP", "BUJF", "DLST", "MUSE"],
                    "STAP": ["BIOL", "BUJF", "PISC"],
                    "BIOL": ["BUDL", "BUJF", "STAP"],
                    "BUDL": ["BIOL", "COND", "PMFR", "BUJF"],
                    "DIDE": ["BUJF", "PMFR", "DLST"],
                    "DLST": ["PISC", "BUJF", "DIDE", "BERL", "MUSE"],
                    "MUSE": ["PISC", "DLST", "BERL", "TAIL"],
                    "COND": ["PMFR", "BUDL"],
                    "PMFR": ["BUDL", "COND", "DIDE"],
                    "BERL": ["MUSE", "DLST", "TAIL"],
                    "TAIL": ["MUSE", "BERL"]}



# Description du graphe sous la forme d'une matrice d'adjacence :
# ---------------------------------------------------------------

# Tableau des étiquettes des sommets :
CAMP_GSMD_ETIQUETTES = ['BUJF', 'PISC', 'STAP', 'BIOL', 'BUDL', 'DIDE', 'DLST', 'MUSE', 'COND', 'PMFR', 'BERL', 'TAIL']

# Matrice d'ajacence :

#                     BUJF | PISC | STAP | BIOL | BUDL | DIDE | DLST | MUSE | COND | PMFR | BERL | TAIL
CAMP_GSMD_MATADJ = [[   0  ,   1  ,   1  ,   1  ,   1  ,   1  ,   1  ,   0  ,   0  ,   0  ,   0  ,   0  ], # BUJF
                    [   1  ,   0  ,   1  ,   0  ,   0  ,   0  ,   1  ,   1  ,   0  ,   0  ,   0  ,   0  ], # PISC
                    [   1  ,   1  ,   0  ,   1  ,   0  ,   0  ,   0  ,   0  ,   0  ,   0  ,   0  ,   0  ], # STAP
                    [   1  ,   0  ,   1  ,   0  ,   1  ,   0  ,   0  ,   0  ,   0  ,   0  ,   0  ,   0  ], # BIOL
                    [   1  ,   0  ,   0  ,   1  ,   0  ,   0  ,   0  ,   0  ,   1  ,   1  ,   0  ,   0  ], # BUDL
                    [   1  ,   0  ,   0  ,   0  ,   0  ,   0  ,   1  ,   0  ,   0  ,   1  ,   0  ,   0  ], # DIDE
                    [   1  ,   1  ,   0  ,   0  ,   0  ,   1  ,   0  ,   1  ,   0  ,   0  ,   1  ,   0  ], # DLST
                    [   0  ,   1  ,   0  ,   0  ,   0  ,   0  ,   1  ,   0  ,   0  ,   0  ,   1  ,   1  ], # MUSE
                    [   0  ,   0  ,   0  ,   0  ,   1  ,   0  ,   0  ,   0  ,   0  ,   1  ,   0  ,   0  ], # COND
                    [   0  ,   0  ,   0  ,   0  ,   1  ,   1  ,   0  ,   0  ,   1  ,   0  ,   0  ,   0  ], # PMFR
                    [   0  ,   0  ,   0  ,   0  ,   0  ,   0  ,   1  ,   1  ,   0  ,   0  ,   0  ,   1  ], # BERL
                    [   0  ,   0  ,   0  ,   0  ,   0  ,   0  ,   0  ,   1  ,   0  ,   0  ,   1  ,   0  ]] # TAIL 



# PARCOURS EN LARGEUR A PARTIR D'UN SOMMET :
# ------------------------------------------

def parcoursLarg(graphe, depart):
    """
    Prend en argument la liste d'adjacence d'un graphe et le sommet de départ.
    Retourne dans une liste les étiquettes des sommets dans l'ordre de leur visite.
    """

    recenses = [...]  # Consigne les sommets recensés et qui seront visités, retour attendu de la fonction et évite les allers/retours ou cycles infinis
    file = [...]      # Consigne les adjacents d'un sommets visité, et seront visité par la suite

    while len(file) != ...:
        sommetEnVisite = file.pop(0)       # On prend le prochain sommet à visiter

        # Boucle de récupération des adjacents du sommet visité :
        for adjacent in graphe[sommetEnVisite]:            
            if ... not in recenses:
                file. ...      # On ajoute dans file l'adjacent s'il n'a pas encore été visité.
                recenses. ...  # On le consigne comme recensé.

    return recenses


# TESTS DE LA FONCTION  parcoursLarg(graphe, depart) :
#-----------------------------------------------------
print("""
      
TESTS DE LA FONCTION parcoursLarg(grahpe, depart) :
---------------------------------------------------
""")

print("Parcours en largeur à partir de BUJF : ", parcoursLarg(CAMP_GSMD_LSTADJ, "BUJF"))
print("Parcours en largeur à partir de TAIL : ", parcoursLarg(CAMP_GSMD_LSTADJ, "TAIL"))
print("Parcours en largeur à partir de COND : ", parcoursLarg(CAMP_GSMD_LSTADJ, "COND"))



# CHEMINS/CHAINES DE MOINDRES D'ETAPES :
# --------------------------------------

# Le parcours en largeur détermine naturellement les chemins/chaines minimisant le nombre d'étapes.
# Nous allons donc reprendre la fonction parcoursLarg() et remplacer la liste des sommets recensés
# par un dictionnaire des prédécesseurs pour pouvoir déterminer ces chemins/chaînes au moyen d'une
# seconde fonctions dédiée à cette tâche.


def predecesseurs(graphe, depart):
    """
    Prend en argument la liste d'adjacence d'un graphe et le sommet de départ.
    Retourne le dictionnaire des prédécesseurs.
    """
    dicoPredecesseurs = {...}			# Dictionnaire des prédesseurs du graphe pour le départ donné en argument   
    file = [...]                        # Consigne les adjacents d'un sommets visité, et seront visité par la suite

    while len(file) != ...:
        sommetEnVisite = file.pop(0)     # On prend le prochain sommet à visiter        

        # Boucle de récupération des adjacents du sommet visité :
        for adjacent in graphe[sommetEnVisite]:            
            if ... not in dicoPredecesseurs:
                file. ...                           # On ajoute dans file l'adjacent s'il n'a pas encore été visité.
                dicoPredecesseurs[...] = ...    # On le consigne comme recensé.


    return dicoPredecesseurs


def chemin(depart, fin, graphe):
    """
    Fonction qui prend en argument :
        Un sommet de départ
        Un sommet de fin
        Le graphe sous forme de liste d'adjacence
    Retourne le chemin dans une liste
    La fonction utilise la fonction predecesseurs()
    """
    dicoPredecesseurs = predecesseurs(graphe, depart)
    chemin = [...]    
    predecesseur = ...

    while predecesseur != ...:
        predecesseur = dicoPredecesseurs[...]
        chemin = [...] + ...

    return chemin


# TESTS DE LA FONCTION : predecesseurs(graphe, depart) :
# ------------------------------------------------------
print("""
      
TEST DE LA FONCTION predecesseurs(graphe, depart) :
---------------------------------------------------
""")

print("Prédesseurs à partir de BUJF : ", predecesseurs(CAMP_GSMD_LSTADJ, "BUJF"))


# TESTS DE LA FONCTION : chemin(depart, fin, graphe) :
# ----------------------------------------------------
print("""
      
TEST DE LA FONCTION : chemin(depart, fin, graphe) :
---------------------------------------------------
""")

print("Chemin pour aller de TAIL à COND : ", chemin("TAIL", "COND", CAMP_GSMD_LSTADJ))
print("Chemin pour aller de STAP à BERL : ", chemin("STAP", "BERL", CAMP_GSMD_LSTADJ))


