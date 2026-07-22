# ____________________________________________
#
# IMPLEMENTATION DES ARBRES BINAIRES EN P.O.O.
#         SPECIALITE N.S.I.
# ____________________________________________


# Version : Février 2021
# ---------


# DEFINITION DES CLASSES :
# ------------------------

# Classe noeud :
# --------------
class Noeud:
    """Classe implémentant les noeuds d'un arbre binaire. La classe comporte
        3 attributs :
            - val -> Etiquette associée au noeud.
            - filsGauche -> Référence du noeud fils de gauche, vaut None si inexistant.
            - filsDroit -> Référence du noeud fils de droite, vaut None si inexistant."""


    def __init__(self, val = None, filsG = None, filsD = None):
        """Le constructeur prend en argument :
                - val = Valeur/Etiquette mémorisée par le noeud.
                - filsG = Référence du fils de gauche.
                - filsD = Référence du fils de droite."""
        
        self.val = val
        self.filsGauche = filsG
        self.filsDroit = filsD
        
        
    def afficherPrefixe(self):
        """Méthode affichant les étiquettes du noeud de départ et de ses descendants
            selon l'ordre préfixé."""
        
        print(str(self.val), end = "; ")
        if self.filsGauche != None : self.filsGauche.afficherPrefixe()
        if self.filsDroit != None :  self.filsDroit.afficherPrefixe()
       

    def afficherInfixe(self):
        """Méthode affichant les étiquettes du noeud de départ de ses descedants
            selon l'ordre infixé."""
        
        if self.filsGauche != None: self.filsGauche.afficherInfixe()
        print(str(self.val), end = "; ")
        if self.filsDroit != None: self.filsDroit.afficherInfixe()


    def afficherPostfixe(self):
        """Méthode affichant les étiquettes du noeud de départ de ses descedants
            selon l'ordre postfixé."""
        
        if self.filsGauche != None: self.filsGauche.afficherPostfixe()
        if self.filsDroit != None:  self.filsDroit.afficherPostfixe()
        print(str(self.val), end = "; ")
        
        
    def taille(self, nbNoeuds = 0):
        """Méthode donnant le nombre de descendants à partir du noeud."""
        
        if self.filsGauche != None: nbNoeuds = self.filsGauche.taille(nbNoeuds)
        if self.filsDroit != None:  nbNoeuds = self.filsDroit.taille(nbNoeuds)         
        return nbNoeuds + 1
        
    
    def hauteur(self):
        """Méthode retournant la hauteur de l'arbre, c'est-à-dire calculer/trouver
            le chemin le plus long de l'arbre."""
        
        cheminGauche = 0
        cheminDroit = 0
        
        if self.filsGauche != None: cheminGauche = self.filsGauche.hauteur()
        if self.filsDroit != None:  cheminDroit = self.filsDroit.hauteur()        
        return 1 + max(cheminGauche, cheminDroit)


    def trouver(self, val):
        """Méthode qui cherche une valeur dans un arbre et retourne la référence du noeud
            si la valeur est trouvée et retourne None si la valeur est absente de l'arbre."""
        
        if self.val == val: return self
        retourGauche = None
        retourDroite = None
        if self.filsGauche != None: retourGauche = self.filsGauche.trouver(val)
        if self.filsDroit != None: retourDroite = self.filsDroit.trouver(val)
        if retourGauche != None: return retourGauche
        elif retourDroite != None: return retourDroite
        else : return None


# Classe arbre :
# --------------
class Arbre:
    """Classe implémentant des arbres binaires. Cette classe instancie
        des objets de la classe noeud pour construire son arborescence."""
    
    def __init__(self, racine = None):
        """Le constructeur récupère la référence d'un noeud existant
            pour le prendre comme racine. Si le noeud n'est pas renseigné
            la référence de la racine est mise à None."""
        
        self.racine = racine
        
    def afficherPrefixe(self):
        """Méthode affichant les étiquettes de l'arbre selon l'ordre préfixe."""
        
        if self.racine != None: self.racine.afficherPrefixe()
        else: print("Arbre vide !")


    def afficherInfixe(self):
        """Méthode affichant les étiquettes de l'arbre selon l'ordre infixe."""
        
        if self.racine != None: self.racine.afficherInfixe()
        else: print("Arbre vide !")
        
        
    def afficherPostfixe(self):
        """Méthode affichant les étiquettes de l'arbre selon l'ordre Postfixe."""
        
        if self.racine != None: self.racine.afficherPostfixe()
        else: print("Arbre vide !")
        

    def taille(self):
        """Méthode donnant la taille de l'arbre (nombre de noeuds composant l'arbre)"""
        
        if self.racine != None: return self.racine.taille()
        else: return 0

    
    def hauteur(self):
        """Méthode retournant la hauteur de l'arbre, c'est-à-dire calculer/trouver
            le chemin le plus long de l'arbre."""
        
        if self.racine != None : return self.racine.hauteur()
        else: return 0
       
       
    def trouver(self, val):
        """Méthode qui cherche une valeur dans un arbre et retourne la référence du noeud
            si la valeur est trouvée et retourne None si la valeur est absente de l'arbre."""
        
        if self.racine != None : return self.racine.trouver(val)
        else: return None
        