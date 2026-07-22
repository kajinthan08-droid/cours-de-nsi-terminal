def fusion(l1: [int], l2: [int]) -> [int]:
    """Prend en argument 2 listes d'entiers l1 et l2
    dont les valeurs sont classées dans l'ordre croissant.
    Retourne une liste contenant l'ensemble des valeurs
    de l1 et l2 classées dans l'ordre croissant."""
    
    l_fusion = []
    # Cas où les listes sont vides:
    if len(l1) == 0 and len(l2) == 0:
        return l_fusion
    i1 = 0
    i2 = 0
    # Copie par récupération de la valeur la plus faible dans l1 et l2 :
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            l_fusion.append(l1[i1])
            i1 += 1
        else:
            l_fusion.append(l2[i2])
            i2 += 1
            
    # Copie de la/des valeur(s) restant(es) dans la liste qui n'a pas été entièrement parcourue:
    if i1 < len(l1):
        l_fusion += l1[i1:]
    else:
        l_fusion += l2[i2:]
    return l_fusion

assert fusion([1, 3, 5, 6, 9, 10, 11], [2, 4, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "Liste de sortie non triées !"
assert fusion([1, 3, 5, 6, 9, 10, 11], []) == [1, 3, 5, 6, 9, 10, 11], "Liste de sortie non triées !"
assert fusion([], []) == []

def tri_fusion(l: [int]) -> [int]:
    """Prend une liste d'entiers en argument.
    Retourne une liste avec l'ensemble des valeurs
    triées ans l'ordre croissant."""
    
    if len(l) <= 1:
        return l
    else:
        l1 = tri_fusion(l[: len(l) // 2])
        l2 = tri_fusion(l[len(l) // 2 :])
        return fusion(l1, l2)
    
assert tri_fusion([5, 8, 2, 1, 3, 4, 7, 6]) == [1, 2, 3, 4, 5, 6, 7, 8], "Liste de sortie non triées !"
assert tri_fusion([5]) == [5]
assert tri_fusion([]) == []

