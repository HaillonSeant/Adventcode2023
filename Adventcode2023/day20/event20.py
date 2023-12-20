import sys
import time
from collections import deque
f=open("input.txt","r")
data=f.read().strip().split("\n")
f.close()
class Flipflop:
    def __init__(self):
        self.name=""
        self.etat=0#0 pour off
        self.queue=deque()#signale a traiter
        self.liaison=[]#liste des flipflop et liste des conjunctions
    def changement(self):
        # print(self.name)
        signal=self.queue.popleft()
        if signal[0] == 0:
            if self.etat == 0:#off
                self.etat=1#on
                self.send((1,self.name))#high
                lipu[1]+=len(self.liaison)
            else:#on
                self.etat=0#off
                self.send((0,self.name))#low
                lipu[0]+=len(self.liaison)
            # return self.liaison
        # return []    
    def send(self,signal):
        for dest in self.liaison:
            dico[dest].queue.append(signal)#on envoie a tout le monde
class Conjunction:
    def __init__(self):
        self.name=""
        self.dicoetat={}
        self.dicoetat["broad"]=1#erengistrement des inputs
        self.queue=deque()
        self.liaison=[]
    def changement(self):
        signal=self.queue.popleft()
        self.dicoetat[signal[1]]=signal[0]
        if 0 not in self.dicoetat.values():
            self.send((0,self.name))
            lipu[0]+=len(self.liaison)
        else:
            self.send((1,self.name))
            lipu[1]+=len(self.liaison)
            if self.name=="jz":#modif a la main pour trouver les boucles
                compt[0]+=1
    def send(self,signal):
        for dest in self.liaison:
            if dest != 'rx':
                dico[dest].queue.append(signal)
def recupdata(data):
    dicomodule={}
    licon=[]
    for line in data[1:]:
        if line[0]=="%":
            flip=Flipflop()
            flip.name=line[1:3]
            flip.etat=0
            for liaison in line[line.index(">")+1:].replace(" ","").split(","):
                flip.liaison.append(liaison)
            dicomodule[flip.name]=flip
        else:
            con=Conjunction()
            con.name=line[1:3]
            for liaison in line[line.index(">")+1:].replace(" ","").split(","):
                con.liaison.append(liaison)
            dicomodule[con.name]=con
            licon.append(con.name)
    for val in dicomodule.values():
        for liaison in val.liaison:
            if liaison in licon:
                dicomodule[liaison].dicoetat[val.name]=0
    return dicomodule
def button(dico):
    for name in broad:
        dico[name].queue.append((0,"broad"))
    run=True
    while run:
        run=False
        for val in dico.values():
            if len(val.queue)!=0:
                run=True
                fini = val.changement()
start=time.time()
broad=data[0][data[0].index(">")+1:].replace(" ","").split(",")
dico=recupdata(data)
t=1000
lipu=[0,0]
while t>0:
    button(dico)
    lipu[0]+=5
    t-=1
print(lipu[0]*lipu[1])
end=time.time()
print(end-start)
start=time.time()
dico=recupdata(data)
compt=[0]
#xm relier que a ng,sv,ft,jz
while True:
    t+=1
    button(dico)
    if compt[0]==1:
        print(t)
        break
    compt[0]=0
#valeur trouver ng=3803 sv=3889 ft=3877 jz=3917 application du ppcm(fonction du day8 utilisé)