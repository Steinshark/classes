import random


filename = "names"
distincts = list()
for name in open("names","r").readlines():
     distincts.append(name.split(",")[0])


bimmy = open("nameBig","w")

for i in range(0,int(input("number of names"))):
    bimmy.write(str(distincts[random.randint(0,len(distincts)-1)]) + "\n")

bimmy.close()
