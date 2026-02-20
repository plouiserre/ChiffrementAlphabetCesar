import unittest
from src.Chiffrement import Chiffrement

class ChiffrementTest(unittest.TestCase):
    def test_chiffrement_mot_simple(self):
        chiffrement = Chiffrement()
        
        mot_chiffre = chiffrement.chiffrer("bonjour", 2)

        self.assertEqual("dqplpwt", mot_chiffre)
