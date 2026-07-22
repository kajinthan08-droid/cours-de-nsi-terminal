class Pile:
    def __init__(self):
        self.memFile = []
        self.cpt = 0
    
    def vide(self):
        if self.cpt == 0:
            return True
        else:
            return False
        
    def taille(self):
        return self.cpt
    
    def enpiler(self, val):
        self.memFile.append(val)
        self.cpt +=1
    
    def depiler(self):
        self.cpt -=1
        return self.memFile.pop(0)
    
    def __str__(self):
        return str(self.memFile)

# Istance d'un objet pile:
print("Istance d'une pile \"pileTest\"")
pileTest = Pile()

# Vérification méthode vide :
print("Le statut vide de la pile est:", pileTest.vide())

# Vérification de la taille :
print("La pile contient :", pileTest.taille(), "éléments(s).")

N = 10
# Peuplement avec une serie numerique croissante :
for i in range(N):
    pileTest.enpiler(i)
    
print("Contenu de la liste :", pileTest.memFile)

# Vérification méthode vide :
print("Le statut vide de la pile est:", pileTest.vide())

# Vérification de la taille :
print("La pile contient :", pileTest.taille(), "éléments(s).")

erreur = False
for i in range(N-1, -1, -1):
    if i != pileTest.depiler():
        erreur = True
if erreur:
    print("Erreur sur les données restituées !")
else:
    print("L'ensemble des données sont restituées selon l'ordre LIFO.")