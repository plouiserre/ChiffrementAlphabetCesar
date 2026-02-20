import os 

base_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(base_dir, "donnees\\dico_fr.txt")
with open(file, "r", encoding="latin1") as f:
    contenu_fichier = f.read()
    print(contenu_fichier)
