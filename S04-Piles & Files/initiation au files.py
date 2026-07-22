class File:
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
    
    def enfiler(self, val):
        self.memFile.append(val)
        self.cpt += 1

    def defiler(self):
        self.cpt -= 1
        return self.memFile.pop(0)
    
    def __str__(self):
        return str(self.memFile)
    

class Tampon:
    def __init__(self, tailleMaxi = 100):
        self.fileInterne = File()
        self.tMax = tailleMaxi

    def enfiler(self, val):
        self.fileInterne.enfiler(val)
    def defiler(self):
        return self.fileInterne.defiler()
    def taille(self):
        return self.fileInterne.taille()
    def vide(self):
        return self.fileInterne.vide()
    def __str__(self):
        return str(self.fileInterne)
        

# Instanciation d'un objet Tampon :
tamponTest = Tampon(5)

#ajout des valeurs de test :
for i in range(5):
    tamponTest.enfiler(i)

print(tamponTest)

tamponTest.enfiler(5)
tamponTest.enfiler(6)

print(tamponTest)

    
# Instance d'un objet file :
print("Instance d'une fille \"fileTest\"")
fileTest = File()

# Vérification méthode vide :
print("Le statut vide de la file est :", fileTest.vide())

# Vérification de la taille:
print("La file contient :", fileTest.taille(), "élément(s)).")

N = 10

# Peuplement avec une série numérique croissante :
for i in range(N):
    fileTest.enfiler(i)

print("Contenu de la liste ; ", fileTest.memFile)

# Vérification méthode vide :
print("Le statut vide de la file est :", fileTest.vide())

# Vérification de la taille:
print("La file contient :", fileTest.taille(), "élément(s)).")

# Vérification de l'ordre PEPS/FIFO

print(fileTest)

erreur = False
for i in range(N):
    if i != fileTest.defiler():
        erreur = True
if erreur:
    print("Erreur sur les données restituées !")
else:
    print("L'ensemble des données sont restituées selon l'ordre PEPS.")

