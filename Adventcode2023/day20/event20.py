import sys
import time
from collections import deque
from math import prod
f=open("input.txt","r")
data=f.read().strip().split("\n")
f.close()
###ppc###
def decomp(num):
    lifact=[]
    liexp=[]
    n=2
    t=0
    while num!=1:
        while num%n==0:
            num=num//n
            t+=1
        if t!=0:
            lifact.append(n)
            liexp.append(t)
            t=0
        n+=1
    return [lifact,liexp]
def ppcm(a,b):
    a=decomp(a)
    b=decomp(b)
    p=1
    for i in range(len(a[0])):
        if a[0][i] not in b[0]:
            p*=a[0][i]**a[1][i]
        else:
            if a[1][i]>b[1][b[0].index(a[0][i])]:
                p*=a[0][i]**a[1][i]
            else :
                p*=b[0][b[0].index(a[0][i])]**b[1][b[0].index(a[0][i])]
    for i in range(len(b[0])):
        if b[0][i] not in a[0]:
            p*=b[0][i]**b[1][i]
        else:
            if b[1][i]>a[1][a[0].index(b[0][i])]:
                p*=b[0][i]**b[1][i]
            else :
                p*=a[0][a[0].index(b[0][i])]**a[1][a[0].index(b[0][i])]
    return p
def ppcmmult(li):
    while len(li)!=1:
        a=li.pop()
        b=li.pop()
        li.append(ppcm(a,b))
    return li[0]
###ppcm###
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
        self.last=False
    def changement(self):
        signal=self.queue.popleft()
        self.dicoetat[signal[1]]=signal[0]
        if 0 not in self.dicoetat.values():
            self.send((0,self.name))
            lipu[0]+=len(self.liaison)
        else:
            self.send((1,self.name))
            lipu[1]+=len(self.liaison)
            if self.last:
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
print('Durée Partie 1 :',end-start)
start=time.time()
dico=recupdata(data)
compt=[0]
#xm relier que a ng,sv,ft,jz
dico["ng"].last=True
dico["sv"].last=True
dico["ft"].last=True
dico["jz"].last=True
valid=[]
while True:
    t+=1
    button(dico)
    if compt[0]==1:
        valid.append(t)
    compt[0]=0
    if len(valid)==4:
        break
print(prod(valid))
end=time.time()
print('Durée Partie 2 :',end-start)
