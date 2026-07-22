def est_present_bmh(motif: str, texte: str) -> bool :
    """Recherche la 1er occurrence du motif dans texte.
    Retourne true si le motif est présent et false en cas d'absence."""
    
    # Construction du dictionnaire de décalage :
    # A pour clé les lettres du motifs et pour valeur les
    # position relatives des lettres du motif par rapport à la dernière.
    # Remarque : Si une lettre apparait plusieurs fois, on appliquera la distance la plus courte
    dico_deca = {}
    i_fin_motif = len(motif) - 1
    for i in range(.....): #On exclut la dernière lettre
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
            i += dico_deca[....]
        else:
            i += ....
            
    return present