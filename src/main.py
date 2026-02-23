import os 

def __dictionnaire_dans_tableau(contenu_fichier):
    mots = contenu_fichier.split("\n")
    return mots

base_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(base_dir, "donnees\\dico_fr.txt")
with open(file, "r", encoding="latin1") as f:
    contenu_fichier = f.read()
    mots = __dictionnaire_dans_tableau(contenu_fichier)
    print(contenu_fichier)

