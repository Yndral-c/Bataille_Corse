class Cellule:
    """Une cellule de liste chaînée"""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

class Pile:
    """Structure de pile"""

    def __init__(self):
        self.contenu = None

    def est_vide(self):
        return self.contenu is None

    def empiler(self, v):
        self.contenu = Cellule(v, self.contenu)

    def sommet(self):
        if self.est_vide():
            raise IndexError("Pile vide")
        v = self.contenu.valeur
        return v

    def depiler(self):
        if self.est_vide():
            raise IndexError("pile vide")
        v = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return v

    def __str__(self):
        chaine = "valeurs de la pile = "
        c = self.contenu
        while c != None:
            chaine = chaine + str(c.valeur) + " "
            c = c.suivante
        return chaine

    def valeurs(self):
        chaine = []
        c = self.contenu
        while c != None:
            chaine.append(c.valeur)
            c = c.suivante
        return chaine

    def __len__(self):
        l = 0
        c = self.contenu
        while c != None:
            l = l + 1
            c = c.suivante
        return l