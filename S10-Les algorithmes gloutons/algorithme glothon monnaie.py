def convMonnaie(Sn, facConv):
    for i in range(len(Sn)):
        Sn[i] = Sn[i] * facConv
  
  
def rendreMonnaie(s, Sn):
    # Conversion des valeurs en centimes (Ceci permet d'éviter les erreurs d'arrondi
    convMonnaie(Sn, 100)
    s = s*100
    
    rendu = [0] * len(Sn)
    reste = s
    Sn.sort(reverse = True) # On tri le système de monnaie dans l'ordre décroissant
    i = 0
    while reste != 0:
        while Sn[i] > reste:
            i = i + 1
            
        reste = reste - Sn[i]
        rendu[i] = rendu[i] + 1
        
    convMonnaie(Sn, 1/100) # Reconversion en euros.
    return rendu


def detailRendu(rendu, Sn):
    print("\nLe rendu est constitué :\n"
          "-------------------------\n")
    for i in range(len(rendu)):
        print(str(rendu[i]) + "\tpièce(s)/billet(s) de :\t" + str(Sn[i]))
        
        
# Exemple :
#----------
        
Sn = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2]
somme = 7.93
print("rendu = " + str(rendreMonnaie(somme, Sn)))
rendu = rendreMonnaie(somme, Sn)
detailRendu(rendu, Sn)