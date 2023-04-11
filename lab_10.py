#----------------------------
strings = input("Введите строку: ")  # считываем строку с клавиатуры

# создаем множество, чтобы получить только уникальные символы
chars = set(strings)

 # сортируем символы по алфавиту
sorted_chars = sorted(chars)

 # выводим результат на экран
print("Уникальные символы в строке: ", end="")
for char in sorted_chars:
     print(char, end="")


#-----------------------------
lit=[1,2,-3,4,5]#создаем список 
#Проверяем список по условию
if any(num % 2 == 0 for num in list):
    print("Список содержит четное число")
else:
    print("Спиосок не содержит четное число")

#Проверям весь список по условию
if all(num>0 for num in list):
    print("Все элементы в списке положительные")
else:
    print("В списке присутсвует отрицательное число")

#-----------------------------
def rotate_matrix_clockwise(matrix):
    """
    Функция, которая поворачивает матрицу на 90 градусов по часовой стрелке
    :param matrix: исходная матрица (список списков)
    :return: повернутая матрица (список списков)
    """
    # используем функцию zip() и reversed() для получения столбцов матрицы
    columns = [list(reversed(col)) for col in zip(*matrix)]
    # возвращаем транспонированную матрицу, которая является результатом поворота на 90 градусов
    return [list(row) for row in zip(*columns)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Вызывваем функцию 
rotated_matrix = rotate_matrix_clockwise(matrix)
print(rotated_matrix)

#------------------------
def knapsack(weights, values, max_weight):
    n = len(weights) # количество предметов
    table = [[0 for x in range(max_weight+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(max_weight+1):
            if i==0 or w==0:
                table[i][w] = 0
            elif weights[i-1] <= w:
                table[i][w] = max(values[i-1] + table[i-1][w-weights[i-1]], table[i-1][w])
            else:
               table[i][w] = table[i-1][w]

    return table[n][max_weight]

max_weight = 6
weights = [1, 2, 3, 4]
values = [1, 2, 3, 5]
result = knapsack(weights, values, max_weight)
print(result)

