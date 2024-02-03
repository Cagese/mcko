import csv

with open('scientist.txt', encoding='utf8') as file:
    # Открываем файл scientist.txt и с помощью модуля csv парсим его
    file = list(csv.DictReader(file, delimiter='#', quotechar='"'))
    # сортировка по дате
    file = sorted(file, key=lambda x: x['date'])
# сортировка всех учёных изобретавших Аллопуринол
Allopuriol = list(filter(lambda x: x['preparation'] == 'Аллопуринол', file))
# вывод информации в консоль
print('Разработчиками Аллопуринола были такие люди (результаты выведите в порядке возрастания даты):')
print(len(Allopuriol))
for i in Allopuriol[1:]:
    print(i['ScientistName'] + ' - ' + i['date'])
print(f'Оригинальный рецепт принадлежит: {Allopuriol[0]["ScientistName"]}')
