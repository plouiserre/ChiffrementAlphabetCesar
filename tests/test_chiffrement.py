import unittest
from src.Chiffrement import Chiffrement

class ChiffrementTest(unittest.TestCase):
    def test_chiffrement_mot_cle_simple(self):
        chiffrement = Chiffrement()
        
        mot_chiffre = chiffrement.chiffrer("bonjour", 2)

        self.assertEqual("dqplqwt", mot_chiffre)

    def test_chiffrement_mot_cle_complexe(self):
        chiffrement = Chiffrement()
        
        mot_chiffre = chiffrement.chiffrer("bonjour", 8)

        self.assertEqual("jwvrwcz", mot_chiffre)


    def test_chiffrement_deux_mots_cle_simple(self):
        chiffrement = Chiffrement()
        
        mot_chiffre = chiffrement.chiffrer("bonjour madame", 2)

        self.assertEqual("dqplqwt ocfcog", mot_chiffre)

    
    def test_chiffrement_majuscule(self):
        chiffrement = Chiffrement()

        mot_chiffre = chiffrement.chiffrer("Bonjour", 2)

        self.assertEqual("Dqplqwt", mot_chiffre)