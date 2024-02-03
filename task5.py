import csv
import random

with open('scientist.txt', encoding='utf8') as file:
    # Открываем файл scientist.txt и с помощью модуля csv парсим его
    file = list(csv.DictReader(file, delimiter='#', quotechar='"'))
# Генерация таблицы ascii
ascii_data = [k + 1 for k in range(1024)]
random.shuffle(ascii_data)
table = {i + 1: j for i, j in enumerate(ascii_data)}


def generate_hash(name):
    # Генерация хеша
    name_hash = 0
    for i in name:
        name_hash += table[ord(i) % 1024]
    return name_hash % 2048


for i in file[1:]:
    i['hash'] = generate_hash(i['ScientistName'])
with open('scientist_with_hash.csv', 'w', encoding='utf8', newline='') as new_file:
    # Создание нового csv файла с данными из scientist.txt и данными о хеше
    new_file = csv.DictWriter(new_file,
                              fieldnames=['hash', 'ScientistName', 'preparation', 'date', 'components', 'login',
                                          'password'], quotechar='"', delimiter='#')
    new_file.writeheader()
    new_file.writerows(file[1:])
