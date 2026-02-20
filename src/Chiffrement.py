class Chiffrement: 
    def __init__(self):
        self.cle = 0        

    def chiffrer(self, texte, cle):
        self.cle = cle
        mot_final = ""
        miniscule_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        majuscule_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        for lettre in texte : 
            if lettre in miniscule_alphabet : 
                mot_final += self.__trouver_bonne_lettre(miniscule_alphabet, lettre)
            elif lettre in majuscule_alphabet : 
                mot_final += self.__trouver_bonne_lettre(majuscule_alphabet, lettre)
            else : 
                mot_final += lettre
        return mot_final
    
    def __trouver_bonne_lettre(self, alphabet, lettre):
        index =  alphabet.index(lettre)
        nouvel_index = (index + self.cle) % 26
        nouvelle_lettre = alphabet[nouvel_index]
        return nouvelle_lettre