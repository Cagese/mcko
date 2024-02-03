import csv
with open('scientist.txt', encoding='utf8') as file:
    # Открываем файл scientist.txt и с помощью модуля csv парсим его
    file = list(csv.reader(file, delimiter='#', quotechar='"'))
    # сортировка по дате
    for i in range(len(file)):
        j = i - 1
        key = file[i]
        while file[j][2] > key[2] and j >= 0:
            file[j + 1] = file[j]
            j -= 1
        file[j + 1] = key

for i in range(1,6):
    # Вывод нужных данных в консоль
    print(f'{file[i][0]}:{file[i][1]}')

