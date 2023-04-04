#Arapova Assylzhan
spisok = {
    "Assylzhan": (5,6,7,8),
    "Aigerim": (9,10,11,12),
    "Uldana": (13,14,15,16),
    "Aiymgul": (15,16,17,18),
    "Symbat": (18,19,1,8),
    "Zhanyl":(25,26,27,28)}


spi = sorted(spisok.items(), key=lambda spisok: spisok[0])
print(spi)

name = str(input("Name: "))
for key in spisok:
    if key == name:
        print(spisok[key])

print("__________________________________________________")
arr = []
san = 1
while san!=0:
    san = int(input("San jaz: "))
    if san !=0:
        arr.append(san)
    
arr.sort()
print("Sort po vozrastaniu: ")
for i in range(len(arr)):
    print(arr[i])

print("Sort po ubivaniu: ")
for i in range(len(arr)):
    print(arr[len(arr)-i-1])

print("__________________________________________________")
import random
ran = []
j = 0
while j!=6:
    daf = True
    rand = random.randint(1,50)
    for i in range(len(ran)-1):
        san1 = ran[i+1]
        if ran[i] == san1:
            daf = False 

    if daf:
        ran.append(rand)
        j+=1

ran.sort()
print(ran)

print("__________________________________________________")

arr = []
san = 1
while san!=0:
    san = int(input("San jaz: "))
    if san !=0:
        arr.append(san)

daf = True
for i in range(len(arr)-1):
    san1 = arr[i+1]
    if arr[i] < san1:
        daf = False 
        break

print(daf)
print(arr)

    

arr.sort()
print("Sort po vozrastaniu: ")
for i in range(len(arr)):
    print(arr[i])