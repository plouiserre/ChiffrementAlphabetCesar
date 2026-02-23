import unittest
from src.Dechiffrement import Dechiffrement

class DechiffrementTest(unittest.TestCase):
    def test_dechiffre_mot_text(self):
        texte = "Estvybyastn"
        dechiffrement = Dechiffrement(["abattoir","actuellement", "concombre", "exploration", "hasardeux", "philosophie", "western"])

        mot_dechiffre = dechiffrement.dechiffrer_sans_clefs_avec_espaces(texte)

        self.assertEqual("Philosophie", mot_dechiffre)

    def test_dechiffre_mot_text_avec_accent(self):
        texte = "Sdwlhqdwmûxg"
        dechiffrement = Dechiffrement(["abattoir","actuellement", "concombre", "exploration", "hasardeux", "philosophie", "mathématique", "western"])

        mot_dechiffre = dechiffrement.dechiffrer_sans_clefs_avec_espaces(texte)

        self.assertEqual("Mathématique", mot_dechiffre)

    def test_dechiffre_plusieurs_mots_avec_espaces(self):
        texte = "Vlmpsvsùlmg Sdwlhqdwmûxg Lüdrëdmv"
        dechiffrement = Dechiffrement(["abattoir","actuellement", "concombre", "exploration", "hasardeux", "philosophie", "western"])

        mot_dechiffre = dechiffrement.dechiffrer_sans_clefs_avec_espaces(texte)

        self.assertEqual("Philosophie Mathématique Français", mot_dechiffre)

    def test_dechiffre_deux_phrases(self):
        texte = "Pg vxmv wsr ùiüg. Xgôsmrv-qsm, fx êtwh sèvêxü fg pd Lsüêg!!"
        dechiffrement = Dechiffrement(["abattoir","actuellement", "concombre", "côté", "de", "du", "exploration", "force", "hasardeux", "je", "la",  
                                       "moi", "obscur", "père", "philosophie", "rejoins", "suis", "ton", "western"])

        mot_dechiffre = dechiffrement.dechiffrer_sans_clefs_avec_espaces(texte)

        self.assertEqual("Je suis ton père. Rejoins-moi, du côté obscur de la Force!!", mot_dechiffre)