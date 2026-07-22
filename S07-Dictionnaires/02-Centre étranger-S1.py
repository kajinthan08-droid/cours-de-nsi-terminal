# Table de données du sujet :
# ---------------------------
flotte = {
    12: {"type": "electrique", "etat": 1, "station": "Prefecture"},
    80: {"type": "classique", "etat": 0, "station": "Saint-Leu"},
    45: {"type": "classique", "etat": 1, "station": "Baraban"},
    41: {"type": "classique", "etat": -1, "station": "Citadelle"},
    26: {"type": "classique", "etat": 1, "station": "Coliseum"},
    28: {"type": "electrique", "etat": 0, "station": "Coliseum"},
    74: {"type": "electrique", "etat": 1, "station": "Jacobins"},
    13: {"type": "classique", "etat": 0, "station": "Citadelle"},
    83: {"type": "classique", "etat": -1, "station": "Saint-Leu"},
    22: {"type": "electrique", "etat": -1, "station": "Joffre"},
    }


# Question 1 :
# ------------
# 1.a :
print("flotte[26]:", flotte[26])

# 1.b
print("flotte[80][\"etat\"]:", flotte[80]["etat"])

# 1.c
#print("flotte[99][\"etat\"]:", flotte[99]["etat"])


# Question 3a :
# -------------

# Rappel, dans l'énnoncé flotte est une variable globale
# On n'a donc pas besoin de la donner en argument des fonctions.
def disponible(station):
    pass
            
disponible("Citadelle")


# Question 3b :
# -------------

def rescencer(cat):
    pass
    
rescencer("electrique")

# Question 4 :
# ------------
def localiser(gpsUtilisateur):
    pass


