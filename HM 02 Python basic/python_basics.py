#№1 Даны 2 переменных, в которых хранятся строки произвольной длины: *phrase_1* и *phrase_2*.  
#Напишите код, который проверяет какая из этих строк длиннее.

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if len(phrase_1) >= len(phrase_2):
    print("Фраза 1 длиннее фразы 2")
else:
    print("Условие не соблюдено")

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