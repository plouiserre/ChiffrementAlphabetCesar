import os 
from Chiffrement import Chiffrement
from Dechiffrement import Dechiffrement

def __dictionnaire_dans_tableau(contenu_fichier):
    mots = contenu_fichier.split("\n")
    return mots

base_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(base_dir, "donnees\\dico_fr.txt")
with open(file, "r", encoding="latin1") as f:
    contenu_fichier = f.read()
    mots = __dictionnaire_dans_tableau(contenu_fichier)

mot_a_chiffrer = "Hacker"

print("Voici le mot à chiffrer : "+mot_a_chiffrer)
chiffrement = Chiffrement()
mot_chiffre = chiffrement.chiffre_texte(mot_a_chiffrer, 6)
print("Voici "+mot_a_chiffrer+" chiffré avec une clé de 6 "+ mot_chiffre)
print("Maintenant on va déchiffrer "+mot_chiffre)
dechiffrement = Dechiffrement(mots)
mot_dechiffrer = dechiffrement.dechiffrer_avec_cle(mot_chiffre, 6)
print("Voici le mot final "+mot_dechiffrer)


