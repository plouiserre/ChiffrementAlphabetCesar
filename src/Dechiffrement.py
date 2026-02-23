class Dechiffrement:
    def __init__(self, mots):
        self.mots = mots
        self.alphabet_minuscule = ["a", "à", "â", "b", "c", "ç","d", "e", "é", "è", "ê", "ë", "f", "g", "h", "i", "î", "ï", "j", "k", "l", "m", "n", "o", "ô", "ö", "p", "q", "r", "s", "t", "u",  "ù", "û", "ü", "v", "w", "x", "y", "ÿ", "z"]
        self.alphabet_majuscule = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.signs_ok = [".", "!", "-", ","]

    def dechiffrer_sans_clefs_avec_espaces(self, texte):
        delimiter = " "
        mot_dechiffre = ""
        cle = 0
        tous_les_mots_chiffres = texte.split(" ")
        tous_mots_dechiffres = []
        
        cle = self.__trouver_cle(tous_les_mots_chiffres[0])

        for mot_chiffre in tous_les_mots_chiffres :
            mot_dechiffre = self.__dechiffrer_mots(mot_chiffre, cle)
            tous_mots_dechiffres.append(mot_dechiffre)
        
        mots_dechiffre_str = delimiter.join(tous_mots_dechiffres)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        return mots_dechiffre_str
    
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
