#-------------------------------------------------------
# Algorithme naïf de recherche d'un motif dans un texte
#---------------------------------------------------------


# Données de test :
#-------------------
le_ver = "Un ver vert va vers un verre vert à l'envers."

def est_present(motif: str, texte: str) -> bool :
    """ Recherche la 1er occurence du motif dans texte.
    Retourne true si le motif est présen et false en cas d'absence."""
    
    present = False
    
    # Boucle principale : déplacement de la fenêtre de gauche à droite
    i_dep = 0
    i_fin = len(texte) - len(motif)
    
    for i in range(i_dep, i_fin + 1, 1):
        # Boucle secondaire : correspondance du motif sur le fragment de texte
        for j in range (len(motif)):
            if motif[j] != texte[i+j]:
                break # Fin de la boucle" secondaire dès qu'une lettre ne correspond pas
            if j == len(motif) - 1:
                present = True
                return present
    
    return present
# Test :
#-------
print("Test de la fonction est_present() :\n"
      "-----------------------------------")
mot_test = "vert"
print(f'''Le mot "{mot_test}" est présent dans : "{le_ver}" : {est_present(mot_test, le_ver)}''')
mot_test = "verte"
print(f'''Le mot "{mot_test}" est présent dans : "{le_ver}" : {est_present(mot_test, le_ver)}''')


print("\n")


#-------------------------------------------------------
# Algorithme naïf de recherche d'un motif dans un texte
#---------------------------------------------------------


# Données de test :
#-------------------
le_ver = "Un ver vert va vers un verre vert à l'envers."

def est_present_sans_break(motif: str, texte: str) -> bool :
    """ Recherche la 1er occurence du motif dans texte.
    Retourne true si le motif est présen et false en cas d'absence."""
    
    present = False
    
    # Boucle principale : déplacement de la fenêtre de gauche à droite
    i_dep = 0
    i_fin = len(texte) - len(motif)
    
    for i in range(i_dep, i_fin + 1, 1):
        # Boucle secondaire : correspondance du motif sur le fragment de texte
        nb_lettres_identiques = 0
        j = 0
        while nb_lettres_identiques != len(motif) and motif[j] == texte[i + j]:
            nb_lettres_identiques += 1
            j +=1
        if nb_lettres_identiques == len(motif):
            present = True
    return present

# Test :
#-------
print("Test de la fonction est_present() :\n"
      "-----------------------------------")
mot_test = "vert"
print(f'''Le mot "{mot_test}" est présent dans : "{le_ver}" : {est_present(mot_test, le_ver)}''')
mot_test = "verte"
print(f'''Le mot "{mot_test}" est présent dans : "{le_ver}" : {est_present(mot_test, le_ver)}''')




def nb_occurrences(motif: str, texte: str) -> int:
    """Retourne le nombre d'occurrences du motif dans texte."""
    compteur = 0
    i_dep = 0
    i_fin = len(texte) - len(motif)

    for i in range(i_dep, i_fin + 1):
        j = 0
        while j < len(motif) and motif[j] == texte[i + j]:
            j += 1
        if j == len(motif):
            compteur += 1

    return compteur

# Tests :
#--------
print("\n"
      "Tests de la fonction nb_occurrence() :\n"
      "---------------------------------------")
mot_test = "vert"
print(f'''Le mot "{mot_test}" a {nb_occurrences(mot_test, le_ver)} occurence(s) dans : "{le_ver}"''')

def index_occurrences(motif: str, texte: str) -> [int]:
    """Retourne une liste contenant l'index du 1er caractère des occurrences du motif dans texte."""
    liste_index = []
    i_dep = 0
    i_fin = len(texte) - len(motif)

    for i in range(i_dep, i_fin + 1):
        j = 0
        while j < len(motif) and motif[j] == texte[i + j]:
            j += 1
        if j == len(motif):
            liste_index.append(i)

    return liste_index

# Tests:
#-------
print("\n"
      "Tests de la fonction index_occurrences() :\n"
      "------------------------------------------")
mot_test = "vert"
print(f'''Le mot "{mot_test}" a pour liste d'occurrences : {index_occurrences(mot_test, le_ver)}\ndans : "{le_ver}"''')


def est_present_bmh(motif: str, texte: str) -> bool :
    """Recherche la 1er occurrence du motif dans texte.
    Retourne true si le motif est présent et false en cas d'absence."""
    
    # Construction du dictionnaire de décalage :
    # A pour clé les lettres du motifs et pour valeur les
    # position relatives des lettres du motif par rapport à la dernière.
    # Remarque : Si une lettre apparait plusieurs fois, on appliquera la distance la plus courte
    dico_deca = {}
    i_fin_motif = len(motif) - 1
    for i in range(i_fin_motif): #On exclut la dernière lettre
        dico_deca[motif[i]] = i_fin_motif - i
        
    # Boucle de déplacement de la fenêtre de contrôle :
    i_dep_droit = len(motif) - 1
    i_fin_texte = len(texte) - 1
    i = i_dep_droit
    present = False
    
    
    while i <= i_fin_texte and not present:
        # Boucle d'identification du motif dans la fenêtre de texte
        nb_lettres_identiques = 0
        j = len(motif) - 1
        while j >= 0 and motif[j] == texte[i - (len(motif) - 1 - j)]:
            nb_lettres_identiques += 1
            j -= 1
        # On vérifie si le motif à été trouvé :
        if nb_lettres_identiques == len(motif):
            present = True
            
        # Mise à jour de l'index de recherche i
        if texte[i] in dico_deca :
            i += dico_deca[texte[i]]
        else:
            i += len(motif)
            
    return present
print("Tests de la fonction est_present_bmh :\n"
      "----------------------------------------")
mot_test= "vert"
print(f'''Le mot "{mot_test}" est présent dans : "{le_ver}" : {est_present_bmh(mot_test, le_ver)}''')
mot_test = "verte"
print(f'''Le mot "{mot_test}" est présent dans : "{le_ver}" : {est_present_bmh(mot_test, le_ver)}''')

def nb_occurences_bmh(motif: str, texte: str) -> int:
    compteur = 0
    i_dep = 0
    i_fin = len(texte) - len(motif)

    for i in range(i_dep, i_fin + 1):
        j = 0
        while j < len(motif) and motif[j] == texte[i + j]:
            j += 1
        if j == len(motif):
            compteur += 1

    return compteur
# Tests :
#--------
print("\n"
      "Tests de la fonction nb_occurrence() :\n"
      "---------------------------------------")
mot_test = "vert"
print(f'''Le mot "{mot_test}" a {nb_occurrences(mot_test, le_ver)} occurence(s) dans : "{le_ver}"''')

def index_occurrences_bmh(motif: str, texte: str) ->[int]:
    liste_index = []
    i_dep = 0
    i_fin = len(texte) - len(motif)

    for i in range(i_dep, i_fin + 1):
        j = 0
        while j < len(motif) and motif[j] == texte[i + j]:
            j += 1
        if j == len(motif):
            liste_index.append(i)

    return liste_index
# Tests:
#-------
print("\n"
      "Tests de la fonction index_occurrences() :\n"
      "------------------------------------------")
mot_test = "vert"
print(f'''Le mot "{mot_test}" a pour liste d'occurrences : {index_occurrences(mot_test, le_ver)}\ndans : "{le_ver}"''')

