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

    def test_chiffrement_gros_texte(self):
        chiffrement = Chiffrement()

        texte_chiffre = chiffrement.chiffrer("L’année 1866 fut marquée par un événement bizarre, un phénomène inexpliqué et inexplicable que personne n’a sans doute oublié. Sans parler des rumeurs qui agitaient les populations des ports et surexcitaient l’esprit public à l’intérieur des continents, les gens de mer furent particulièrement émus. Les négociants, armateurs, capitaines de navires, skippers et masters de l’Europe et de l’Amérique, officiers des marines militaires de tous pays, et, après eux, les gouvernements des divers Etats des deux continents, se préoccupèrent de ce fait au plus haut point.", 9)

        self.assertEqual("U’èuuïî 1866 mzÿ tèxwzïî vèx zu ïbïuîtîuÿ fôéèxxî, zu voïuùtjuî ôuîçvsôwzï îÿ ôuîçvsôgèfsî wzî vîxyùuuî u’è yèuy iùzÿî ùzfsôï. Bèuy vèxsîx iîy xztîzxy wzô ènôÿèôîuÿ sîy vùvzsèÿôùuy iîy vùxÿy îÿ yzxîçgôÿèôîuÿ s’îyvxôÿ vzfsôg ê s’ôuÿïxôîzx iîy gùuÿôuîuÿy, sîy nîuy iî tîx mzxîuÿ vèxÿôgzsôjxîtîuÿ ïtzy. Uîy uïnùgôèuÿy, èxtèÿîzxy, gèvôÿèôuîy iî uèbôxîy, yrôvvîxy îÿ tèyÿîxy iî s’Nzxùvî îÿ iî s’Jtïxôwzî, ùmmôgôîxy iîy tèxôuîy tôsôÿèôxîy iî ÿùzy vèdy, îÿ, èvxjy îzç, sîy nùzbîxuîtîuÿy iîy iôbîxy Nÿèÿy iîy iîzç gùuÿôuîuÿy, yî vxïùggzvjxîuÿ iî gî mèôÿ èz vszy oèzÿ vùôuÿ.", texte_chiffre)