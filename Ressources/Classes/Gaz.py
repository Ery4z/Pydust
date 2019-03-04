import random

class Gaz() :

    def __init__(self,P,i,j,density) :
        '''(self,P,i,j,<density>)'''

        self.posi = i
        self.posj = j
        self.group = 'Gaz'
        self.permeability = False
        self.divecounter = False
        self.Plateau = P
        self.speed = [0,0]
        self.nm = False
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
                    if self.Plateau.gr[i+Is][j+Js].stat :
                        self.near.append((i+Is,j+Js))

    def move(self) :
        i,j = self.posi,self.posj

        self.Plateau.gr[i][j].stat = False
        self.Plateau.gr[i][j].element = None
        self.Plateau.gr[i][j].check = True

        self.posi,self.posj = i + self.speed[0], j + self.speed[1]
        
        i,j = self.posi,self.posj

        self.Plateau.gr[i][j].stat = True
        self.Plateau.gr[i][j].element = self
        self.Plateau.gr[i][j].check = True
        

    def calcspeed(self) :
        i = self.posi
        j = self.posj
        gr = self.Plateau.gr
        modi = len(gr)
        modj = len(gr[1])
        
        HH = False
        HB = False
        HD = False
        HG = False
        HHD = False
        HHG = False
        HBD = False
        HBG = False

        self.Near = []

        for Is in range(-1,2) :
            for Js in range(-1,2) :
                if (Is,Js) != (0,0) :
                    if gr[(i+Is)%modi][(j+Js)%modj].stat :
                        self.Near.append((Is,Js))
                        if Is < 0 :
                            if Js == 0:
                                HH = True
                                continue
                            if Js == -1 :
                                HHG = True
                                continue
                            if Js == 1 :
                                HHD = True
                                continue


                        elif Is > 0 :
                            if Js == 0:
                                HB = True
                                continue
                            if Js == -1 :
                                HBG = True
                                continue
                            if Js == 1 :
                                HBD = True
                                continue


                        if Js < 0 and Is == 0:
                            HG = True
                            continue

                        elif Js > 0 and Is == 0 :
                            HD = True
                            continue

                    
            
        for q in self.Near :
            self.speed[0],self.speed[1] = self.speed[0]-q[0],self.speed[1]-q[1]

        if self.speed[0] != 0 :
            self.speed[0] = int(self.speed[0]/abs(self.speed[0]))
        if self.speed[1] != 0 :
            self.speed[1] = int(self.speed[1]/abs(self.speed[1]))

        if HH and self.speed[0] < 0 :
            self.speed[0] = 0
        if HB and self.speed[0] > 0 :
            self.speed[0] = 0
        if HD and self.speed[1] > 0 :
            self.speed[1] = 0
        if HG and self.speed[1] < 0 :
            self.speed[1] = 0
        if HHD and self.speed == [-1,1] :
            self.speed = [0,0]
        if HHG and self.speed == [-1,-1] :
            self.speed = [0,0]
        if HBD and self.speed == [1,1] :
            self.speed = [0,0]
        if HBG and self.speed == [1,-1] :
            self.speed = [0,0]



        


        self.Plateau.gr[i][j].check = True

        '''for q in Near :
            if gr[i+q[0]][j+q[1]].element.group == 'Gaz' and not gr[i+q[0]][j+q[1]].check :
                gr[i+q[0]][j+q[1]].element.calcspeed()'''

    def therm(self) : #Agitation thermique
        gr = self.Plateau.gr
        i = self.posi
        j = self.posj
        modi = len(gr)
        modj = len(gr[1])
        Free = [(-1,-1),(-1,0),(-1,1),
        (0,-1),(0,0),(0,1),
        (1,-1),(1,0),(1,1)]
        self.Near = []

        for Is in range(-1,2) :
            for Js in range(-1,2) :
                if (Is,Js) != (0,0) :
                    if gr[(i+Is)%modi][(j+Js)%modj].stat :
                        self.Near.append((Is,Js))

        for q in self.Near :
            Free.remove(q)

        if len(Free) != 0 :
            q = random.choice(Free)
            self.posi += q[0]
            self.posj += q[1]
            gr[i][j].element = None
            gr[i][j].stat = False
            gr[i][j].check = False

        i = self.posi
        j = self.posj
        gr[i][j].element = self
        gr[i][j].stat = True
        gr[i][j].check = True


    def dep(self) :
        i = self.posi
        j = self.posj

        self.nm = True
        self.calcspeed()

        self.move()
        self.therm()

        self.interaction()

        self.nm = False
        self.Plateau.gr[i][j].check = True