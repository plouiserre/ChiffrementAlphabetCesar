import unittest
from src.Chiffrement import Chiffrement

class ChiffrementTest(unittest.TestCase):
    def test_chiffrement_mot_cle_simple(self):
        chiffrement = Chiffrement()
        
        mot_chiffre = chiffrement.chiffrer("bonjour", 2)

        self.assertEqual("çöôlöût", mot_chiffre)

    def test_chiffrement_mot_cle_complexe(self):
        chiffrement = Chiffrement()
        
        mot_chiffre = chiffrement.chiffrer("bonjour", 8)

        self.assertEqual("ëutpuÿw", mot_chiffre)


    def test_chiffrement_deux_mots_cle_simple(self):
        chiffrement = Chiffrement()
        
        mot_chiffre = chiffrement.chiffrer("bonjour madame", 2)

        self.assertEqual("çöôlöût oâéâoè", mot_chiffre)

    
    def test_chiffrement_majuscule(self):
        chiffrement = Chiffrement()

        mot_chiffre = chiffrement.chiffrer("Bonjour", 2)

        self.assertEqual("Döôlöût", mot_chiffre)


    def test_lol(self): 
        chiffrement = Chiffrement()

        mot_chiffre = chiffrement.chiffrer("Je", 6)
        mot_chiffre1 = chiffrement.chiffrer("suis", 6)
        mot_chiffre2 = chiffrement.chiffrer("ton", 6)
        mot_chiffre3 = chiffrement.chiffrer("père", 6)
        mot_chiffre4 = chiffrement.chiffrer("Rejoins", 6)
        mot_chiffre5 = chiffrement.chiffrer("moi", 6)
        mot_chiffre6 = chiffrement.chiffrer("du", 6)
        mot_chiffre7 = chiffrement.chiffrer("côté", 6)
        mot_chiffre8 = chiffrement.chiffrer("obscur", 6)
        mot_chiffre9 = chiffrement.chiffrer("de", 6)
        mot_chiffre10 = chiffrement.chiffrer("la", 6)
        mot_chiffre11 = chiffrement.chiffrer("Force", 6)

        self.assertEqual(2, 1)