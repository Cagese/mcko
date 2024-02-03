import csv

with open('scientist.txt', encoding='utf8') as file:
    # Открываем файл scientist.txt и с помощью модуля csv парсим его
    file = list(csv.DictReader(file, delimiter='#', quotechar='"'))

def initial_name(name):
    surname,name, pat = name.split()
    return f'{surname} {name[0]}.{pat[0]}.'


while True:
    # ожидаем ввод пользователя
    date = input().replace('.','-')
    # проверяем на стоп слово
    if date == 'эксперимент':
        break
    # проверям правильность данных вводимых пользователя
    if sum([int(i.isdigit()) for i in date.split('-')]) != 3 or len(date.split('-')) !=3:
        continue
    # преобразуем дату в правильный формат
    date_prepared = '-'.join(date.split('-')[::-1])
    for i in file:
        if i['date'] == date_prepared:
            # выводим а консоль нужную информацию
            print(f'Ученый {initial_name(i["ScientistName"])} создал препарат: {i["preparation"]} - {date}')
