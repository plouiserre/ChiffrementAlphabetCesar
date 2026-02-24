import unittest
from src.Dechiffrement import Dechiffrement

class DechiffrementTest(unittest.TestCase):
    dics = ["abattoir","actuellement", "concombre", "côté", "de", "du", "exploration", "force", "hasardeux", "je", "la",  
                                       "mathématique", "moi", "obscur", "père", "philosophie", "rejoins", "suis", "ton", "western"]
    
    def test_dechiffre_mot_text_avec_cle(self):
        texte = "Estvybyastn"
        dechiffrement = Dechiffrement(self.dics)

        mot_dechiffre = dechiffrement.dechiffrer_avec_cle(texte, 15)

        self.assertEqual("Philosophie", mot_dechiffre)

    
    def test_dechiffre_mot_text_bruteforce(self):
        texte = "Estvybyastn"
        dechiffrement = Dechiffrement(self.dics)

        mot_dechiffre = dechiffrement.dechiffrer_sans_clefs_avec_espaces(texte)

        self.assertEqual("Philosophie", mot_dechiffre)

    def test_dechiffre_mot_text_avec_accent_bruteforce(self):
        texte = "Sdwlhqdwmûxg"
        dechiffrement = Dechiffrement(self.dics)

        mot_dechiffre = dechiffrement.dechiffrer_sans_clefs_avec_espaces(texte)

        self.assertEqual("Mathématique", mot_dechiffre)

    def test_dechiffre_plusieurs_mots_avec_espaces_bruteforce(self):
        texte = "Vlmpsvsùlmg Sdwlhqdwmûxg Lüdrëdmv"
        dechiffrement = Dechiffrement(self.dics)

        mot_dechiffre = dechiffrement.dechiffrer_sans_clefs_avec_espaces(texte)

        self.assertEqual("Philosophie Mathématique Français", mot_dechiffre)

    def test_dechiffre_deux_phrases_bruteforce(self):
        texte = "Pg vxmv wsr ùiüg. Xgôsmrv-qsm, fx êtwh sèvêxü fg pd Lsüêg!!"
        dechiffrement = Dechiffrement(self.dics)

        mot_dechiffre = dechiffrement.dechiffrer_sans_clefs_avec_espaces(texte)

        self.assertEqual("Je suis ton père. Rejoins-moi, du côté obscur de la Force!!", mot_dechiffre)

    def test_dechiffre_frequence_texte(self):
        texte_chiffre = "U’èuuïî 1866 mzÿ tèxwzïî vèx zu ïbïuîtîuÿ fôéèxxî, zu voïuùtjuî ôuîçvsôwzï îÿ ôuîçvsôgèfsî wzî vîxyùuuî u’è yèuy iùzÿî ùzfsôï. Bèuy vèxsîx iîy xztîzxy wzô ènôÿèôîuÿ sîy vùvzsèÿôùuy iîy vùxÿy îÿ yzxîçgôÿèôîuÿ s’îyvxôÿ vzfsôg ê s’ôuÿïxôîzx iîy gùuÿôuîuÿy, sîy nîuy iî tîx mzxîuÿ vèxÿôgzsôjxîtîuÿ ïtzy. Uîy uïnùgôèuÿy, èxtèÿîzxy, gèvôÿèôuîy iî uèbôxîy, yrôvvîxy îÿ tèyÿîxy iî s’Nzxùvî îÿ iî s’Jtïxôwzî, ùmmôgôîxy iîy tèxôuîy tôsôÿèôxîy iî ÿùzy vèdy, îÿ, èvxjy îzç, sîy nùzbîxuîtîuÿy iîy iôbîxy Nÿèÿy iîy iîzç gùuÿôuîuÿy, yî vxïùggzvjxîuÿ iî gî mèôÿ èz vszy oèzÿ vùôuÿ."
        texte_dechiffre_attendu = "L’année 1866 fut marquée par un événement bizarre, un phénomène inexpliqué et inexplicable que personne n’a sans doute oublié. Sans parler des rumeurs qui agitaient les populations des ports et surexcitaient l’esprit public à l’intérieur des continents, les gens de mer furent particulièrement émus. Les négociants, armateurs, capitaines de navires, skippers et masters de l’Europe et de l’Amérique, officiers des marines militaires de tous pays, et, après eux, les gouvernements des divers Etats des deux continents, se préoccupèrent de ce fait au plus haut point."
        dechiffrement = Dechiffrement(self.dics)

        text_dechiffre = dechiffrement.dechiffrer_avec_frequences(texte_chiffre)

        self.assertEqual(texte_dechiffre_attendu, text_dechiffre)