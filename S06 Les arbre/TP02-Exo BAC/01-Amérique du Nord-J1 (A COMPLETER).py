# Implémentation d'un arbre de compétition :
# ------------------------------------------
class Arb:
    """Implémentation en POO de l'arbre de compétition du sujet"""
    
    def __init__(self, valeur = None, gauche = None, droit = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
 
class Arb_vide:
    
    def __init__(self):
        self.valeur = None
        self.gauche = None
        self.droit  = None

        
# Implémentation des fonctions de traitement :
# --------------------------------------------
def racine(arb):
    return arb.valeur

def gauche(arb):
    return arb.gauche

def droit(arb):
    return arb.droit

def est_vide(arb):
    if arb.valeur == None:
        return True
    else:
        return False


# Instance d'un arbre vide :
# --------------------------
vide = Arb_vide()


# Application à l'arbre A du sujet :
# ----------------------------------
# On note les arbres par a1, a2, an selon un parcours en largeur, la racine est A est a1 le fils de gauche de A et a2 le droit.
# Les feuilles :
a3 = Arb("Joris", vide, vide)
a4 = Arb("Kamel", vide, vide)
a5 = Arb("Carine", vide, vide)
a6 = Arb("Abdou", vide, vide)

# Sous-arbres :
a1 = Arb(a4.valeur, a3, a4)
a2 = Arb(a5.valeur, a5, a6)

# Racine :
A = Arb(a1.valeur, a1, a2)


# Application à l'arbre B du sujet :
# ----------------------------------
# Les feuilles (niveau 4) :
b7 = Arb("Marc", vide, vide)
b8 = Arb("Lea", vide, vide)

b9 = Arb("Claire", vide, vide)
b10 = Arb("Theo", vide, vide)

b11 = Arb("Marie", vide, vide)
b12 = Arb("Louis", vide, vide)

b13 = Arb("Anne", vide, vide)
b14 = Arb("Kevin", vide, vide)


# Sous-arbres niveau 3 :
b3 = Arb(b8.valeur, b7, b8)
b4 = Arb(b10.valeur, b9, b10)

b5 = Arb(b12.valeur, b11, b12)
b6 = Arb(b13.valeur, b13, b14)


# Sous-arbres niveau 2 :
b1 = Arb(b3.valeur, b3, b4)
b2 = Arb(b5.valeur, b5, b6)

# Racine (niveau 1) :
B = Arb(b1.valeur, b1, b2)


# Test des fonctions initiales :
# ------------------------------

print("\nTests sur l'arbre A des fonctions initiales :\n"
      "---------------------------------------------")
print("Racine de A :", racine(A))
print("Gauche de A :", gauche(A).valeur)
print("Droit de A :", droit(A).valeur)
print("Arbre A vide ? :", est_vide(A))

print("\nTests sur l'arbre B des fonctions initiales :\n"
      "---------------------------------------------")
print("Racine de B :", racine(B))
print("Gauche de B :", gauche(B).valeur)
print("Droit de B :", droit(B).valeur)
print("Arbre B vide ? :", est_vide(B))


# Fonctions des questions :
# -------------------------
def vainqueur(arb):
    return racine(arb)

print("\nTests des fonctions des questions :\n"
      "-----------------------------------\n")
print("Test vainqueur(A) :", vainqueur(A))
print("Test vainqueur(B) :", vainqueur(B))


def finale(arb):
    pass


print("finale(A) :", finale(A))
print("finale(B) :", finale(B))


def occurrences(arb, nom): 
    pass
        
        
print("Nombre d'occurrences de Kamel dans A :", occurrences(A, "Kamel"))
print("Nombre d'occurrences de Abdou dans A :", occurrences(A, "Abdou"))
print("Nombre d'occurrences de Lea dans B :", occurrences(B, "Lea"))
print("Nombre d'occurrences d'Anne dans B :", occurrences(B, "Anne"))

def a_gagne(arb, nom):    
    pass

print("Louis a-t-il gagné dans B ? :", a_gagne(B, "Louis"))
print("Marc a-t-il gagné dans B ? :", a_gagne(B, "Marc"))


def nombre_matchs(arb, nom):
    """arbre_competition, str -> int"""
    pass

print("Nombre de matchs de Lea :", nombre_matchs(B, "Lea"))
print("Nombre de matchs de Marc :", nombre_matchs(B, "Marc"))


def liste_joueurs(arb):
    """arbre_competition -> tableau"""
    pass

print("Liste des joueurs de l'arbre A :", liste_joueurs(A))    
print("Liste des joueurs de l'arbre B :", liste_joueurs(B))   
    
