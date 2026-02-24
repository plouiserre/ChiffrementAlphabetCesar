import os 
from Chiffrement import Chiffrement
from Dechiffrement import Dechiffrement

########################################Récupération mots dictionnaire####################################################


def __dictionnaire_dans_tableau(contenu_fichier):
    mots = contenu_fichier.split("\n")
    return mots

base_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(base_dir, "donnees\\dico_fr.txt")
with open(file, "r", encoding="latin1") as f:
    contenu_fichier = f.read()
    mots = __dictionnaire_dans_tableau(contenu_fichier)

 ########################################Récupération mots dictionnaire####################################################
 
chiffrement = Chiffrement()
dechiffrement = Dechiffrement(mots)
phrase_globale = "L’année 1866 fut marquée par un événement bizarre, un phénomène inexpliqué et inexplicable que personne n’a sans doute oublié"

########################################Chiffrement Déchiffrement Avec clé####################################################

mot_a_chiffrer = "Hacker"
print("Voici le mot à chiffrer : "+mot_a_chiffrer)
mot_chiffre = chiffrement.chiffre_texte(mot_a_chiffrer, 6)
print("Voici "+mot_a_chiffrer+" chiffré avec une clé de 6 "+ mot_chiffre)
print("Maintenant on va déchiffrer "+mot_chiffre)
mot_dechiffrer = dechiffrement.dechiffrer_avec_cle(mot_chiffre, 6)
print("Voici le mot final "+mot_dechiffrer)


########################################Chiffrement Déchiffrement Avec clé####################################################

phrase_chiffre = chiffrement.chiffre_texte(phrase_globale, 6)
print("Voici la phrase chiffrée: "+phrase_chiffre)

########################################Chiffrement Déchiffrement Par bruteforce####################################################
phrase_dechiffre_bruteforce = dechiffrement.dechiffrer_sans_clefs_avec_espaces(phrase_chiffre)
print("Voici la phrase déchiffrée par bruteforce: "+phrase_dechiffre_bruteforce)

########################################Chiffrement Déchiffrement Par bruteforce####################################################

########################################Chiffrement Déchiffrement Par Fréquence####################################################
phrase_dechiffre_frequence = dechiffrement.dechiffrer_avec_frequences(phrase_chiffre)
print("Voici la phrase déchiffrée par fréquence: "+phrase_dechiffre_frequence)


########################################Chiffrement Déchiffrement Par Fréquence####################################################
