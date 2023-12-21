import sys
import time
start=time.time()
f=open(sys.argv[1],'r')
grille=f.read().strip().split('\n')
f.close()
end = time.time()
print("Time to read the file : " + str(end - start))
def startpos(grille):
    for i in range(len(grille)):
        for i2 in range(len(grille[i])):
            if grille[i][i2]=="S":
                grille[i]=grille[i][0:i2]+"."+grille[i][i2+1:]#on retire le S
                return (i,i2)
def step(lipos):
    nsetpos=set()
    for pos in setpos:
        y=pos[0]
        x=pos[1]
        if y-1>=0 and grille[y-1][x]==".":
            nsetpos.add((y-1,x))
        if y+1<len(grille) and grille[y+1][x]==".":
            nsetpos.add((y+1,x))
        if x-1>=0 and grille[y][x-1]==".":
            nsetpos.add((y,x-1))
        if x+1<len(grille) and grille[y][x+1]==".":
            nsetpos.add((y,x+1))
    return nsetpos
solutionStart = time.time()
setpos={startpos(grille)}
t=64
while t>0 :
    setpos=step(setpos)
    t-=1
print(len(setpos))
end = time.time()
print("Part 1 : ", )
print("Solution 1 time : " + str(end - solutionStart)+"\n")