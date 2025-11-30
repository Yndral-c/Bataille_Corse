import pygame # type: ignore
from jeu_de_carte import Jeu_de_cartes
from pile_prof import Pile


class Bataille_Corse:
    def __init__(self, paquet : Jeu_de_cartes):
        """_summary_

        Args:
            paquet (File de Carte): paquet de cartes
        """
        self.WIDTH, self.HEIGHT = 1000, 650
        pygame.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        self.__paquet = paquet 
        print(self.__paquet.get_nb_cartes())

        self.__paquet_mid = Pile()
        self.__paquet.melanger_paquet()
        self.player1, self.player2 = self.__paquet.diviser()
        print(self.player1.__len__(), self.player2.__len__())

        self.__valeur = ["as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi", 0]

        self.main()

    def main(self):
        image_fond = pygame.image.load("./assets/tapis.jpg").convert()
        
        pygame.display.set_caption("Bataille Corse")

        #{valeur[val1 - 1]}_{coul1} ==> permet d'afficher les valets / dame / roi /as ;sans quoi l'image ne pourra pas chargée
        val, coul = 0, 0

        running = True
        while running:
            # Efface l'écran
            self.screen.fill((255, 255, 255))
            self.screen.blit(image_fond, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.verification(self.__paquet_mid, "s")

                    elif event.key == pygame.K_DOWN:
                        self.verification(self.__paquet_mid, "down")
                    
                    #retourne une carte du joueur 1/2 lorsque la  touche Q/Flèche de gauche du clavier est appuyé.
                    if event.key == pygame.K_z:
                        #valeurp1, couleurp1 = self.nouvelle_carte_p1()
                        self.__paquet_mid.empiler(self.nouvelle_carte(self.player1))

                    elif event.key == pygame.K_UP:
                        #valeurp2, couleurp2 = self.nouvelle_carte_p2()
                        self.__paquet_mid.empiler(self.nouvelle_carte(self.player2))
                        
            
            police = pygame.font.SysFont("Arial", 30) #afficher un texte
            image_texte1 = police.render(f"Nombre de carte du joueur 1 : {self.player1.__len__()}", 1, (255, 255, 255))
            self.screen.blit(image_texte1, (0, self.HEIGHT - 30))
            image_texte2 = police.render(f"Nombre de carte du joueur 2 : {self.player2.__len__()}", 1, (255, 255, 255))
            self.screen.blit(image_texte2, (self.WIDTH - 450, self.HEIGHT - 30))
            

            #afficher la carte au milieu
            if self.__paquet_mid.__len__() >= 1:
                val, coul = self.__paquet_mid.sommet().get_attributs()


            image_centre = pygame.image.load(f"./assets/{self.__valeur[val - 1]}_{coul}.png")
            img_c_width = image_centre.get_width()
            img_c_height = image_centre.get_height()
            self.screen.blit(image_centre, (self.WIDTH // 2 - img_c_width // 2, self.HEIGHT //2 - img_c_height // 2))
            
            dos_carte = pygame.image.load("./assets/dos_de_carte2.png")
            self.screen.blit(dos_carte, (30, 30))
            self.screen.blit(dos_carte, (self.WIDTH - dos_carte.get_width() - 30, 30))

            #vérifier si l'un des 2 joueur n'a plus de carte
            if self.victoire():
                running = False

            # Met à jour l'écran
            pygame.display.flip()

        pygame.quit()
    
    def nouvelle_carte(self, player):
        carte = player.retirer()
        return carte
    
    def verification(self, pile: Pile, touche: str):
        """Fonction qui vérifie si le joueur a tappé au bon moment afin de récupérer la pile du milieu
        """
        carte_verif = pile.valeurs()
        if touche == "s":
            if len(carte_verif) != 0:
                if len(carte_verif) >= 3:#créer une condition au cas où la list carte_verif est vide/contient moins de 3 élements
                    carte1 = carte_verif[0]
                    carte2 = carte_verif[1]
                    carte3 = carte_verif[2]
                elif len(carte_verif) == 2:
                    carte1 = carte_verif[0]
                    carte2 = carte_verif[1]
                elif len(carte_verif) == 1:
                    carte1 = carte_verif[0]


            if carte1.get_valeur() == 10: #Si la carte du milieu est un 10
                for i in range(pile.__len__()):
                    carte = pile.depiler()
                    self.player1.ajouter(carte)

            elif carte1.get_valeur() == carte2.get_valeur(): #Si les 2 dernières cartes du milieu sont double (double 4 par exemple)
                for i in range(pile.__len__()):
                    carte = pile.depiler()
                    self.player1.ajouter(carte)

            elif carte1.get_valeur() + carte2.get_valeur() == 10: #Si la somme des 2 dernières cartes du milieu est égale à 10 (8 de trèfle + 2 carreau par exemple)
                for i in range(pile.__len__()):
                    carte = pile.depiler()
                    self.player1.ajouter(carte)
            
            elif carte3.get_valeur() == carte1.get_valeur(): #Si l'avant avant dernière carte et la dernière cartes du milieu sont double (double 4 séparé par un 2 de trèfle par exemple)
                for i in range(pile.__len__()):
                    carte = pile.depiler()
                    self.player1.ajouter(carte)

            elif carte3.get_valeur() + carte1.get_valeur() == 10: #Si la somme de l'avant avant dernière carte et de la dernière carte du milieu est égale à 10 (8 de trèfle + 2 carreau séparé par un As de coeur par exemple)
                for i in range(pile.__len__()):
                    carte = pile.depiler()
                    self.player1.ajouter(carte)
            

        elif touche == "down":
            if len(carte_verif) != 0:
                if len(carte_verif) >= 3:#créer une condition au cas où la list carte_verif est vide/contient moins de 3 élements
                    carte1 = carte_verif[0]
                    carte2 = carte_verif[1]
                    carte3 = carte_verif[2]
                elif len(carte_verif) == 2:
                    carte1 = carte_verif[0]
                    carte2 = carte_verif[1]
                elif len(carte_verif) == 1:
                    carte1 = carte_verif[0]


            if carte1.get_valeur() == 10: #Si la carte du milieu est un 10
                for i in range(pile.__len__()):
                    carte = pile.depiler()
                    self.player2.ajouter(carte)

            elif carte1.get_valeur() == carte2.get_valeur(): #Si les 2 dernières cartes du milieu sont double (double 4 par exemple)
                for i in range(pile.__len__()):
                    carte = pile.depiler()
                    self.player2.ajouter(carte)

            elif carte1.get_valeur() + carte2.get_valeur() == 10: #Si la somme des 2 dernières cartes du milieu est égale à 10 (8 de trèfle + 2 carreau par exemple)
                for i in range(pile.__len__()):
                    carte = pile.depiler()
                    self.player2.ajouter(carte)
            
            elif carte3.get_valeur() == carte1.get_valeur(): #Si l'avant avant dernière carte et la dernière cartes du milieu sont double (double 4 séparé par un 2 de trèfle par exemple)
                for i in range(pile.__len__()):
                    carte = pile.depiler()
                    self.player2.ajouter(carte)

            elif carte3.get_valeur() + carte1.get_valeur() == 10: #Si la somme de l'avant avant dernière carte et de la dernière carte du milieu est égale à 10 (8 de trèfle + 2 carreau séparé par un As de coeur par exemple)
                for i in range(pile.__len__()):
                    carte = pile.depiler()
                    self.player2.ajouter(carte)

    
    def victoire(self):
        """Fonction qui permet de vérifier si l'un des joueur n'a plus de carte, si c'est le cas, alors il a perdu
        """
        
        if self.player1.est_vide():
            if self.player2.__len__() == 52:
                print("Le joueur 2 a gagné la partie !")
                return True
        elif self.player2.est_vide():
            if self.player1.__len__() == 52:
                print("Le joueur 1 a gagné la partie !")
                return True
        


    

jeu_de_carte = Jeu_de_cartes(52)
jeu = Bataille_Corse(jeu_de_carte)