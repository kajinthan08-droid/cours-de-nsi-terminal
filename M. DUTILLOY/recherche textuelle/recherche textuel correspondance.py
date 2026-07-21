"""def correspondance(texte, motif, p, i):
    for j in range(p):
        if(motif[j] == texte[i+j]):
            ok = True
        else:
            return(False,1)
    return (ok, -1)"""

def correspondance(texte, motif, longeurMoitf, position):
    indice = 0
    trouve = True
    decalage = 0
    
    while(indice < longeurMotif and trouve == True):
        if texte[position + indice] == motif[indice]:
            trouve = True
            indice = indice + 1
        else :
            trouve = False
            decalage = 1
    return (trouve,decalage)


def recherche (texte, motif):
    indexTexte = 0
    while indexTexte + len(motif) <= len(texte):
        correspondance(texte ,motif , len(motif), indexTexte)
    