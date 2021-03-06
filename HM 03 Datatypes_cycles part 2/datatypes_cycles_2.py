## Задание 1
# Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя (пример структуры данных приведен ниже). 
# Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех пользователей.

ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]
       }
user1_set = (set(ids['user1']))
user2_set = (set(ids['user2']))
user3_set = (set(ids['user3']))

print (user1_set|user2_set|user3_set)
print ()
## Задание 2
# Дана переменная, в которой хранится список поисковых запросов пользователя (пример структуры данных приведен ниже). 
# Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.
# Поисковых запросов, содержащих 2 слов(а): 42.86%
# Поисковых запросов, содержащих 3 слов(а): 57.14%
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
storage = {}

for query in queries:
#Разделение запросов по словам 
    words = query.split()

    if len(words) in storage.keys():
    #Считаем данное количество слов если в запросе встретится еще запрос 
    # с одинаковым колличеством слов то происходит + 1 затем довавляет в множество 
        storage[len(words)] += 1
    else:
    # Добавление в множество 
        storage.update({
            len(words): 1
        })

for key, value in storage.items():
    percentage = round((value / len(queries)) * 100, 2)
    print(f'Поисковых запросов из {key} слова: {percentage}% ({value} запр.)')
print ()
#Задача 3
#Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам. 
#Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: (revenue / cost - 1) * 100

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}
for key, value in results.items():
    value['ROI'] = round(((value['revenue'] / value['cost']) - 1)*100 , 2)
print (results)
print ()
## Задание 4
#Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж (пример структуры данных приведен ниже). 
#Напишите программу, которая возвращает название канала с максимальным объемом продаж.
stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
max_stats = max(stats, key = stats.get)
print ("Максимальный объем продаж на рекламном канале:", max_stats)