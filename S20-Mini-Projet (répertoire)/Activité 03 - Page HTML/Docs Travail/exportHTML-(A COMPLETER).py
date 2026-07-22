# ------------------------------------------------------------
# Module d'expotation de la liste de conctact au format HTML :
# ------------------------------------------------------------

# Description :
# -------------
# Module contenant la fonction réalisant l'export de la liste des contacts
# dans un fichier au format HTML.

from listeContacts import contacts # Liste préremplie pour le développement du programme
import codecs # Module pour l'export au format utf-8

def exporterVersHTML(listeContacts, nomFichier):
    """Fonction assurant la sauvegarde de la base dans un fichier dont le nom
    est donnée en argument au format HTML."""

    pageHTML = codecs.open(nomFichier, "w", "utf-8")

    # Génération du code statique en amont tableau :
    pageHTML.write("""
<!DOCTYPE html>
<html>
    <head>
        <!-- En-tête de la page -->
        <meta charset = "utf-8" />
        <link rel = "stylesheet" href = "styleHTML.css" />
        <title>Répertoire des Contacts</title>
    </head>

    <body>
        <h1>REPERTOIRE</h1>
        <h2>Liste des contacts du répertoire :</h2>
        
        <table>
""")


    # Génération du tableau :
    codeHTML =""
    # TAPER ICI VOTRE CODE PERMETTANT DE GENERER LE TABLEAU D'AFFICHAGE DES CONTACTS.

    pageHTML.write(codeHTML)

    # Génération du code statique en aval du tableau :
    pageHTML.write("""        </table>
        
    
    </body>

</html>""")    
    
    pageHTML.close()


# Test de la fonction :
exporterVersHTML(contacts, "listeDesContacts.html")

    
    
    
