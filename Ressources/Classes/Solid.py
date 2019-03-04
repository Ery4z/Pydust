import random
class Solid() :

    def __init__(self,P,i,j,density) :
        '''(self,P,i,j,<density>)'''

        self.posi = i
        self.posj = j
        self.group = 'Solid'
        self.Plateau = P
        self.density = density

    def kill(self) :
        i = self.posi
        j = self.posj
        
        self.Plateau.gr[i][j].element = None
        self.Plateau.gr[i][j].stat = False
        if self in self.Plateau.past_alv :
            self.Plateau.past_alv.remove(self)
        self.Plateau.alv.remove(self)