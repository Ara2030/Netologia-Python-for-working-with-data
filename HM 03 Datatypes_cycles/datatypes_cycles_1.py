## Задание 1
# Дана переменная, в которой хранится слово из латинских букв. 
# Напишите код, который выводит на экран:
# - среднюю букву, если число букв в слове нечетное;
# - две средних буквы, если число букв четное.

from ntpath import join


word = "testing"
if len(word) % 2 == 0:
    print (word [1:3])
elif len(word) % 2 != 0:
    print (word [3:4])

## Задание 2
# Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз) 
# и после первого нуля выводит сумму всех ранее введенных чисел.
numbers = 0
while True:
    numbers_1 = (int(input("Введите число: ")))
    if numbers_1 == 0:
        break
    else: numbers += numbers_1
print ("Сумма: ", numbers)

## Задание 3
# Мы делаем [MVP] dating-сервиса, и у нас есть список парней и девушек.  
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и 
# познакомим людей с одинаковыми индексами после сортировки!
# Но мы не будем никого знакомить, если кто-то может остаться без пары:
print()
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Tanya']
boys.sort()
girls.sort()
perfect_couples = zip(boys, girls)
print ("Идеальная пара")
for couple in (list(perfect_couples)):
    print(",".join(couple))
    if len(girls) == len(boys):
        pass
    else:
        print ("Внимание, кто-то может остаться без пары!")
