import random
class Powder() :

    def __init__(self,P,i,j,density) :
        '''(self,P,i,j,<density>)'''

        self.posi = i
        self.posj = j
        self.group = 'Dust'
        self.permeability = False
        self.divecounter = False
        self.Plateau = P
        self.density = density
        self.near = []
        
    def kill(self) :
        i = self.posi
        j = self.posj
        
        self.Plateau.gr[i][j].element = None
        self.Plateau.gr[i][j].stat = False
        if self in self.Plateau.past_alv :
            self.Plateau.past_alv.remove(self)
        self.Plateau.alv.remove(self)

    def scan(self):
        i = self.posi
        j = self.posj
        self.near = []

        for Is in range(-1,2) :
            for Js in range(-1,2) :
                if (Is,Js) != (0,0) :
                    if self.Plateau.gr[i+Is][j+Js].stat and type(self.Plateau.gr[i+Is][j+Js].element) != type(self) and self.Plateau.gr[i+Is][j+Js].element in self.Plateau.past_alv :
                        self.near.append((i+Is,j+Js))

    def gravity(self) :
        i = self.posi
        j = self.posj
        
        self.posi = i+1
        self.Plateau.gr[i+1][j].check = True
        self.Plateau.gr[i+1][j].element = self
        self.Plateau.gr[i+1][j].stat = True
        self.Plateau.gr[i][j].element = None
        self.Plateau.gr[i][j].stat = False
                
    def spread(self) :
        i = self.posi
        j = self.posj

        if random.random() > 0.5 :
            
            if not self.Plateau.gr[i+1][j-1].stat and (not self.Plateau.gr[i][j-1].stat or self.Plateau.gr[i][j-1].element.permeability) :
                self.posi,self.posj = i+1, j-1
                self.Plateau.gr[i][j].element = None
                self.Plateau.gr[i][j].stat = False
                self.Plateau.gr[i+1][j-1].stat = True
                self.Plateau.gr[i+1][j-1].element = self
                self.Plateau.gr[i+1][j-1].check = True

                
            elif self.Plateau.gr[i+1][j-1].stat and self.Plateau.gr[i+1][j-1].element.density < self.density and (not self.Plateau.gr[i][j-1].stat or (self.Plateau.gr[i][j-1].element.group != "Solid" or self.Plateau.gr[i][j-1].element.permeability)) :
                self.posi,self.posj = i+1, j-1
                self.Plateau.gr[i+1][j-1].element.posi,self.Plateau.gr[i+1][j-1].element.posj = i,j
                self.Plateau.gr[i][j].element = self.Plateau.gr[i+1][j-1].element
                self.Plateau.gr[i][j].check = True
                self.Plateau.gr[i+1][j-1].element = self
                self.Plateau.gr[i+1][j-1].check = True
                

            elif not self.Plateau.gr[i+1][j+1].stat and (not self.Plateau.gr[i][j+1].stat or self.Plateau.gr[i][j+1].element.permeability) :
                self.posi,self.posj = i+1, j+1
                self.Plateau.gr[i][j].element = None
                self.Plateau.gr[i][j].stat = False
                self.Plateau.gr[i+1][j+1].stat = True
                self.Plateau.gr[i+1][j+1].element = self
                self.Plateau.gr[i+1][j+1].check = True

            elif self.Plateau.gr[i+1][j+1].stat and self.Plateau.gr[i+1][j+1].element.density < self.density and (not self.Plateau.gr[i][j+1].stat or (self.Plateau.gr[i][j+1].element.group != "Solid" or self.Plateau.gr[i][j+1].element.permeability)) :
                self.posi,self.posj = i+1, j+1
                self.Plateau.gr[i+1][j+1].element.posi,self.Plateau.gr[i+1][j+1].element.posj = i,j
                self.Plateau.gr[i][j].element = self.Plateau.gr[i+1][j+1].element
                self.Plateau.gr[i][j].check = True
                self.Plateau.gr[i+1][j+1].element = self
                self.Plateau.gr[i+1][j+1].check = True
        else :

            if not self.Plateau.gr[i+1][j+1].stat and (not self.Plateau.gr[i][j+1].stat or self.Plateau.gr[i][j+1].element.permeability) :
                self.posi,self.posj = i+1, j+1
                self.Plateau.gr[i][j].element = None
                self.Plateau.gr[i][j].stat = False
                self.Plateau.gr[i+1][j+1].stat = True
                self.Plateau.gr[i+1][j+1].element = self
                self.Plateau.gr[i+1][j+1].check = True

            elif self.Plateau.gr[i+1][j+1].stat and self.Plateau.gr[i+1][j+1].element.density < self.density and (not self.Plateau.gr[i][j+1].stat or (self.Plateau.gr[i][j+1].element.group != "Solid" or self.Plateau.gr[i][j+1].element.permeability)) :
                self.posi,self.posj = i+1, j+1
                self.Plateau.gr[i+1][j+1].element.posi,self.Plateau.gr[i+1][j+1].element.posj = i,j
                self.Plateau.gr[i][j].element = self.Plateau.gr[i+1][j+1].element
                self.Plateau.gr[i][j].check = True
                self.Plateau.gr[i+1][j+1].element = self
                self.Plateau.gr[i+1][j+1].check = True

            elif not self.Plateau.gr[i+1][j-1].stat and (not self.Plateau.gr[i][j-1].stat or self.Plateau.gr[i][j-1].element.permeability) :
                self.posi,self.posj = i+1, j-1
                self.Plateau.gr[i][j].element = None
                self.Plateau.gr[i][j].stat = False
                self.Plateau.gr[i+1][j-1].stat = True
                self.Plateau.gr[i+1][j-1].element = self
                self.Plateau.gr[i+1][j-1].check = True
                
            elif self.Plateau.gr[i+1][j-1].stat and self.Plateau.gr[i+1][j-1].element.density < self.density and (not self.Plateau.gr[i][j-1].stat or (self.Plateau.gr[i][j-1].element.group != "Solid" or self.Plateau.gr[i][j-1].element.permeability)) :
                self.posi,self.posj = i+1, j-1
                self.Plateau.gr[i+1][j-1].element.posi,self.Plateau.gr[i+1][j-1].element.posj = i,j
                self.Plateau.gr[i][j].element = self.Plateau.gr[i+1][j-1].element
                self.Plateau.gr[i][j].check = True
                self.Plateau.gr[i+1][j-1].element = self
                self.Plateau.gr[i+1][j-1].check = True

    def dive(self) :
        i = self.posi
        j = self.posj

        if self.Plateau.gr[i+1][j].element.density < self.density :
            self.posi= i+1
            self.Plateau.gr[i+1][j].element.posi = i
            self.Plateau.gr[i][j].element = self.Plateau.gr[i+1][j].element
            self.Plateau.gr[i+1][j].element = self
            self.Plateau.gr[i+1][j].check = True
            self.Plateau.gr[i][j].check = True

            self.divecounter = True

    def dep(self) :
        i = self.posi
        j = self.posj

        if not self.Plateau.gr[i+1][j].stat : #Si il n'y a pas d'élement en dessous
            self.gravity()

        else :
            if not self.Plateau.gr[i+1][j].check and self.Plateau.gr[i+1][j].element.group != 'Solid':
                self.Plateau.gr[i+1][j].element.dep() #On actualise la cellule du dessous

            if self.interaction() != True :

                if not self.Plateau.gr[i+1][j].stat :
                    self.gravity()

                elif self.Plateau.gr[i+1][j].element.group == 'Solid' :
                    self.spread()
                    
                elif self.Plateau.gr[i+1][j].element.group == 'Dust' :
                    self.dive()
                    if not self.divecounter :
                        self.spread()
                    self.divecounter = False
                    
                elif self.Plateau.gr[i+1][j].element.group == 'Liquid' :
                    self.dive()
                    if not self.divecounter :
                        self.spread()
                    self.divecounter = False
   
        self.Plateau.gr[i][j].check = True