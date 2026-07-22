# ---------------------------------------------
# Module d'affichage de la liste des contacts :
# ---------------------------------------------



DIM_TAB_CONTACTS = [7, 18, 18, 16, 16] #Définie la largeur des colonnes du tableau d'affichage
                                       #des contacts sans compter les chaînes "| " et " |" de
                                       #début et de fin.


contacts=[\
    ["Titre", "Nom", "Prénom", "N° mobile", "N° fixe"],\
    ["M.", "Barack", "Obama", "+33700000001", "+33900000001"],\
    ["M.", "George W.", "Bush",  "+33700000002", "+33900000002"],\
    ["M.", "Bill", "Clinton",  "+33700000003", "+33900000003"],\
    ["M.", "George H.W.", "Bush", "+33700000004", "+33900000004"],\
    ["M.", "Ronald W.", "Reagan", "+33700000005", "+33900000005"],\
    ["M.", "Jimmy", "Carter", "+33700000006", "+33900000006"],\
    ["M.", "Gerald R.", "Ford", "+33700000007", "+33900000007"],\
    ["M.", "Jimmy", "Carter", "+33700000008", "+33900000008"],\
    ["M.", "Richard M.", "Nixon", "+33700000009", "+33900000009"],\
    ["M.", "Lyndon B.", "Johnson", "+33700000010", "+33900000010"],\
    ["M.", "John F.", "Kennedy", "+33700000011", "+33900000011"],\
    ] #Fin liste des contacts

def titrePage():
    print("""

----------------------------------
LISTE DES CONTACTS DU REPERTOIRE :
----------------------------------


""")


def formaterCellule(donnee, largCellule):
    """Fonction qui retourne une chaîne de caractères correspondant à la
    construction d'une cellule du tableau. Les argumments sont la donnée
    affichée (str) et la largeur de cellule désirée"""

    nbrEspacesGauche = (largCellule - len(donnee)) // 2
    nbrEspacesDroit = (...) - nbrEspacesGauche
    chaineCellule = ""
    ... COMPLETER ICI LE CODE PERMETTANT DE COMPLETER LA VARIABLE chaineCellule...

    return chaineCellule


def listerContacts(contacts, dimTabContacts):
    """Fonction affichant tous les contacts de l'agenda sous la forme d'un tableau"""

    titrePage()
    
    # Calcul de la largeur du tableau :
    largeurTab = 0
    for i in dimTabContacts:
        largeurTab = largeurTab + i        

    # Génération de la ligne de séparation de lignes :
    ligne = ""
    for i in range(0, largeurTab + len(dimTabContacts) + 1):
        ligne = ligne + "-"
    
    # Génération des cellules d'une ligne :
    print(ligne)
    for entree in contacts:
        ligneContact = "|" # Chaîne de caractères pour l'affichage d'une ligne du tableau( 1 contact).
        for i in range(0, len(entree)):
            ligneContact = ligneContact + formaterCellule(entree[i], dimTabContacts[i]) + "|" #Concaténation de la ligne

        print(...) # Affichage de la ligne dans la console
        print(...)

    input("\n\nPresser la touche entrée pour revenir au menu précédent...")
   
listerContacts(contacts, DIM_TAB_CONTACTS)
