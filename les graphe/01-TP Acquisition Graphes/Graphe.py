# Classe Graphe :
# ---------------

class Graphe:
    """Classe définissant une structure de type graphe. Le réprésentation
    en mémoire est réalisée par un dictionnaire d'adjacence."""
    
    def __init__(self, listAdj = None, matAdj = None, dicAdj = None):
        """Constructeur de la classe Graphe qui prend en argurment une
        liste d'adjacence ou une matrice d'adjacence ou une matrice d'adjancence pour initialiser
        l'objet graphe"""
        
        self.dicAdj = {}
        
        # Construction à partir d'une liste adjacence donnée en argument :
        # --------------------------------------------------------------
        if listAdj != None:
            # Création des clés (Les clés correspondent aux numéros d'indices de ligne de la liste d'adjacence)
            for i in range(len(listAdj)):
                self.dicAdj[i] = [] # On rajoute la clé correspondante au sommet i
                # Ajout des sommets adjacents du sommet i :
                for sommet in listAdj[i]:
                    self.dicAdj[i].append(sommet)
                    
                    
        # Construction à partir d'une matrice adjacence donnée en argument :
        # ------------------------------------------------------------------
        elif matAdj != None:
            # Création des clés (Les clés correspondent aux numéros d'indices de ligne de la matrice d'adjacence)
            for i in range(len(matAdj)):
                self.dicAdj[i] = [] # On rajoute la clé correspondante au sommet :
                for j in range(len(matAdj[i])):
                    if matAdj[i][j] == 1:
                        self.dicAdj[i].append(j)
                    
                    
        # Construction à partir d'un dictionnaire d'adjancence donnée en argument :
        # -------------------------------------------------------------------------
        elif dicAdj != None:
            self.dicAdj = dicAdj
            
    
    
    def __str__(self):
        """Méthode générant l'affichage du graphe sous la forme d'un dictionnaire d'adjacence."""
        
        
        dicoStr = ""
        for cle in self.dicAdj:
            dicoStr = dicoStr + str(cle) + ":" + str(self.dicAdj[cle]) + "\n"
        return dicoStr
                    
                    

    def parcoursLargeur(self, sommetDepart):
        """Parcours du graphe selon un schéma en largeur. La méthode prend en argument le sommet de départ et retourne
        une liste contenant les sommets visités selon l'ordre du parcours"""
        
        # Déclarations :
        # --------------
        file = [sommetDepart]       # Liste qui sera utilisée comme une file en utilisant exclusivement les méthodes append() et pop(0)
        visites = [sommetDepart]    # Liste contenant les sommets visités ou à visiter.
        parcours = []               # Liste contenant les sommets visités selon le parcours imposé par l'algorithme
        
        
        # Exécution du parcours :
        # -----------------------
        
        while(len(file) != 0):
            # Récupération du sommet à traiter
            sommetCourant = file.pop(0)
            parcours.append(sommetCourant)
            
            # Mise en attente dans la file des adjacents du sommetCourant :
            listeAdjacents = self.dicAdj[sommetCourant]
            for adjacent in listeAdjacents:
                # On filtre les sommets déjà visités :
                if adjacent not in visites:
                    file.append(adjacent)
                    visites.append(adjacent)
                    
                    
        return parcours

    def parcoursProfondeur(self, sommetDepart):
        """Parcours du graphe selon un schéma en profondeur. La méthode prend en argument le sommet de départ et retourne
        une liste contenant les sommets visités selon l'ordre du parcours."""
        
        # Déclaration :
        # ------------
        pile = [sommetDepart]       # Liste qui sera utilisée comme une file en utilisant exclusivement les méthodes append() et pop(0)
        visites = [sommetDepart]    # Liste contenant les sommets visités ou à visiter.
        parcours = []               # Liste contenant les sommets visités selon le parcours imposé par l'algorithm
        

        # Exécution du parcours :
        # -----------------------
        
        while(len(pile) != 0):
            # Récupération du sommet à traiter
            sommetCourant = pile.pop(0)
            parcours.append(sommetCourant)
            
            # Mise en attente dans la file des adjacents du sommetCourant :
            listeAdjacents = self.dicAdj[sommetCourant]
           
           
            for i in range(len(listeAdjacents)-1,-1,-1):
                # On filtre les sommets déjà visités :
                if listeAdjacents[i] not in visites:
                    pile.append(listeAdjacents[i])
                    visites.append(listeAdjacents[i])
                    
                    
        return parcours


    def chaîne(self, depart, fin):
        """ Méthode déterminant s'il existe une chaîne entre 2 sommets. Si la chaîne n'existe pas la méthode retourne
        false. Si la chaîne existe, la méthode retourne une liste contenant les sommets constituant la chaîne.
        Pour procédé la méthode réalise un parcours en largeur jusqu'à rencontrer le sommet de fin. Si tout le graphe
        est parcouru sans trouver le sommet de fin, alors la méthode retourne false."""
        
        # Déclarations :
        #---------------
        file = [depart]        # Liste qui sera utilisée comme une file en utilisant exclusivement les méthode append() et pop()
        visites = [depart]     # Liste contenant les sommets visités ou à visiter.
        predecesseurs = {}     # Dictionnaire qui va consigner pour chaque sommet, le sommet dit prédecesseur qui l'a inscrit dans la file.
        chaîne = False
        sommetCourant = None
        
        # Exécution du parcours :
        #------------------------
        while(len(file) != 0 and (fin not in file)):
            
            # Récupération du sommet à traiter
            sommetCourant = file.pop(0)
            
            # Mise en attente dans la file des adjacents du sommetCourant :
            listeAdjacents = self.dicAdj[sommetCourant]
            
            for adjacent in listeAdjacents:
                #on filtre les sommets déjà visités :
                if adjacent not in visites:
                    file.append(adjacent)
                    visites.append(adjacent)
                    predecesseurs[adjacent] = sommetCourant
                    
                # Construction de la chaîne à parir du dictionnaire des predecesseurs:
                if fin in file:
                    curseur = [depart]
                    chaîne = [curseur]
                    while curseur != depart:
                        curseur = predecesseur[adjacent]          #on remonte le chemin de prédecesseur en prédecesseur.
                        chaîne.append(curseur)
                    chaîne.reverse()
                    
                return chaîne



if __name__ == "__main__":
    
    #Import des graphes pour la série de tests :
    from graphes_non_pondérés import *
    
    
    
    print("_____________________________________\n\n"
          "JEUX DE TESTS POUR LA CLASSE GRAPHE :\n"
          "_____________________________________\n\n")
    
    print("Tests des instances de la classe Graphe :\n"
          "-----------------------------------------\n")
    
    # Création d'un graphe vide :
    grapheVide = Graphe()
    print("Le graphe vide est de type : " + str(type(grapheVide)))
    
    # Création d'un graphe à partir d'une liste d'adjacence :
    grapheDeListe = Graphe(listAdj  = listAdjTest)
    
    # Création d'un graphe à partir d'une matrice d'adjacence :
    grapheDeMatrice = Graphe(matAdj = matriTest)
    
    # Création d'un graphe à partir d'un dictionnaire d'adjacence :
    grapheDeDico = Graphe(dicAdj = dicoTest)
    grapheSpider = Graphe(dicAdj = spider)
    
    
    print("\n\nTests de l'affichage d'un graphe :\n"
          "-----------------------------------")
    print(grapheDeListe)
    print(grapheDeMatrice)
    print(grapheDeDico)
    
        
    print("\n\nTests des parcours des graphes :\n"
          "---------------------------------")
    
    # Test des parcours :
    print("\nParcours en largeur sur grapheDeListe : " + str(grapheDeListe.parcoursLargeur(0)))
    print("Parcours en profondeur sur grapheDeListe : " + str(grapheDeListe.parcoursProfondeur(0)))
    
    print("\nParcours en largeur sur grapheDeMatrice : " + str(grapheDeMatrice.parcoursLargeur(0)))
    print("Parcours en profondeur sur grapheDeMatrice : " + str(grapheDeMatrice.parcoursProfondeur(0)))
    
    print("\nParcours en largeur sur  grapheDeListe :" + str(grapheDeDico.parcoursLargeur("a")))    
    print("Parcours en profondeur sur grapheDeDico : " + str(grapheDeDico.parcoursProfondeur("a")))
    
    print("\nParcours en largeur sur grapheSpider : " + str(grapheSpider.parcoursLargeur("a")))
    print("Parcours en profondeur sur grapheSpider : " + str(grapheSpider.parcoursProfondeur("a")))

    print("\n\nTest des chaîne et chemin :\n"
          "-------------------------------")
    grapheNonConnexe = Graphe(dicAdj = nonConnexe)
    depart, fin = "a", "x"
    print("La chaîne entre : " + str(depart) + " et " + str(fin) + " est : " + str(grapheNonConnexe.chaîne(depart, fin)))
    depart, fin = "a", "g"
    print("La chaîne entre : " + str(depart) + " et " + str(fin) + " est : " + str(grapheNonConnexe.chaîne(depart, fin)))
    depart, fin = "a", "h"
    print("La chaîne issue du graphe spider entre : " + str(depart) + " et " + str(fin) + " est : " + str(grapheSpider.chaîne(depart, fin)))