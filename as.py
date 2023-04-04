#Arapova Assylzhan
#1
    # 1 вывод 
s = "Hello, How are you?" 
print(s.isdigit())

    # 2 метод len
print( ("dlina stroki: "),len('hello'))

    # 3 Конкатенация (сложение)
S1 = str('Hello')
S2 = str('world')
print(S1 + S2)

    # 4 Состоит ли строка из букв
txt = '1465'
print(txt.isalpha())

    # 5 Переводит первый символ строки в верхний регистр, а все остальные в нижний
x = 'HELLO WORLD'
print(x.capitalize())

s1= '1 '
s2 = 10
print(s1 * s2)
    # 6 умножение строк

s1 = 'Hello ! My name is Assylzhan'
print('Assylzhan' in s1)
    # 7 нахождение


s ='Assylzhan'
print(s[0])
    # 8 ВЫвод по индексу

s = 10 * 254 // 77 % 5 ** 5
s2 = f'Вот что получилось {s}'
print(s2)
   # 9 форматирование строк


s = 'Hello! '
s += 'I am  '
print(s)
s = s[:11] + ' Assylzhan'
print(s)
  # 10 изменение строк

print('__________________________________________________')
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

print('__________________________________________________')

a = input("a = ")
b = input("b = ")
while not(a.isdigit() and b.isdigit()):
  a = input("a = ")
  b = input("b = ")
print("Zhayaby = ", (int(a) + int(b)))

#4 лаб есептері шығарылды 2 есепті шығара алмадым

print ("Hello!")
