#Arapova Assylzhan
#1 for және while циклдарды қолданып жеке программа құру
a = int(input("a="))
i=0
while i<a:
    i+=1
    if i%2==0:
        print(i, "-" ,"Zhyp san")
    else:
        print(i,"-","Taq san")

#Arapova Assylzhan
#1 for және while циклдарды қолданып жеке программа құру
N= int(input("N="))
for i in range (1, N+1):
    if i%2==0:
        print(i, "-" ,"Zhyp san")
    else:
        print(i,"-","Taq san")


#Arapova Assylzhan
#2-3
import random
print(list(range(1, 10)))
print(random.randint(-100, 10))
print(random.randrange(10))
print(random.random())
a = [1, 4, 2, -5, 0, 11]
for e in enumerate(a, 1):
    print(e)

#Arapova Assylzhan
#4
a=int(input("a= "))
b=int(input("b="))
if a>b:
    while a>b:
        a=int(input("a="))
        b=int(input("b="))
for i in range(a,b+1):
    print(i)

#Arapova Assylzhan
a=int(input("a="))
b=int(input("b="))
if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)


#Arapova Assylzhan
n = int(input("Kartalar sany"))
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
   sum -= int(input())
print(sum)

#Arapova Assylzhan
a=int(input())
sum=0
k = 0
while a != 0:
    sum += a
    k += 1
    a = int(input())
print("Summa =", sum,"Sany =", k)