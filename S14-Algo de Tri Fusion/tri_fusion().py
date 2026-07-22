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
