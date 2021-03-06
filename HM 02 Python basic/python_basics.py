#№1 Даны 2 переменных, в которых хранятся строки произвольной длины: *phrase_1* и *phrase_2*.  
#Напишите код, который проверяет какая из этих строк длиннее.

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if len(phrase_1) >= len(phrase_2):
    print("Фраза 1 длиннее фразы 2")
else:
    print("Условие не соблюдено")
print()
# Результат:  
# Фраза 1 длиннее фразы 2

# Результат:  
# Фраза 2 длиннее фразы 1

# Результат:  
# Фраза равной длинны

# № 2 Дана переменная, в которой хранится число (год). 
# Необходимо написать программу, которая выведет, является ли данный год високосным или обычным.

year = 2019
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print ("Високосный год")
else:
    print ("Не високосный год")
print()
    # №3 Необходимо написать программу, которая будет запрашивать у пользователя месяц и дату рождения и выводить соответствующий знак зодиака.

date = int (input ("Введите дату рождения: "))
month = (input("Введите месяц рождения: "))
   
if (date >= 21 and date <= 31 and month == "Март") or (date >= 1 and date <= 20 and month == "Апрель"):
    print ("Ваш знак зодиака Овен")
elif (date >= 21 and date <= 30 and month == "Апрель") or (date >= 1 and date <= 20 and month == "Май"):
    print ("Ваш знак зодиака Телец")
elif (date >= 21 and date <= 31 and month == "Май") or (date >= 1 and date <= 21 and month == "Июнь"):
    print ("Ваш знак зодиака Близнецы")
elif (date >= 22 and date <= 30 and month == "Июнь") or (date >= 1 and date <= 22 and month == "Июль"):
    print ("Ваш знак зодиака Раки")
elif (date >= 23 and date <= 31 and month == "Июль") or (date >= 1 and date <= 23 and month == "Август"):
    print ("Ваш знак зодиака Лев")
elif (date >= 24 and date <= 31 and month == "Август") or (date >= 1 and date <= 23 and month == "Сентябрь"):
    print ("Ваш знак зодиака Дева")
elif (date >= 24 and date <= 30 and month == "Сентябрь") or (date >= 1 and date <= 23 and month == "Октябрь"):
    print ("Ваш знак зодиака Весы")
elif (date >= 24 and date <= 30 and month == "Октябрь") or (date >= 1 and date <= 22 and month == "Ноябрь"):
    print ("Ваш знак зодиака Скорпион")
elif (date >= 23 and date <= 30 and month == "Ноябрь") or (date >= 1 and date <= 21 and month == "Декабря"):
    print ("Ваш знак зодиака Стрелец")
elif (date >= 22 and date <= 31 and month == "Декабрь") or (date >= 1 and date <= 20 and month == "Январь"):
    print ("Ваш знак зодиака Козерог")
elif (date >= 21 and date <= 31 and month == "Январь") or (date >= 1 and date <= 18 and month == "Февраль"):
    print ("Ваш знак зодиака Водолей")
elif (date >= 19 and date <= 28 and month == "Февраль") or (date >= 1 and date <= 20 and month == "Март"):
    print ("Ваш знак зодиака Рыбы")
print()
    # №4 Вам нужно написать программу для подбора упаковок по размерам товара. Размеры (ширина, длина, высота) хранятся в переменных (в сантиметрах):

# Используйте следующие правила:
# - если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран "Коробка №1";
# - если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите "Коробка №2";
# - если длина товара больше 2 метров, то выводите "Упаковка для лыж";
# - во всех остальных случаях выводите "Стандартная коробка №3".

width = 45
length = 205
height = 45

if (width <= 15) and (height <= 15) and (length <= 15):
    print ("Коробка №1")
elif (15 > width < 50) or ( 15 > height < 50)  or ( 15 > length < 50):
    print ("Коробка №2")
elif length > 200:
    print ("Упаковка для лыж")
else:
    print ("Стандартая коробка №3")
print()
# №5 Дана переменная, в которой хранится шестизначное число (номер проездного билета). 
# Напишите программу, которая будет определять, является ли данный билет "счастливым". 
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера.

tickets = "123721"
numbers = list(tickets)
numbers = [int(i) for i in numbers]
if (sum(numbers[:3]) == sum(numbers[3:])):
    print("Счастливый")
else:
    print("Обычный")
print()

# Задание 6 
# Напишите программу, которая сможет вычислять площади трех фигур (круг, треугольник и прямоугольник). 
# Тип фигуры запрашиваем через пользовательский ввод, после чего делаем запрос характеристик фигуры:

# если пользователь выбрал круг, запрашиваем его радиус,
# если треугольник – длины трех его сторон;
# если прямоугольник – длины двух его сторон.

entering_a_shape = input("Введите название фигуры для вычисление площади: ")
if entering_a_shape == "круг":
    radius = (int(input("Введите радиус круга: ")))
    pi = 3.14
    area_of_the_circle = (pi * radius)
    print ("Площадь круга равна", area_of_the_circle)
if entering_a_shape == "треугольник":
    side = (int(input("Введите длину стороны A: ")))
    side2 = (int(input("Введите длину стороны B: ")))
    side3 = (int(input("Введите длину стороны C: ")))
    area_of_the_triangle = (1/2 * side * side2)
    print ("Площадь треугольника равна", area_of_the_triangle)
if entering_a_shape == "прямоугольник":
    width = (int(input("Введите ширину прямоугольника: ")))
    length = (int(input("Введите длину прямоугольника: ")))
    area_of_the_triangle = (width * length)
    print ("Площадь прямоугольника равна", area_of_the_triangle)
print ()
