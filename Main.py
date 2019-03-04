import pygame
from pygame.locals import *
import time
import random
import os
import operator
from Ressources.Classes.Elements import *
from tkinter import *


pygame.init()


class Cell :
    """Classe de type cellule avec les fonctions usuelles
        NECESSITE PYGAME
        
        """

    def __init__(self, x, y) :
        
        (largeur, hauteur) = (5,5)################################################
        
        self.pos = (x,y)
        self.stat = False #Statut de la cellule (Vivante ou morte)
        self.zone = pygame.Rect((x,y),(largeur,hauteur)) #Permet de connaitre la zone de la cellule (position et taille)
        self.surf = pygame.Surface(self.zone.size) # Objet affichable de la cellule
        self.aff = self.surf , self.zone 
        self.check = False # Marqueur de 'check' de la cellule (permet de savoir si l'algorithme à déjà calculé l'état de la cellu
        self.element = None

    def fill(self,i,j) :
        """Actualise la couleur de la cellule"""
        
        NOIR = (0,0,0)
        if not self.stat :
            self.surf.fill(NOIR)

        else :
            self.surf.fill(self.element.color)
            

    def chkup(self) :
        '''Change le statut 'check' de la cellule'''
        
        if self.check :
            self.check = False
        else :
            self.check = True


class Grille :
    '''Classe du damier, permet le calcul de la génération suivante'''

    def __init__(self,grille) :
        
        self.gr = grille
        self.alv = []
        self.chktmp = []
        self.past_alv = []
        
    def afill(self) :
        for k in self.alv :
            self.gr[k.posi][k.posj].fill(k.posi,k.posj)
            
    def next(self) :
        '''Passe à la génération suivante'''
        global tour, Num_gen
        self.past_alv = list(self.alv)
        
        for k in self.past_alv :
            i,j = k.posi,k.posj
            
            if (not self.gr[i][j].check) and (k.group != 'Solid') :
                k.dep()
                
            
        for k in self.past_alv : # on uncheck toutes les cellules
            i,j = k.posi,k.posj
            self.gr[i][j].check = False
            if i == 0 or i == (len(self.gr)-1) or j == 0 or j == (len(self.gr[0])-1) :
                k.kill()
            

        for k in self.alv : # on uncheck toutes les cellules
            i,j = k.posi,k.posj
            self.gr[i][j].check = False
            if i == 0 or i == (len(self.gr)-1) or j == 0 or j == (len(self.gr[0])-1) :
                k.kill()
                
        
        
        Num_gen=1

    def alea(self):
        i=1
    def save(self):
        i=1
    def charger (self):
        i=1

        
def Affichage_plateau() :
    global Plateau
    global fenetre
    Plateau.afill()
    for k in Plateau.alv :
        i,j = k.posi,k.posj
        fenetre.blit(Plateau.gr[i][j].aff[0],Plateau.gr[i][j].aff[1])


#Cara damier 

pos_x, pos_y =55,205
scale = 5
nb_i = 78
nb_j = 240

#Damier

tabl = []
for i in range(nb_i) :
    soutab = []
    for j in range(nb_j) :#######
        soutab.append(Cell(scale*j + pos_x, scale*i + pos_y))##################################
    tabl.append(soutab)


Plateau = Grille(tabl)
for i in range(len(Plateau.gr)) :
    for j in range(len(Plateau.gr[0])) :
        if i == 1 or i == len(Plateau.gr)-2 or j == 1 or j == len(Plateau.gr[0])-2 :
            Plateau.gr[i][j].element = Marble(i,j,Plateau)
                                    
    

#-----------------------------------Affichage-assignation des variables-----------------------------------------
fenetre = pygame.display.set_mode((1340,675))

RED = (255,0,0) #Définitions de couleurs usuelles
GREEN = (0,255,0)
GRIS = (150,150,150)
NOIR = (0,0,0)
PALE = (50,50,50)


autoplay = 0
Affichage = True #Variable si on affiche ou non le plateau
appuyeG = 0
appuyeD = 0
tour=0 #Variable pour tuer les cellules dans le mode non tore
Num_gen=1 #Variable désignant le numéro de la génération
Num_ite=1 #Nombre d'iteration manuelle
font=pygame.font.Font(None, 24) #On définit la police et la taille d'écriture
pygame.display.flip()
c_element = Marble
ind_elem = 0
entite = 0
mouse_pos = (0,0)
pushA = 0
slowmo = False
radius = 1
clock = pygame.time.Clock()





#-----------------------------------------Définition des boutons----------------------------------------------------

#BOUTON CHANGER ELEM
Changeelem = font.render("Changer d'élement",1,(255,255,255)) #J'arrive à court de synonymes ...
zone_clic_E = Changeelem.get_rect(topleft=(53, 180))

#ENTITE
message_entite = font.render("Nombre entités : ", 1,(255,255,255))

#---------------------------------------------------------------------------------------------------------------------

#FENETRE EVOLUTION DU JEU

zone_ext = pygame.Rect((50,200),((nb_j)*scale+10,(nb_i)*scale+10)) #Zone du rect ext
zone_int = pygame.Rect((55,205),((nb_j)*scale,(nb_i)*scale))

rect_ext = pygame.Surface(zone_ext.size) #Definition du rect ext
rect_int = pygame.Surface(zone_int.size)
rect_ext.fill(GRIS) # couleur du rect ext
rect_int.fill(PALE)

#############################

def Cursorpos(p) :
    (y,x) = p
    return (int((x-pos_y)/scale),int((y-pos_x)/scale))


#Boucle programme
continuer = True

while continuer:
    
    

    entite = font.render(str(len(Plateau.alv)), 1, (255,255,255))
    Matiere = font.render(c_element(3.1415,3.1415,None).name, 1, (255,255,255))
    if appuyeG :
            (i,j) = Cursorpos(mouse_pos)
            if zone_int.collidepoint(mouse_pos) :
                for ri in range(radius) :
                    for rj in range(radius) :
                        if i+ri > len(Plateau.gr) or i+ri < 0 :
                            Is = 0
                        else :
                            Is = ri

                        if j+rj > len(Plateau.gr[1]) or j+rj < 0 :
                            Js =0
                        else :
                            Js = rj
                            
                        if not Plateau.gr[i+Is][j+Js].stat:

                            Plateau.gr[i+Is][j+Js].element = c_element(i+Is,j+Js,Plateau)
                        

    if appuyeD :
            (i,j) = Cursorpos(mouse_pos)
            if zone_int.collidepoint(mouse_pos) :
                for ri in range(radius) :
                    for rj in range(radius) :
                        if i+ri > len(Plateau.gr) or i+ri < 0 :
                            Is = 0
                        else :
                            Is = ri

                        if j+rj > len(Plateau.gr[1]) or j+rj < 0 :
                            Js =0
                        else :
                            Js = rj
                            
                        if Plateau.gr[i+Is][j+Js].stat:

                            Plateau.gr[i+Is][j+Js].element.kill()
                            
    if slowmo :
        if s < 1 :
            s += 0.005

        time.sleep(s)


    for event in pygame.event.get():

        if event.type == pygame.QUIT: #Fermer le programme
            continuer = False
        if event.type == MOUSEMOTION :
            mouse_pos = event.pos
        if appuyeG :
            (i,j) = Cursorpos(mouse_pos)
            if zone_int.collidepoint(mouse_pos) :
                for ri in range(radius) :
                    for rj in range(radius) :
                        if i+ri > len(Plateau.gr) or i+ri < 0 :
                            Is = 0
                        else :
                            Is = ri

                        if j+rj > len(Plateau.gr[1]) or j+rj < 0 :
                            Js =0
                        else :
                            Js = rj
                            
                        if not Plateau.gr[i+Is][j+Js].stat:

                            Plateau.gr[i+Is][j+Js].element = c_element(i+Is,j+Js,Plateau)
                                      
        if appuyeD :
            (i,j) = Cursorpos(mouse_pos)
            if zone_int.collidepoint(mouse_pos) :
                for ri in range(radius) :
                    for rj in range(radius) :
                        if i+ri > len(Plateau.gr) or i+ri < 0 :
                            Is = 0
                        else :
                            Is = ri

                        if j+rj > len(Plateau.gr[1]) or j+rj < 0 :
                            Js =0
                        else :
                            Js = rj
                            
                        if Plateau.gr[i+Is][j+Js].stat:

                            Plateau.gr[i+Is][j+Js].element.kill()


        if event.type == MOUSEBUTTONDOWN :
            if event.button == 3 :
                appuyeD = True
                
                
            if event.button == 1 :
                appuyeG = True

            if event.button == 2 :
                (i,j) = Cursorpos(mouse_pos)
                c = Plateau.gr[i][j]
                print("<----------Debug-----------> \nCell : ",(i,j))
                print("Stat : ",c.stat)
                print("Elem : ",c.element)
                print("Check : ",c.check)
                print("In alv : ",c.element in Plateau.alv)
                if c.element != None and c.element.group != "Solid" :
                    print( "Near : ", c.element.near)



            
               
                           
        if event.type == MOUSEBUTTONUP : # relachement bouton
            if event.button == 3 :
                appuyeD = False
                
        
            if event.button == 1 : #clic gauche
                appuyeG = False


                if zone_clic_E.collidepoint(event.pos) :
                    menu = Tk()
                    var_choix = StringVar()

                    liste = Listbox(menu)
                    liste.pack()
                    for e in Elemlist : 
                        liste.insert(END,e(3.1415,3.1415,Plateau).name)
                    
                    def clic(evt):
                        global ind_elem
                        ind_elem = liste.curselection()[0]
                        menu.destroy()
                        
                    liste.bind('<ButtonRelease-1>',clic)
                    menu.mainloop()

                    c_element = Elemlist[ind_elem]
                    

        if event.type == KEYUP :
            if event.key == K_SPACE :
                if autoplay :
                    autoplay = False
                else :
                    autoplay = True

            if event.key == K_s :
                    slowmo = False

            if event.key == K_r :
                radius = 1

        if event.type == KEYDOWN :
            if event.key == K_s :
                s = 0
                slowmo = True
            if event.key == K_r :
                radius = 3
        
    
                    
                
    pygame.display.flip()

    if autoplay :
        Plateau.next()
        time.sleep(0.002)
    fenetre.fill((100,100,100)) # on efface l'écran

    fenetre.blit(Changeelem, zone_clic_E)
    fenetre.blit(Matiere, (900,183))
    fenetre.blit(message_entite, (1100,183))
    fenetre.blit(entite, (1240,183))
    fenetre.blit(rect_ext, zone_ext)# on print le rect ext à la zone du rect ext
    fenetre.blit(rect_int, zone_int)

    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
    fenetre.blit(fps, (50, 50))

    Affichage_plateau()


    pygame.display.flip()

    clock.tick(30)


pygame.quit()
