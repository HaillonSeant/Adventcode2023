import sys
from time import time as ti
start=ti()
data=open(sys.argv[1],"r").read().strip().split('\n')
data = list(filter(("").__ne__, data))
liseed=[]
dico_seed_to_soil={}
dico_soil_to_fertilizer={}
dico_fertilizer_to_water={}
dico_water_to_light={}
dico_light_to_temp={}
dico_temp_to_humidity={}
dico_humidity_to_location={}
def Recupdata(data):
	liseed=data[0][data[0].index(":")+2:].split(" ")
	for i in range(2,len(data)):
		if data[i][0].isdigit():
			num=data[i].split(" ")
			dico_seed_to_soil[(int(num[1]),int(num[1])+int(num[2])-1)]=int(num[0])-int(num[1])
		else:
			break
	
	for i in range(i+1,len(data)):
		if data[i][0].isdigit():
			num=data[i].split(" ")
			dico_soil_to_fertilizer[(int(num[1]),int(num[1])+int(num[2])-1)]=int(num[0])-int(num[1])
		else:
			break
	
	for i in range(i+1,len(data)):
		if data[i][0].isdigit():
			num=data[i].split(" ")
			dico_fertilizer_to_water[(int(num[1]),int(num[1])+int(num[2])-1)]=int(num[0])-int(num[1])
		else:
			break
	
	for i in range(i+1,len(data)):
		if data[i][0].isdigit():
			num=data[i].split(" ")
			dico_water_to_light[(int(num[1]),int(num[1])+int(num[2])-1)]=int(num[0])-int(num[1])
		else:
			break
	
	for i in range(i+1,len(data)):
		if data[i][0].isdigit():
			num=data[i].split(" ")
			dico_light_to_temp[(int(num[1]),int(num[1])+int(num[2])-1)]=int(num[0])-int(num[1])
		else:
			break
	
	for i in range(i+1,len(data)):
		if data[i][0].isdigit():
			num=data[i].split(" ")
			dico_temp_to_humidity[(int(num[1]),int(num[1])+int(num[2])-1)]=int(num[0])-int(num[1])
		else:
			break
	
	for i in range(i+1,len(data)):
		if data[i][0].isdigit():
			num=data[i].split(" ")
			dico_humidity_to_location[(int(num[1]),int(num[1])+int(num[2])-1)]=int(num[0])-int(num[1])

	return liseed
def Find_min():
	min=int()
	first=True
	for seed in liseed:
		seed=int(seed)
		for inter in dico_seed_to_soil.keys():
			if inter[0]<=seed and seed<=inter[1]:
				seed=seed+dico_seed_to_soil[inter]
				break
		
		for inter in dico_soil_to_fertilizer.keys():
			if inter[0]<=seed and seed<=inter[1]:
				seed=seed+dico_soil_to_fertilizer[inter]
				break
		
		for inter in dico_fertilizer_to_water.keys():
			if inter[0]<=seed and seed<=inter[1]:
				seed=seed+dico_fertilizer_to_water[inter]
				break
		
		for inter in dico_water_to_light.keys():
			if inter[0]<=seed and seed<=inter[1]:
				seed=seed+dico_water_to_light[inter]
				break
		
		for inter in dico_light_to_temp.keys():
			if inter[0]<=seed and seed<=inter[1]:
				seed=seed+dico_light_to_temp[inter]
				break
		
		for inter in dico_temp_to_humidity.keys():
			if inter[0]<=seed and seed<=inter[1]:
				seed=seed+dico_temp_to_humidity[inter]
				break
		
		for inter in dico_humidity_to_location.keys():
			if inter[0]<=seed and seed<=inter[1]:
				seed=seed+dico_humidity_to_location[inter]
				break	
		if first:
			min=seed
			first=False
		else:
			if seed<min:
				min=seed
	return min
def Crea_inter_seed():
	tmp=[]
	for i in range(0,len(liseed)-1,2):
		tmp.append((int(liseed[i]),int(liseed[i])+int(liseed[i+1])-1))
	return tmp
def Crea_inter(inter_base):
	li_inter=list()
	keys=list(dico_temp_to_humidity)
	keys=Dans_lordre(keys)
	for inter in keys:
		if inter_base[0]<inter[0]:#{[}]
			if inter_base[1]<inter[1]:
					li_inter.append((inter_base[0],inter[1]))
					
	return
def Dans_lordre(keys):
	#bourrin
	mini=keys[0][0]
	min_inter=keys[0]
	tmp=[]
	while True:
		for inter in keys[1:]:
			start=inter[0]
			if start<mini:
				mini=start
				min_inter=inter
		tmp.append(min_inter)
		keys.remove(min_inter)
		if len(keys)==0:
			return tmp
		mini=keys[0][0]
		min_inter=keys[0]

#JE SUIS TROP NAIF
# def Create_range(liseed):
# 	tmp=list()
# 	for i in range(0,len(liseed)-1,2):
# 		for i in range(int(liseed[i]),int(liseed[i])+int(liseed[i+1])):
# 			tmp.append(i)
# 	return tmp
# def Create_range(liseed):
#solution test = 42
liseed=Recupdata(data)
# soluce=Find_min()
# print('premiere partie : ',ti()-start)
# print(soluce,"\n")
# start=ti()
liseed=Crea_inter_seed()
keys=list(dico_light_to_temp)
keys=Dans_lordre(keys)
print(keys)
# print('seconde partie : ',ti()-start)
Crea_inter("a")
