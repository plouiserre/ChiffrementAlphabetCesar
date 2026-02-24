import math

class Dechiffrement:
    def __init__(self, mots):
        self.mots = mots        
        self.alphabet_minuscule = ["a", "à", "â", "b", "c", "ç","d", "e", "é", "è", "ê", "ë", "f", "g", "h", "i", "î", "ï", "j", "k", "l", "m", "n", "o", "ô", "ö", "p", "q", "r", "s", "t", "u",  "ù", "û", "ü", "v", "w", "x", "y", "ÿ", "z"]
        self.alphabet_majuscule = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.signs_ok = [".", "!", "-", ",", "’", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def dechiffrer_avec_cle(self, mot_chiffre, cle):
        mot_dechiffre = self.__dechiffrer_mots(mot_chiffre, cle)
        return mot_dechiffre

    def dechiffrer_sans_clefs_avec_espaces(self, texte):
        delimiter = " "
        mot_dechiffre = ""
        cle = 0
        tous_les_mots_chiffres = texte.split(" ")
        tous_mots_dechiffres = []

        mot_pour_trouver_cle = self.__trouver_mot_pour_deviner_clefs(tous_les_mots_chiffres)
        
        cle = self.__trouver_cle(mot_pour_trouver_cle)

        for mot_chiffre in tous_les_mots_chiffres :
            mot_dechiffre = self.__dechiffrer_mots(mot_chiffre, cle)
            tous_mots_dechiffres.append(mot_dechiffre)
        
        mots_dechiffre_str = delimiter.join(tous_mots_dechiffres)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        return mots_dechiffre_str
    
    def __trouver_mot_pour_deviner_clefs(self, tous_les_mots_chiffres): 
        mot_pour_trouver_cle = ""
        for mot in tous_les_mots_chiffres : 
            if len(mot) > 3 and self.__not_wrong_signs(mot) :
                mot_pour_trouver_cle = mot
                break
        return mot_pour_trouver_cle
    
    def __not_wrong_signs(self, mot):
        is_ok = True 
        for letter in mot :
            if letter in self.signs_ok : 
                is_ok = False
                break
        return is_ok
    
    def dechiffrer_avec_frequences(self, texte):
        delimiter = " "
        frequences = self.compte_frequence_lettre(texte)
        lettre_e_chiffre = self.__trouver_lettre_e(frequences)
        index_e_chiffre = self.alphabet_minuscule.index(lettre_e_chiffre)
        index_e = self.alphabet_minuscule.index("e")
        cle = index_e_chiffre - index_e
        tous_les_mots_chiffres = texte.split(" ")
        tous_mots_dechiffres = []
        for mot_chiffre in tous_les_mots_chiffres :
            mot_dechiffre = self.__dechiffrer_mots(mot_chiffre, cle)
            tous_mots_dechiffres.append(mot_dechiffre)
        
        mots_dechiffre_str = delimiter.join(tous_mots_dechiffres)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        return mots_dechiffre_str
    
    def compte_frequence_lettre(self, texte): 
        comptages = {}
        frequences = {}
        for letter_alphabet in self.alphabet_minuscule : 
            comptages[letter_alphabet] = 0
            for lettre in texte : 
                if letter_alphabet == lettre : 
                    comptages[letter_alphabet] += 1

        for lettre in comptages: 
            frequences[lettre] = round(comptages[lettre] / len(texte) * 100, 2)
        return frequences

    def __trouver_lettre_e(self, frequences): 
        lettre_e_chiffre = max(frequences, key = frequences.get)
        return lettre_e_chiffre
    
    def __trouver_cle(self, mot_chiffre):
        cle = 0
        cle_possible = 0
        while cle_possible < 26 :
            mot_candidat = self.__dechiffrer_mots(mot_chiffre, cle_possible) 
            if  str.lower(mot_candidat) in self.mots :
                cle = cle_possible
                break
            else :
                cle_possible += 1
        return cle

    def __dechiffrer_mots(self, mot_chiffre, cle):
        possible_mot = ""
        for lettre in mot_chiffre :
            if lettre in self.signs_ok : 
                possible_mot += lettre
            elif lettre in self.alphabet_minuscule : 
                possible_mot += self.__trouver_lettre_dechiffrer(self.alphabet_minuscule, lettre, cle, 41)
            else : 
                possible_mot += self.__trouver_lettre_dechiffrer(self.alphabet_majuscule, lettre, cle, 26)
        return possible_mot
    
    def __trouver_lettre_dechiffrer(self, alphabet, lettre, cle, total_lettre) : 
        index = alphabet.index(lettre)
        nouvel_index = (index - cle) % total_lettre 
        nouvelle_lettre = alphabet[nouvel_index]
        return nouvelle_lettre
