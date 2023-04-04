#Arapova Assylzhan
#1
tuple_5 = (0,2,4,5,6,6)
sets = {1,2,3,4,5,6,7,8,9,10}
print(tuple_5.count(6))
sets.add(6)
print(sets)
sets.pop()
print(sets)
print(len(sets))
print(len(tuple_5))

print(" ")
#2
#1
tuple_1 = (0,1,2,3,4,5)
tuple_2 = (-5,-4,-3,-2,-1,0)
tuple_3 = tuple_1 + tuple_2
print(f"Count: {tuple_3.count(0)}")
print(f"Tuple 3 :   {tuple_3}")

#2
element = (5,(7,(8,("soz",()))))
print(element[1][1][1][1])


countries = (
    ("Germany", 80, (("Berlin",3), ("Hamburg", 1))),
    ("France", 66, (("Paris", 2),("Marsel", 1)))
)
for country in countries:
    countryName, countryPopulation, cities = country
    print("\nCountry: {} population: {}".format(countryName, countryPopulation))
    for city in cities:
        cityName, cityPopulation= city
        print("City: {} population: {}".format(cityName, cityPopulation))
#3
shygyn = ((2500,80,100),(2700,100,100),(3000,100,100),(1000,100,1000),(1500,100,100),(1000,150,120),(8000,80,150))
sum_shugun = 0
for shy in shygyn:
    for shy_2 in shy:
        sum_shugun+=shy_2

print(f"\nShygyn: {sum_shugun}")

#4
name = tuple(input("\nName:").split(" "))
for i in name:
    if 'ва' in i:
        print(i,end=" ")

#5
cyr = ('а','ә','б','в','г','ғ','д','е','ё','ж','з','и','й','к','қ','л','м','н','ң','о','ө','п','р','с','т','у','ұ','ү','ф', 'х', 'һ','ц','ч','ш','щ','ъ','ы','і','ь','э','ю','я')
lat = ('a','a','b','v','g','g','d','e','io','j','z','i','i','k','q','l','m','n','n','o','o','p','r','s','t','u','u','u','f','h','h','ts','ch','sh','shch','','y','i','','e','iu','ia')
soz = input("\n\nSoz: ")
for i in soz:
    san = 0
    for j in cyr:
        if j == i:
            print(lat[san],end="")
            break
        elif i.lower() == j:
            print(lat[san].upper(),end="")
            break
        san +=1