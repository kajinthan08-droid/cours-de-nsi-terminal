from TriFusion import tri_fusion
from random import shuffle
from time import perf_counter
import matplotlib.pyplot as plt


# Génération d'un jeu de test :
#-------------------------------
k = 12
l_tests = []

for i in range(k):
    liste_test = [ j for j in range(int(10**(i / 2)))]
    shuffle(liste_test)
    l_tests.append(liste_test)
    
    
# Exécution chronométrée des tests avec consignation des résultats :
#-------------------------------------------------------------------
nb_val = []
durees = []

for liste_test in l_tests:
    t_deb = perf_counter()
    tri_fusion(liste_test)
    t_fin = perf_counter()
    
    nb_val.append(len(liste_test))
    durees.append(t_fin - t_deb)
    
    
# Tracé de la courbe :
#---------------------
plt.title("Performace de l'algo de tri fusion")
plt.xlabel("Nombre de valeur n")
plt.ylabel("Durée exécution (s)")
plt.plot(nb_val, durees)
plt.show()