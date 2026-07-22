import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier as Knn





df_personne = pd.read_csv("IRIS-dataset.csv")
print(df_iris)


# Sélection des données à afficher :
# ----------------------------------
taille_personne = df_personne["taille"]
masse_personne = df_personne["masse"]
espece = df_iris["species"]


# Ajout du nouvel individu :
# --------------------------
personne_inconnue = {"longueur_pétale": 2.5, "largeur_pétale": 0.75}


# Classification du nouvel individu :
# -----------------------------------
zip_personne = list(zip(longueur_petale, largeur_petale)) # Mise en forme du jeux de données des longueurs et largeurs

k = 3 # Nombre de voisins validant la classification d'un nouveau individu
mode1 = Knn(n_neighbors = k) # Instance d'un modèle

mode1.fit(zip_personne, espece) # Entrainement du modèle

classification = mode1.predict([(personne_inconnue["longueur_pétale"], personne_inconnue["largeur_pétale"])])
print(f"La personne inconnue est classée (avec k={k}) comme : {classification[0]}")






# Affichage avec matplotlib :
# ---------------------------
plt.title("Jeux de données sur les iris")
plt.xlabel("Longueur des pétales")
plt.ylabel("Largeur des pétales")
plt.scatter(longueur_petale[espece =="setosa"], largeur_petale[espece=="setosa"], color="green", label="Setosa")
plt.scatter(longueur_petale[espece =="versicolor"], largeur_petale[espece=="versicolor"], color="blue", label="Versicolor")
plt.scatter(longueur_petale[espece =="virginica"], largeur_petale[espece=="virginica"], color="red", label="Virginica")
plt.scatter(iris_inconnue["longueur_pétale"], iris_inconnue["largeur_pétale"], color = "black", label = "Iris inconnue")
plt.text(3, 0.7, "Iris inconnue :", fontsize = 10)
plt.text(3, 0.5, f"largeur : {iris_inconnue['longueur_pétale']} cm; longueur : {iris_inconnue['largeur_pétale']} cm", fontsize = 10)
plt.text(3, 0.3, f"Pour k = {k} est nclassée dans : {classification[0]}", fontsize = 10)
plt.legend()
plt.show()
