
# Labyrinthes du sujet :
# ----------------------

lab1 = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [2, 0, 1, 0, 0, 0, 1, 0, 1, 0, 3],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]]

lab2 = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 3, 1]]


lab3 = [[1, 1, 1, 1, 1, 1],
        [2, 0, 0, 0, 0, 3],
        [1, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 1]]



# Question 1 :
# ------------

# A faire


# Question 2 :
# ------------

def est_valide(i, j ,n ,m):
    pass
    

print("est_valide(5, 2, 10, 10)", est_valide(5, 2, 10, 10))
print("est_valide(-3, 4, 10, 10)", est_valide(-3, 4, 10, 10))


# Question 3 :
# ------------

def depart(lab):
    n = len(lab)
    m = len(lab[0])
    
    pass

print("Départ lab1:", depart(lab1))


# Question 4 :
# ------------

def nb_cases_vides(lab):
    pass

print("Nombres cases vides de lab2:", nb_cases_vides(lab2))


# Question B.1 :
# --------------

def voisines(i, j, lab):
    pass
    # Réactiver le code en supprimant les """ et compléter
    """
    lstVoisines = []
    
    for k in range(i-1, i+2, 2):
        if est_valide(k, j ,len(lab) ,len(lab[0])) and lab[k][j] not in [1, 4]:
            lstVoisines.append((k, j))
            
    for l in range(j-1, j+2, 2):
        if est_valide(i, l ,len(lab) ,len(lab[0])) and lab[i][l] not in [1, 4]:
            lstVoisines.append((i, l))
        
    return lstVoisines
    """

print("Voisines de i = 7, j = 7, dans lab1:", voisines(7, 7, lab1))



# Question B.2b :
# ---------------

def solution(lab):
    # Réactiver le code en supprimant les """ et compléter
    """
    chemin = [depart(lab)]
    case = chemin[0]
    i = case[0]
    j = case[1]
    """


    
    
# Test de la fonction sur lab1 et lab2 :
print("Tests sur la fonction solution():\n")
print("Solution de lab2:\n", solution(lab2), "\n")
print("Solution de lab1:\n", solution(lab1), "\n") 


