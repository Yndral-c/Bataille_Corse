import random 
import cartes
from file import File

class Jeu_de_cartes:
    """classe définissant un jeu de cartes caractérisé par :
    - son nombre de cartes
    - son paquet de cartes"""
    def __init__(self, nb):
        """constructeur de la classe jeu_de_cartes"""
        self.__nb_cartes = nb
        self.__paquet = File()
        self.__creer_paquet()

    def __creer_paquet(self):
        """méthode privée pour créer le jeu de cartes classé
        par valeur et couleur, donc non classé"""
        num_debut = 1

        for coul in ["trefle", "carreau", "coeur", "pique"]:
            for i in range(num_debut, 14):
                new_carte = cartes.Carte(i, coul)
                self.__paquet.ajouter(new_carte)

        return self.__paquet
    
    def get_nb_cartes(self):
        """renvoie le nombre de cartes dans le jeu"""
        return self.__nb_cartes
    
    def get_paquet(self):
        """renvoie le paquet de cartes"""
        return self.__paquet
    
    def melanger_paquet(self) -> File:
        """mélange aléatoirement le paquet de cartes"""
        liste = []
        a = len(self.__paquet)
        for i in range(a):
            liste.append(self.__paquet.retirer())
        random.shuffle(liste)
        for i in range(a):
            self.__paquet.ajouter(liste[i])
        return self.__paquet
    
    def diviser(self) -> File:
        """permet de diviser un jeu de cartes en 2

        Returns:
            File: Renvoie 2 paquets de cartes.
        """
        liste = []
        self.liste_player1 = File()
        self.liste_player2 = File()
        a = len(self.__paquet)
        for i in range(a):
            liste.append(self.__paquet.retirer())
        for j in range(0, a//2):
            self.liste_player1.ajouter(liste[j])
        for u in range(a//2, a):
            self.liste_player2.ajouter(liste[u])
        
        return self.liste_player1, self.liste_player2