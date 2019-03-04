from Ressources.Classes.Liquid import *
from Ressources.Classes.Powder import *
from Ressources.Classes.Solid import *
from Ressources.Classes.Gaz import *
import random
'''
To add new elem don't forget to add them to the list at the end
'''


class Marble(Solid) :

    def __init__(self,i,j,P) :
        self.name = 'Marbre'
        self.color = (225,247,253)
        density = 1000
        self.permeability = False

        Solid.__init__(self,P,i,j,density)
        if (i,j) != (3.1415,3.1415) :
            
            self.Plateau.gr[i][j].stat = True
            self.Plateau.alv.append(self)

class Sand(Powder) :

    def __init__(self,i,j,P) :
        self.name = 'Sable'
        self.color = (236,183,111)
        density = 2

        Powder.__init__(self,P,i,j,density)
        if (i,j) != (3.1415,3.1415) :
            self.Plateau.gr[i][j].stat = True
            self.Plateau.gr[i][j].check = False
            self.Plateau.alv.append(self)
        
    def interaction(self) :
        return()

class Salt(Powder) :

    def __init__(self,i,j,P) :
        self.name = 'Sel'
        self.color = (182,208,231)
        density = 1.2

        Powder.__init__(self,P,i,j,density)
        if (i,j) != (3.1415,3.1415) :
            self.Plateau.gr[i][j].stat = True
            self.Plateau.gr[i][j].check = False
            self.Plateau.alv.append(self)
        
    def interaction(self) :
        self.scan()
        eligible = []
        for p in self.near :
            if type(self.Plateau.gr[p[0]][p[1]].element) == Water :
                eligible.append(p)
        if eligible != [] :
            s = random.choice(eligible)
            self.Plateau.gr[s[0]][s[1]].element.kill()
            self.Plateau.gr[s[0]][s[1]].element = SaltWater(s[0],s[1],self.Plateau)
            self.kill()
            return(True)

class Water(Liquid) :

    def __init__(self,i,j,P) :
        self.name = 'Eau'
        self.color = (62,211,255)
        density = 1

        Liquid.__init__(self,P,i,j,density)
        if (i,j) != (3.1415,3.1415) : #Permet d'eviter la création pour recup le nom
            self.Plateau.gr[i][j].stat = True
            self.Plateau.gr[i][j].check = False
            self.Plateau.alv.append(self)
        
    def interaction(self) :
        return()

class SaltWater(Liquid) :

    def __init__(self,i,j,P) :
        self.name = 'Eau salé'
        self.color = (151,232,255)
        density = 0.9

        Liquid.__init__(self,P,i,j,density)
        if (i,j) != (3.1415,3.1415) : #Permet d'eviter la création pour recup le nom
            self.Plateau.gr[i][j].stat = True
            self.Plateau.gr[i][j].check = False
            self.Plateau.alv.append(self)
        
    def interaction(self) :
        return()

class Oil(Liquid) :

    def __init__(self,i,j,P) :
        self.name = 'Pétrole'
        self.color = (107,81,41)
        density = 0.99

        Liquid.__init__(self,P,i,j,density)
        if (i,j) != (3.1415,3.1415) : #Permet d'eviter la création pour recup le nom
            self.Plateau.gr[i][j].stat = True
            self.Plateau.gr[i][j].check = False
            self.Plateau.alv.append(self)
        
    def interaction(self) :
        return()

class H2(Gaz) :

    def __init__(self,i,j,P) :
        self.name = 'Hydrogene'
        self.color = (164,223,255)
        density = 0.1

        Gaz.__init__(self,P,i,j,density)
        if (i,j) != (3.1415,3.1415) : #Permet d'eviter la création pour recup le nom
            self.Plateau.gr[i][j].stat = True
            self.Plateau.gr[i][j].check = False
            self.Plateau.alv.append(self)
        
    def interaction(self) :
        return()

class O2(Gaz) :

    def __init__(self,i,j,P) :
        self.name = 'Oxygene'
        self.color = (245,223,235)
        density = 3

        Gaz.__init__(self,P,i,j,density)

        if (i,j) != (3.1415,3.1415) : #Permet d'eviter la création pour recup le nom
            self.Plateau.gr[i][j].stat = True
            self.Plateau.gr[i][j].check = False
            self.Plateau.alv.append(self)
        
    def interaction(self) :
        return()

Elemlist = [Marble,Sand,Salt,Water,SaltWater,Oil,H2,O2]