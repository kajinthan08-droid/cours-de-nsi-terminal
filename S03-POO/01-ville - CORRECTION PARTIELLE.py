
# ------------------------
# DEFINITION DES CLASSES :
# ------------------------

# Classe Ville :
# --------------
class Ville:
    
    def __init__(self, nom, codePostal = "NO DATA",  nbrHab = 0, superficie = 0, pays = "France", ):
        self.nomVille = nom
        self.pays = pays
        self.codePostal = codePostal
        self.region = "NO DATA"
        self.departement = "NO DATA"
        self.nbrHabitants = nbrHab
        self.superficie = superficie
        self.coordGPS = "NO DATA"

    def densite(self):
        return self.nbrHabitants / self.superficie
       
    #def presentation(self):
    def __str__(self):
        texte = ("Nom : " + self.nomVille + "\n"
                 "Pays : " + self.pays + "\n"
                 "Code postal : " + self.codePostal + "\n"
                 "Region : " + self.region + "\n"
                 "Département : " + self.departement + "\n"
                 "Nombre d'habitant : " + str(self.nbrHabitants) + "\n"
                 "Superficie : " + str(self.superficie) + " km²\n"
                "Densité population : " + str(self.densite()) + " hab/km²\n"
                 "Coordonnées GPS : " + str(self.coordGPS) + "\n")

        return texte

    # RAJOUTER ICI : joindreInterco(self, interco)

        
        

# Classe Interco :
# ----------------

class Interco:
    
    def __init__(self, nom, region = None, departement = None, date = None, pays = "France"):
        self.nom = nom
        self.pays = pays
        self.region = region
        self.departement = departement
        self.dateCreation = date
        self.listeVilles = []

    def __str__(self):
        texte = ("Nom : " + self.nom + "\n"
                 "Pays : " + self.pays + "\n"
                 "Region : " + self.region + "\n"
                 "Département : " + self.departement + "\n"
                 "Date création : " + self.dateCreation)

        return texte
    
    def listeNomVilles(self):
        # A FAIRE
        pass

    def nbrHabitants(self):
        # A FAIRE
        pass
            
        return sommeHabitants
    
    def densiteHab(self):
        # A FAIRE
        pass


# ---------------------------
# INSTANCIATIONS DES OBJETS :
# ---------------------------


# Ville Python City pour test :
# -----------------------------
"""
pythonCity = Ville("Python City")

pythonCity.codePostal = "99 999"
pythonCity.region = "Python State"
pythonCity.departement = "Python Land"
pythonCity.nbrHabitants = 5000
pythonCity.superficie = 10
pythonCity.coordGPS = (29, 57, 'N', 90, 5, 'O')

print("Nom :", pythonCity.nomVille)
print("Pays :", pythonCity.pays)
print("Code postal :", pythonCity.codePostal)
print("Région : ", pythonCity.region)
print("Département : ", pythonCity.departement)
print("Nombre d'habitants :", pythonCity.nbrHabitants)
print("Superificie :", pythonCity.superficie)
print("Coordonnées GPS :", pythonCity.coordGPS)
"""

#print(pythonCity.presentation())
#print(pythonCity)


# Villes de l'interco de Melun Val de Seine :
# -------------------------------------------


boissettes = Ville("Boissettes", "77350", 401, 1.54)
boissiseLaBertrand = Ville("Boissise La Bertrand", "77350", 1150, 7.8)
boissiseLeRoi = Ville("Boissise Le Roi", "77310", 3775, 7.09)
dammarieLesLys = Ville("Dammarie Les Lys", "77190", 21835, 10.24)
laRochette = Ville("La Rochette", "77000", 3412, 5.85)
leMeeSurSeine = Ville("Le Mée sur Seine", "77350", 20816, 5,34)
limogesFourches = Ville("Limoges Fourches", "77550", 490, 7,96)
lissy = Ville("Lissy", "77550", 230, 6.85)
livrySurSeine = Ville("Livry sur Seine", "77000", 2076, 4.97)
maincy = Ville("Maincy", "77950", 1732, 10,19)
melun = Ville("Melun", "77000", 40032, 8.04)
montereauSurLeJard = Ville("Montereau sur le Jard", "77950", 516, 11,29)
pringy = Ville("Pringy", "77310", 2924, 4.1)
rubelles = Ville("Rubelles", "77950", 2355, 3.91)
stFargeauxPonthierry = Ville("Saint Fargeau Ponthierry", "77310", 14206, 16.57)
stGermainLaxis = Ville("Saint Germain Laxis", "77950", 743, 7.18)
seinePort = Ville("Seine Port", "77240", 1888, 8.53)
vauxLePenil = Ville("Vaux-le-Pénil", "77000", 11062, 10.76)
villiersEnBiere = Ville("Villiers en Bière", "77190", 211, 10,76)
voisenon = Ville("Voisenon", "77950", 1133, 3.36)

print(lissy)


# Instance de l'interco de Melun Val de Seine :
# ---------------------------------------------

melunValDeSeine = Interco("Melun Val de Seine", "Ile de France", "Seine et Marne","01/01/2002")
print(melunValDeSeine)


# Intégration des villes à l'interco :
# ------------------------------------
# boissettes.joindreInterco(melunValDeSeine)
# boissiseLaBertrand.joindreInterco(melunValDeSeine)
# boissiseLeRoi.joindreInterco(melunValDeSeine)
# dammarieLesLys.joindreInterco(melunValDeSeine)
# laRochette.joindreInterco(melunValDeSeine)
# leMeeSurSeine.joindreInterco(melunValDeSeine)
# limogesFourches.joindreInterco(melunValDeSeine)
# lissy.joindreInterco(melunValDeSeine)
# livrySurSeine.joindreInterco(melunValDeSeine)
# maincy.joindreInterco(melunValDeSeine)
# melun.joindreInterco(melunValDeSeine)
# montereauSurLeJard.joindreInterco(melunValDeSeine)
# pringy.joindreInterco(melunValDeSeine)
# rubelles.joindreInterco(melunValDeSeine)
# stFargeauxPonthierry.joindreInterco(melunValDeSeine)
# stGermainLaxis.joindreInterco(melunValDeSeine)
# seinePort.joindreInterco(melunValDeSeine)
# vauxLePenil.joindreInterco(melunValDeSeine)
# villiersEnBiere.joindreInterco(melunValDeSeine)
# voisenon.joindreInterco(melunValDeSeine)


#print(melunValDeSeine.listeVilles[0].nomVille)

#print(melunValDeSeine.listeNomVilles())

#print("Nombre total d'habitants sur Melun Val de Seine :", melunValDeSeine.nbrHabitants())




