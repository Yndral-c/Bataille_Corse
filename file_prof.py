class Cellule:
    """Une cellule de liste chaînée"""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

class File:
    def __init__(self):
        self.tete = None
        self.queue = None

    def est_vide(self):
        return self.tete is None
    
    def get_tete(self):
        return self.tete
    
    def get_queue(self):
        return self.queue

    def ajouter(self, v):
        """- prend en paramètre une file et une valeur v
        - ajoute la valeur v à l'arrière de la file
        """
        c = Cellule(v, None)
        if self.est_vide():
            self.tete = c
        else:
            self.queue.suivante = c
        self.queue = c

    def retirer(self):
        """- prend en paramètre une file
        - défile l'élément situé à l'avant de la file
        - renvoie la valeur défilée ou None si la file est vide
        """
        if self.est_vide():
            raise IndexError("La file est vide")
        v = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None
        return v

    def valeurs(self, iteration: int) -> list:
        chaine = []
        c = self.tete
        for i in range(iteration):
            chaine.append(c)
            c = c.suivante
        return chaine

    def __str__(self):
        chaine = "valeurs de la file = "
        c = self.tete
        while c != None:
            chaine = chaine + str(c.valeur) + " "
            c = c.suivante
        return chaine

    def __len__(self):
        l = 0
        c = self.tete
        while c != None:
            l = l + 1
            c = c.suivante
        return l
