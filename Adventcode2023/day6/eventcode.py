import sys
import time
start = time.time() 
filename=sys.argv[1]
input=open(filename,"r")
lines=input.readlines()
timecourse=[]
distcourse=[]
number=""
for i in range(13,37):
	if lines[0][i].isdigit():
		number+=lines[0][i]
	elif number!="":
		timecourse.append(int(number))
		number=""

for i in range(12,37):
	if lines[1][i].isdigit():
		number+=lines[1][i]
	elif number!="":
		distcourse.append(int(number))
		number=""

def Combienvictoire(time,dist):
	som=0
	for vit in range(1,time):
		if dist < vit*(time-vit):
			som+=1
	return som
som=1
for i in range(4):
	som*=Combienvictoire(timecourse[i],distcourse[i])
print(time.time()-start)
print(som)
timetot=""
disttot=""
for timecourse in timecourse:
	timetot+=str(timecourse)
for dist in distcourse:
	disttot+=str(dist)
timetot=int(timetot)
disttot=int(disttot)
#soluce opti
#vit = t ; t_restant = T-t ; dist = vit*t_restant <=> dist = t*(T-t) = -t^2+T*t 
#avec t le temps avant de relacher le bouton
#il faut que dist>Record => dist-record > 0 
#polynome qui represente le problème est -t^2 + T*t - Record = 0
#on cherche quand le poly est positif, soit entre les 2 racines reels (on suppose que l'input est bien fait)
#puis on ne prends que les entiers dans cette intervalle  soit int(x2)-int(x1) avec x2>x1 les 2 racine reels
squaredelta = (timetot**2-4*disttot)**(1/2)  
x1 = (timetot-squaredelta)/2
x2 = int((timetot+squaredelta)/2)
if isinstance(x1,int): #correection d'un bug possible si x1 est un int
	x1-=1
else:
	x1 = int(x1)
print(x2-x1)
print(time.time()-start)
start=time.time()
som = Combienvictoire(timetot,disttot)
print(som)
print(time.time()-start)