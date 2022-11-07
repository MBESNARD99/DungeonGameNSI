"""
Programme réalisé par Besnard, Mathéo, TG6
"""
import pygame
from random import randint,choice
import time

#variables du niveau
NB_TILES = 666   #nombre de tiles a chager (ici de 00.png à 26.png) 27 au total !!
TITLE_SIZE=32   #definition du dessin (carré)
largeur=12       #hauteur du niveau
hauteur=12       #largeur du niveau
tiles=[]       #liste d'images tiles
clock = pygame.time.Clock()

combat = False

#definition du niveau

zone=1

""""
NIVEAU PRINCIPAL
"""

niveau=[[23, 24, 24, 24, 486, 486, 486, 24, 24, 24, 24, 25],
        [46, 47, 47, 486, 486, 486, 47, 47, 47, 47, 47, 48],
        [46, 47, 47, 486, 486, 47, 47, 47, 88, 47, 47, 48],
        [46, 47, 47, 486, 486, 47, 47, 88, 88, 91, 47, 47],
        [210, 212, 417, 417, 486, 47, 88, 88, 88, 91, 91, 47],
        [46, 47, 416, 33, 33, 47, 88, 111, 131, 114, 91, 47],
        [46, 486, 486, 416, 188, 47, 111, 223, 270, 133, 114, 47],
        [46, 486, 486, 486, 187, 47, 153, 222, 268, 222, 154, 47],
        [46, 486, 486, 47, 187, 47, 270, 177, 224, 177, 270, 47],
        [486, 486, 486, 47, 164, 120, 47, 47, 188, 47, 47, 48],
        [486, 486, 47, 47, 47, 164, 189, 189, 194, 47, 47, 48],
        [486, 486, 70, 70, 70, 70, 70, 70, 70, 70, 70, 71]]

decor=[[0, 138, 0, 0, 0, 0, 0, 0, 0, 0, 278, 279],
       [185, 0, 0, 0, 0, 0, 0, 0, 322, 0, 276, 277],
       [0, 0, 253, 0, 0, 0, 0, 65, 0, 68, 299, 300],
       [0, 322, 0, 0, 0, 256, 65, 66, 0, 0, 68, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 130, 0, 112, 0, 322],
       [322, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 207, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 231, 0, 0, 322, 0],
       [0, 0, 0, 0, 256, 0, 0, 0, 0, 257, 0, 0],
       [0, 0, 0, 322, 0, 0, 303, 0, 0, 0, 0, 0]]

collisions=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

""""
NIVEAU PRINCIPAL
"""

niveau2=[[46, 73, 73, 73, 73, 73, 24, 24, 24, 24, 24, 25],
        [46, 27, 149, 28, 150, 73, 47, 47, 47, 47, 47, 47],
        [46, 73, 149, 151, 150, 27, 47, 47, 47, 47, 47, 47],
        [46, 288, 73, 73, 73, 287, 47, 47, 47, 47, 47, 47],
        [46, 311, 73, 73, 73, 310, 47, 47, 47, 170, 189, 189],
        [46, 221, 149, 151, 150, 289, 47, 47, 47, 187, 47, 47],
        [46, 47, 47, 187, 47, 47, 47, 47, 170, 194, 47, 47],
        [46, 47, 47, 193, 171, 47, 47, 47, 187, 47, 47, 47],
        [46, 47, 47, 47, 147, 189, 189, 189, 194, 47, 47, 47],
        [46, 47, 47, 47, 187, 47, 47, 47, 47, 47, 47, 486],
        [46, 47, 47, 237, 142, 237, 47, 47, 47, 47, 486, 486],
        [69, 70, 70, 519, 500, 521, 70, 70, 70, 70, 486, 486]]

decor2=[[0, 0, 0, 0, 0, 0, 0, 0, 278, 279, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 276, 277, 0, 185],
       [0, 0, 0, 0, 0, 0, 256, 0, 299, 300, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 0, 0],
       [140, 0, 0, 0, 0, 0, 0, 253, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 256, 0],
       [0, 0, 231, 0, 0, 0, 207, 0, 0, 0, 0, 0],
       [0, 278, 279, 0, 0, 0, 0, 0, 0, 0, 0, 322],
       [0, 301, 302, 0, 0, 0, 0, 0, 0, 186, 0, 0],
       [0, 276, 277, 0, 0, 0, 0, 278, 279, 0, 0, 0],
       [0, 299, 300, 0, 0, 0, 0, 276, 277, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 299, 300, 0, 0, 0]]

collisions2=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
         [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
         [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

"""
SHOP
"""

shop=[[121, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 123],
      [144, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 146],
      [144, 142, 30, 142, 30, 142, 142, 30, 142, 30, 142, 146],
      [144, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 146],
      [144, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 146],
      [144, 142, 30, 142, 30, 142, 142, 30, 142, 30, 142, 146],
      [144, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 146],
      [144, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 146],
      [144, 142, 30, 142, 30, 142, 142, 142, 142, 142, 142, 146],
      [144, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 146],
      [144, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 146],
      [167, 168, 168, 168, 168, 201, 202, 168, 168, 168, 168, 169]]

decorshop=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 665, 0, 664, 0, 0, 663, 0, 662, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 661, 0, 660, 0, 0, 652, 0, 653, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 650, 0, 651, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

colshop=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]]

"""
DONJON
"""

donjon=[[73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73],
      [73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73],
      [73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73],
      [73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73],
      [73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73],
      [73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73],
      [73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73],
      [73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73],
      [73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73],
      [73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73],
      [73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73],
      [73, 73, 73, 73, 73, 28, 73, 73, 73, 73, 73, 73]]

decordonjon=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

coldonjon=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

achatMarteauBois = False
achatMarteauAmeliore = False

class Personnage(pygame.sprite.Sprite):

    def __init__(self,position,size,img,collisions,collisions2,colshop,coldonjon,nom,vie,xp,niveau,argent):
        super().__init__()


        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.size=size
        self.collisions=collisions
        self.collisions2=collisions2
        self.colshop=colshop
        self.coldonjon=coldonjon
        self.x,self.y=position
        self.rect.x=self.x*size
        self.rect.y=self.y*size

        self.nom=nom
        self.vie=vie
        self.maxVie=vie
        self.xp=xp
        self.niveau=niveau
        self.argent=argent

    def testCollisionsDecor(self,x,y):
        if zone==1:
            if (self.collisions[self.y+y][self.x+x]==0):
                self.x+=x
                self.y+=y
        if zone==2:
            if (self.colshop[self.y+y][self.x+x]==0):
                self.x+=x
                self.y+=y
        if zone==3:
            if (self.collisions2[self.y+y][self.x+x]==0):
                self.x+=x
                self.y+=y
        if zone==4:
            if (self.coldonjon[self.y+y][self.x+x]==0):
                self.x+=x
                self.y+=y

    def droite(self):
        global zone
        global achatMarteauBois
        global achatMarteauAmeliore
        if self.x == 11 and self.y == 4 and zone == 3:
            print("Map Principale")
            zone = 1
            self.x = -1
            self.y = 4
            aventuriers.update()
        self.testCollisionsDecor(1,0)
        self.rect.x=self.x*self.size
        if self.x == 3 and self.y == 1 and zone == 3:
            print("Donjon")
            zone = 4
            self.x = 5
            self.y = 11
            self.testCollisionsDecor(0,-1)
            self.rect.y=self.y*self.size
            self.rect.x=self.x*self.size


        if self.x == 2 and self.y == 2 and zone == 2: #MARTEAU EN BOIS
            if perso.estGuerrier() == False:
                print("Vous ne pouvez pas acheter de marteau car vous n'êtes pas Guerrier !")
            if perso.estGuerrier() == True:
                if achatMarteauBois == True:
                    print("Vous avez déjà acheté ce marteau !")
                if achatMarteauBois == False:
                    if perso.argent < 3:
                        print("Vous ne pouvez pas acheter ce marteau car vous n'avez pas assez d'argent ! (Il vous faut 3 pièces)")
                    else:
                        print("Vous venez d'acheter ce marteau pour 3 pièces ! Vous gagnez 1 force !")
                        perso.argent-=3
                        perso.augmenterForce()
                        achatMarteauBois = True
        if self.x == 4 and self.y == 2 and zone == 2: #MARTEAU AMELIORÉ
            if perso.estGuerrier() == False:
                print("Vous ne pouvez pas acheter de marteau car vous n'êtes pas Guerrier !")
            if perso.estGuerrier() == True:
                if achatMarteauAmeliore == True:
                    print("Vous avez déjà acheté ce marteau !")
                if achatMarteauAmeliore == False:
                    if perso.argent < 6:
                        print("Vous ne pouvez pas acheter ce marteau car vous n'avez pas assez d'argent ! (Il vous faut 6 pièces)")
                    else:
                        print("Vous venez d'acheter ce marteau pour 6 pièces ! Vous gagnez 2 forces !")
                        perso.argent-=6
                        perso.augmenterForce()
                        perso.augmenterForce()
                        achatMarteauAmeliore = True

        if self.x == 7 and self.y == 2 and zone == 2:  # KNIFE EN BOIS
            print("Vous ne pouvez pas acheter ce couteau car vous n'êtes pas Assassin !")
        if self.x == 9 and self.y == 2 and zone == 2:  # KNIFE AMELIORE
            print("Vous ne pouvez pas acheter ce couteau car vous n'êtes pas Assassin !")
        if self.x == 2 and self.y == 5 and zone == 2:  # BATON MAGE EN BOIS
            print("Vous ne pouvez pas acheter ce baton magique car vous n'êtes pas Mage !")
        if self.x == 4 and self.y == 5 and zone == 2:  # BATON MAGE AMELIORE
            print("Vous ne pouvez pas acheter ce baton magique car vous n'êtes pas Mage !")
        if self.x == 7 and self.y == 5 and zone == 2:  # SHIELD EN BOIS
            print("Vous ne pouvez pas acheter ce bouclier car vous n'êtes pas Tank !")
        if self.x == 9 and self.y == 5 and zone == 2:  # SHIELD AMELIORE
            print("Vous ne pouvez pas acheter ce bouclier car vous n'êtes pas Tank !")

        if self.x == 2 and self.y == 8 and zone == 2:  # POTION XP
            if perso.argent < 1:
                print("Vous ne pouvez pas acheter cette potion d'xp car vous n'avez pas assez d'argent ! (Il vous faut 1 pièce)")
            else:
                print("Vous venez d'acheter cette potion d'xp pour 1 pièce ! Vous gagnez 2 xp !")
                perso.monterExperience()
                perso.argent-=1

        if self.x == 4 and self.y == 8 and zone == 2:  # POTION DE VIE
            if perso.argent < 5:
                print("Vous ne pouvez pas acheter cette potion de vie car vous n'avez pas assez d'argent ! (Il vous faut 5 pièces)")
            if perso.argent >= 5:
                if perso.vie == perso.maxVie:
                    print("Vous ne pouvez pas acheter cette potion de vie car vous êtes déjà au maximum !")
                else:
                    print("Vous venez d'acheter cette potion de vie pour 5 pièces ! Vous regagnez toute votre vie !")
                    perso.ajouterVie(perso.maxVie-perso.vie)
                    perso.argent-=5

    def gauche(self):
        global zone
        global achatMarteauBois
        global achatMarteauAmeliore
        if self.x == 0 and self.y == 4 and zone == 1:
            print("Map Gauche")
            zone = 3
            self.x = 12
            self.y = 4
            aventuriers.update()
        self.testCollisionsDecor(-1,0)
        self.rect.x=self.x*self.size
        if self.x == 3 and self.y == 1 and zone == 3:
            print("Donjon")
            zone = 4
            self.x = 5
            self.y = 11
            self.testCollisionsDecor(0,-1)
            self.rect.y=self.y*self.size
            self.rect.x=self.x*self.size


        if self.x == 2 and self.y == 2 and zone == 2: #MARTEAU EN BOIS
            if perso.estGuerrier() == False:
                print("Vous ne pouvez pas acheter de marteau car vous n'êtes pas Guerrier !")
            if perso.estGuerrier() == True:
                if achatMarteauBois == True:
                    print("Vous avez déjà acheté ce marteau !")
                if achatMarteauBois == False:
                    if perso.argent < 3:
                        print("Vous ne pouvez pas acheter ce marteau car vous n'avez pas assez d'argent ! (Il vous faut 3 pièces)")
                    else:
                        print("Vous venez d'acheter ce marteau pour 3 pièces ! Vous gagnez 1 force !")
                        perso.argent-=3
                        perso.augmenterForce()
                        achatMarteauBois = True
        if self.x == 4 and self.y == 2 and zone == 2: #MARTEAU AMELIORÉ
            if perso.estGuerrier() == False:
                print("Vous ne pouvez pas acheter de marteau car vous n'êtes pas Guerrier !")
            if perso.estGuerrier() == True:
                if achatMarteauAmeliore == True:
                    print("Vous avez déjà acheté ce marteau !")
                if achatMarteauAmeliore == False:
                    if perso.argent < 6:
                        print("Vous ne pouvez pas acheter ce marteau car vous n'avez pas assez d'argent ! (Il vous faut 6 pièces)")
                    else:
                        print("Vous venez d'acheter ce marteau pour 6 pièces ! Vous gagnez 2 forces !")
                        perso.argent-=6
                        perso.augmenterForce()
                        perso.augmenterForce()
                        achatMarteauAmeliore = True

        if self.x == 7 and self.y == 2 and zone == 2:  # KNIFE EN BOIS
            print("Vous ne pouvez pas acheter ce couteau car vous n'êtes pas Assassin !")
        if self.x == 9 and self.y == 2 and zone == 2:  # KNIFE AMELIORE
            print("Vous ne pouvez pas acheter ce couteau car vous n'êtes pas Assassin !")
        if self.x == 2 and self.y == 5 and zone == 2:  # BATON MAGE EN BOIS
            print("Vous ne pouvez pas acheter ce baton magique car vous n'êtes pas Mage !")
        if self.x == 4 and self.y == 5 and zone == 2:  # BATON MAGE AMELIORE
            print("Vous ne pouvez pas acheter ce baton magique car vous n'êtes pas Mage !")
        if self.x == 7 and self.y == 5 and zone == 2:  # SHIELD EN BOIS
            print("Vous ne pouvez pas acheter ce bouclier car vous n'êtes pas Tank !")
        if self.x == 9 and self.y == 5 and zone == 2:  # SHIELD AMELIORE
            print("Vous ne pouvez pas acheter ce bouclier car vous n'êtes pas Tank !")

        if self.x == 2 and self.y == 8 and zone == 2:  # POTION XP
            if perso.argent < 1:
                print("Vous ne pouvez pas acheter cette potion d'xp car vous n'avez pas assez d'argent ! (Il vous faut 1 pièce)")
            else:
                print("Vous venez d'acheter cette potion d'xp pour 1 pièce ! Vous gagnez 2 xp !")
                perso.monterExperience()
                perso.argent-=1

        if self.x == 4 and self.y == 8 and zone == 2:  # POTION DE VIE
            if perso.argent < 5:
                print("Vous ne pouvez pas acheter cette potion de vie car vous n'avez pas assez d'argent ! (Il vous faut 5 pièces)")
            if perso.argent >= 5:
                if perso.vie == perso.maxVie:
                    print("Vous ne pouvez pas acheter cette potion de vie car vous êtes déjà au maximum !")
                else:
                    print("Vous venez d'acheter cette potion de vie pour 5 pièces ! Vous regagnez toute votre vie !")
                    perso.ajouterVie(perso.maxVie-perso.vie)
                    perso.argent-=5

    def haut(self):
        global zone
        global achatMarteauBois
        global achatMarteauAmeliore
        self.testCollisionsDecor(0,-1)
        self.rect.y=self.y*self.size
        if self.x == 3 and self.y == 1 and zone == 3:
            print("Donjon")
            zone = 4
            self.x = 5
            self.y = 11
            self.testCollisionsDecor(0,-1)
            self.rect.y=self.y*self.size
            self.rect.x=self.x*self.size
        if self.x == 8 and self.y == 8 and zone == 1:
            print("Shop")
            zone = 2
            self.x = 5
            self.y = 11
            self.testCollisionsDecor(0,-1)
            self.rect.y=self.y*self.size
            self.rect.x=self.x*self.size


        if self.x == 2 and self.y == 2 and zone == 2: #MARTEAU EN BOIS
            if perso.estGuerrier() == False:
                print("Vous ne pouvez pas acheter de marteau car vous n'êtes pas Guerrier !")
            if perso.estGuerrier() == True:
                if achatMarteauBois == True:
                    print("Vous avez déjà acheté ce marteau !")
                if achatMarteauBois == False:
                    if perso.argent < 3:
                        print("Vous ne pouvez pas acheter ce marteau car vous n'avez pas assez d'argent ! (Il vous faut 3 pièces)")
                    else:
                        print("Vous venez d'acheter ce marteau pour 3 pièces ! Vous gagnez 1 force !")
                        perso.argent-=3
                        perso.augmenterForce()
                        achatMarteauBois = True
        if self.x == 4 and self.y == 2 and zone == 2: #MARTEAU AMELIORÉ
            if perso.estGuerrier() == False:
                print("Vous ne pouvez pas acheter de marteau car vous n'êtes pas Guerrier !")
            if perso.estGuerrier() == True:
                if achatMarteauAmeliore == True:
                    print("Vous avez déjà acheté ce marteau !")
                if achatMarteauAmeliore == False:
                    if perso.argent < 6:
                        print("Vous ne pouvez pas acheter ce marteau car vous n'avez pas assez d'argent ! (Il vous faut 6 pièces)")
                    else:
                        print("Vous venez d'acheter ce marteau pour 6 pièces ! Vous gagnez 2 forces !")
                        perso.argent-=6
                        perso.augmenterForce()
                        perso.augmenterForce()
                        achatMarteauAmeliore = True

        if self.x == 7 and self.y == 2 and zone == 2:  # KNIFE EN BOIS
            print("Vous ne pouvez pas acheter ce couteau car vous n'êtes pas Assassin !")
        if self.x == 9 and self.y == 2 and zone == 2:  # KNIFE AMELIORE
            print("Vous ne pouvez pas acheter ce couteau car vous n'êtes pas Assassin !")
        if self.x == 2 and self.y == 5 and zone == 2:  # BATON MAGE EN BOIS
            print("Vous ne pouvez pas acheter ce baton magique car vous n'êtes pas Mage !")
        if self.x == 4 and self.y == 5 and zone == 2:  # BATON MAGE AMELIORE
            print("Vous ne pouvez pas acheter ce baton magique car vous n'êtes pas Mage !")
        if self.x == 7 and self.y == 5 and zone == 2:  # SHIELD EN BOIS
            print("Vous ne pouvez pas acheter ce bouclier car vous n'êtes pas Tank !")
        if self.x == 9 and self.y == 5 and zone == 2:  # SHIELD AMELIORE
            print("Vous ne pouvez pas acheter ce bouclier car vous n'êtes pas Tank !")

        if self.x == 2 and self.y == 8 and zone == 2:  # POTION XP
            if perso.argent < 1:
                print("Vous ne pouvez pas acheter cette potion d'xp car vous n'avez pas assez d'argent ! (Il vous faut 1 pièce)")
            else:
                print("Vous venez d'acheter cette potion d'xp pour 1 pièce ! Vous gagnez 2 xp !")
                perso.monterExperience()
                perso.argent-=1

        if self.x == 4 and self.y == 8 and zone == 2:  # POTION DE VIE
            if perso.argent < 5:
                print("Vous ne pouvez pas acheter cette potion de vie car vous n'avez pas assez d'argent ! (Il vous faut 5 pièces)")
            if perso.argent >= 5:
                if perso.vie == perso.maxVie:
                    print("Vous ne pouvez pas acheter cette potion de vie car vous êtes déjà au maximum !")
                else:
                    print("Vous venez d'acheter cette potion de vie pour 5 pièces ! Vous regagnez toute votre vie !")
                    perso.ajouterVie(perso.maxVie-perso.vie)
                    perso.argent-=5

    def bas(self):
        global zone
        global achatMarteauBois
        global achatMarteauAmeliore
        if self.x == 5 and self.y == 10 and zone == 4:
            print("Map Gauche")
            zone = 3
            self.x = 3
            self.y = 1
            self.rect.x = self.x * self.size
        if self.x == 5 and self.y == 10 and zone == 2:
            print("Map Principale")
            zone = 1
            self.x = 8
            self.y = 8
            self.rect.x = self.x * self.size
        if self.x == 6 and self.y == 10 and zone == 2:
            print("Map Principale")
            zone = 1
            self.x = 8
            self.y = 8
            self.rect.x = self.x * self.size
        self.testCollisionsDecor(0,1)
        self.rect.y=self.y*self.size


        if self.x == 2 and self.y == 2 and zone == 2: #MARTEAU EN BOIS
            if perso.estGuerrier() == False:
                print("Vous ne pouvez pas acheter de marteau car vous n'êtes pas Guerrier !")
            if perso.estGuerrier() == True:
                if achatMarteauBois == True:
                    print("Vous avez déjà acheté ce marteau !")
                if achatMarteauBois == False:
                    if perso.argent < 3:
                        print("Vous ne pouvez pas acheter ce marteau car vous n'avez pas assez d'argent ! (Il vous faut 3 pièces)")
                    else:
                        print("Vous venez d'acheter ce marteau pour 3 pièces ! Vous gagnez 1 force !")
                        perso.argent-=3
                        perso.augmenterForce()
                        achatMarteauBois = True
        if self.x == 4 and self.y == 2 and zone == 2: #MARTEAU AMELIORÉ
            if perso.estGuerrier() == False:
                print("Vous ne pouvez pas acheter de marteau car vous n'êtes pas Guerrier !")
            if perso.estGuerrier() == True:
                if achatMarteauAmeliore == True:
                    print("Vous avez déjà acheté ce marteau !")
                if achatMarteauAmeliore == False:
                    if perso.argent < 6:
                        print("Vous ne pouvez pas acheter ce marteau car vous n'avez pas assez d'argent ! (Il vous faut 6 pièces)")
                    else:
                        print("Vous venez d'acheter ce marteau pour 6 pièces ! Vous gagnez 2 forces !")
                        perso.argent-=6
                        perso.augmenterForce()
                        perso.augmenterForce()
                        achatMarteauAmeliore = True

        if self.x == 7 and self.y == 2 and zone == 2:  # KNIFE EN BOIS
            print("Vous ne pouvez pas acheter ce couteau car vous n'êtes pas Assassin !")
        if self.x == 9 and self.y == 2 and zone == 2:  # KNIFE AMELIORE
            print("Vous ne pouvez pas acheter ce couteau car vous n'êtes pas Assassin !")
        if self.x == 2 and self.y == 5 and zone == 2:  # BATON MAGE EN BOIS
            print("Vous ne pouvez pas acheter ce baton magique car vous n'êtes pas Mage !")
        if self.x == 4 and self.y == 5 and zone == 2:  # BATON MAGE AMELIORE
            print("Vous ne pouvez pas acheter ce baton magique car vous n'êtes pas Mage !")
        if self.x == 7 and self.y == 5 and zone == 2:  # SHIELD EN BOIS
            print("Vous ne pouvez pas acheter ce bouclier car vous n'êtes pas Tank !")
        if self.x == 9 and self.y == 5 and zone == 2:  # SHIELD AMELIORE
            print("Vous ne pouvez pas acheter ce bouclier car vous n'êtes pas Tank !")

        if self.x == 2 and self.y == 8 and zone == 2:  # POTION XP
            if perso.argent < 1:
                print("Vous ne pouvez pas acheter cette potion d'xp car vous n'avez pas assez d'argent ! (Il vous faut 1 pièce)")
            else:
                print("Vous venez d'acheter cette potion d'xp pour 1 pièce ! Vous gagnez 2 xp !")
                perso.monterExperience()
                perso.argent-=1

        if self.x == 4 and self.y == 8 and zone == 2:  # POTION DE VIE
            if perso.argent < 5:
                print("Vous ne pouvez pas acheter cette potion de vie car vous n'avez pas assez d'argent ! (Il vous faut 5 pièces)")
            if perso.argent >= 5:
                if perso.vie == perso.maxVie:
                    print("Vous ne pouvez pas acheter cette potion de vie car vous êtes déjà au maximum !")
                else:
                    print("Vous venez d'acheter cette potion de vie pour 5 pièces ! Vous regagnez toute votre vie !")
                    perso.ajouterVie(perso.maxVie-perso.vie)
                    perso.argent-=5

    def montrerVie(self):
        print(self.nom, "à", self.vie, "HP")

    def ajouterVie(self, vie):
        if vie > self.maxVie:
            print("Vous ne pouvez pas dépasser la vie maximale du personnage !")
        else:
            self.vie += vie

    def retirerVie(self, vie):
        self.vie -= vie
        if self.vie < 0:
            self.vie = 0

    def monterExperience(self):
        self.xp += 2
        self.niveau = self.xp // 10
        print(self.xp, self.niveau)

    def estVivant(self):
        if self.vie > 0:
            return True
        else:
            return False

    def estMort(self):
        if self.vie > 0:
            return False
        else:
            return True


"""

CLASSE GUERRIER

"""
#(self,position,size,img,collisions,collisions2,colshop,coldonjon,nom,vie,xp,niveau):
class Guerrier(Personnage):
    def __init__(self,position,size,img,collisions,collisions2,colshop,coldonjon,nom,force,vie,xp,niveau,argent):
        super().__init__(position,size,img,collisions,collisions2,colshop,coldonjon,nom, vie, xp, niveau,argent)
        self.force = force

    def augmenterForce(self):
        self.force += 1

    def estGuerrier(self):
        return True

    def estMage(self):
        return False

    def combat(self, adversaire):
        attaque = randint(1, 4)
        degats = attaque * self.niveau * self.force - adversaire.niveau
        print("{} a fait {} de dégats sur {}".format(self.nom, degats, adversaire.nom))
        if adversaire.estVivant() == True:
            adversaire.retirerVie(degats)
        self.xp += degats
        self.niveau = self.xp // 10
        if adversaire.estMort() == True:
            self.augmenterForce()
            print("{} est mort ! {} a donc gagné 1 de force !".format(adversaire.nom, self.nom))

    def __repr__(self):
        return ("Nom: " + str(self.nom) + ", Vie: " + str(self.vie) + ", Xp: " + str(self.xp) + ", Niveau: " + str(
            self.niveau) + ", Force: " + str(self.force))

"""

CLASSE MAGICIEN

"""

class Magicien(Personnage):
    def __init__(self,position,size,img,collisions,collisions2,colshop,coldonjon,nom,force,vie,xp,niveau,argent):
        super().__init__(position,size,img,collisions,collisions2,colshop,coldonjon,nom, vie, xp, niveau,argent)
        self.maxMana = mana
        self.mana = mana

    def augmenterMana(self):
        self.maxMana += 10

    def ajouterMana(self):
        self.mana += 1
        if self.mana > self.maxMana:
            self.mana -= 1
            print("Le magicien à déjà son mana max !")

    def estGuerrier(self):
        return False

    def estMage(self):
        return True

    def retirerMana(self, mana):
        self.mana -= mana
        if self.mana < 0:
            self.mana += 1
            return False
            print("Le magicien n'a plus de mana, il ne peut donc plus lancer de sort")
        else:
            return True

    def combat(self, adversaire):
        attaque = randint(1, 4)
        degats = attaque * self.niveau * 2 - adversaire.niveau
        print("{} a fait {} de dégats sur {}".format(self.nom, degats, adversaire.nom))
        if adversaire.estVivant() == True:
            if self.mana > 0:
                adversaire.retirerVie(degats)
                self.retirerMana(1)
        self.xp += degats
        self.niveau = self.xp // 10
        if adversaire.estMort() == True:
            self.augmenterMana()
            print("{} est mort ! {} a donc gagné 10 de mana max !".format(adversaire.nom, self.nom))

    def __repr__(self):
        return ("Nom: " + str(self.nom) + ", Vie: " + str(self.vie) + ", Xp: " + str(self.xp) + ", Niveau: " + str(
            self.niveau) + ", Mana: " + str(self.mana) + ", Mana Max: " + str(self.maxMana))

"""

SIMULATION DE COMBAT ENTRE 2 PERSONNAGES

"""

def duel(combattant,mechant):
    global combat
    while combattant.estVivant() and mechant.estVivant():
        if combattant.vie <= 0:
            print("Le combat est terminé ! {} a donc gagné".format(mechant.nom))
            combat = False
        else:
            combattant.combat(mechant)
            time.sleep(1)
        if mechant.vie <= 0:
            print("Le combat est terminé ! {} a donc gagné".format(combattant.nom))
            combat = False
        else:
            mechant.combat(combattant)
            time.sleep(1)


#la taille de la fenetre dépend de la largeur et de la hauteur du niveau
#on rajoute une rangée de 32 pixels en bas de la fentre pour afficher le score d'ou (hauteur +1)
pygame.init()
fenetre = pygame.display.set_mode((largeur*TITLE_SIZE, (hauteur+1)*TITLE_SIZE))
pygame.display.set_caption("Dungeon")
font = pygame.font.Font('freesansbold.ttf', 20)



def chargetiles(tiles):
    """
    fonction permettant de charger les images tiles dans une liste tiles[]
    """
    for n in range(0,NB_TILES):
        #print('data/'+str(n)+'.png')
        tiles.append(pygame.image.load('data/'+str(n)+'.png')) #attention au chemin


def afficheNiveau(niveau):
    """
    affiche le niveau a partir de la liste a deux dimensions niveau[][]
    """
    global collisions
    for y in range(hauteur):
        for x in range(largeur):
            fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))
            if zone==1:
                if (decor[y][x]>0):
                    fenetre.blit(tiles[decor[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))
            if zone==2:
                if (decorshop[y][x]>0):
                    fenetre.blit(tiles[decorshop[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))
                fenetre.blit(tiles[643], (0, 0))
            if zone==3:
                if (decor2[y][x]>0):
                    fenetre.blit(tiles[decor2[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))
            if zone==4:
                if (decordonjon[y][x]>0):
                    fenetre.blit(tiles[decordonjon[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))



fenetre.fill((0,0,0))   #efface la fenetre
chargetiles(tiles)  #chargement des images


#perso = Personnage([1,1],TITLE_SIZE,"data/knight.png",collisions,collisions2,colshop,coldonjon,"Perso1",30,20,2)
perso2 = Guerrier([5,2],TITLE_SIZE,"data/SkeletonMage.png",collisions,collisions2,colshop,coldonjon,"Mage Squelette",2,30,20,2,0)

perso = Guerrier([1,1],TITLE_SIZE,"data/knight.png",collisions,collisions2,colshop,coldonjon,"Perso1",2,30,20,2,0)

aventuriers = pygame.sprite.Group()
aventuriers.add(perso)

mechants = pygame.sprite.Group()
mechants.add(perso2)



arial_font = pygame.font.SysFont("arial", 20)
arial_font_2 = pygame.font.SysFont("arial", 28)
arial_font_money = pygame.font.SysFont("arial", 35)

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP
                perso.haut()
            elif event.key == pygame.K_DOWN:  #est-ce la touche DOWN
                perso.bas()
            elif event.key == pygame.K_RIGHT:  #est-ce la touche RIGHT
                perso.droite()
            elif event.key == pygame.K_LEFT:  #est-ce la touche LEFT
                perso.gauche()
            elif event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
    col = pygame.sprite.collide_rect(perso, perso2)
    if zone == 4:
        if col==1:
            print("Combat")
            perso.x = 4
            perso.y = 5
            perso2.x = 7
            perso2.y = 5
            perso.rect.y=perso.y*perso.size
            perso.rect.x=perso.x*perso.size
            perso2.rect.y=perso2.y*perso2.size
            perso2.rect.x=perso2.x*perso2.size
            combat = True
            duel(perso,perso2)
            if perso2.estMort() == True:
                mechants.remove(perso2)
                perso.argent += 10

    if perso.estMort() == True:
        loop = False
        print("Vous êtes mort, vous avez donc perdu !")

    fenetre.fill((0,0,0))
    if zone == 1:
        afficheNiveau(niveau)   #affiche le niveau
    if zone == 2:
        afficheNiveau(shop)   #affiche le shop
    if zone == 3:
        afficheNiveau(niveau2)   #affiche le niveau 2
    if zone == 4:
        afficheNiveau(donjon)   #affiche le donjon
        mechants.update()
        mechants.draw(fenetre)
    aventuriers.update()
    aventuriers.draw(fenetre)
    pygame.display.update() #mets à jour la fentre graphique


    lifehero_text = arial_font.render(str(perso.vie), True, (255, 255, 255))
    life_text = arial_font.render("Vie :", True, (255, 255, 255))
    fenetre.blit(life_text, [10, 385])
    fenetre.blit(lifehero_text, [53, 385])

    xphero_text = arial_font.render(str(perso.xp), True, (255, 255, 255))
    xp_text = arial_font.render("Xp :", True, (255, 255, 255))
    fenetre.blit(xphero_text, [140, 385])
    fenetre.blit(xp_text, [100, 385])

    lvlhero_text = arial_font.render(str(perso.niveau), True, (255, 255, 255))
    lvl_text = arial_font.render("Niveau :", True, (255, 255, 255))
    fenetre.blit(lvlhero_text, [267, 385])
    fenetre.blit(lvl_text, [185, 385])

    forcehero_text = arial_font.render(str(perso.force), True, (255, 255, 255))
    force_text = arial_font.render("Force :", True, (255, 255, 255))
    fenetre.blit(forcehero_text, [360, 385])
    fenetre.blit(force_text, [290, 385])

    if zone == 2:
        money_text = arial_font_money.render(str(perso.argent), True, (255, 255, 255))
        fenetre.blit(money_text, [40, 0])

    combat_text = arial_font_2.render("COMBAT", True, (255, 255, 255))
    if combat == True:
        fenetre.blit(combat_text, [130, 70])

    gagner_text = arial_font_2.render("Vous avez gagné le combat !", True, (255, 255, 255))
    if perso2.estMort() == True:
        if zone == 4:
            fenetre.blit(gagner_text, [10, 70])


    pygame.display.flip()
    clock.tick(60)
pygame.quit()

