#Arapova 
#Baurzhan
string = str(input())
upper = 0
lower = 0
for i in string:
    if i.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(string.upper())
else:
    print(string.lower())


#2
a = input("a = ")
b = input("b = ")
while not(a.isdigit() and b.isdigit()):
  a = input("a = ")
  b = input("b = ")
print("Zhayaby = ", (int(a) + int(b)))
#355
#Assylzhan Arapova git hub-ta ozgeris zhasaidy. Bugin 11.04.23