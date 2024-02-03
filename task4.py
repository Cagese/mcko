import csv
import string
import random

with open('scientist.txt', encoding='utf8') as file:
    # Открываем файл scientist.txt и с помощью модуля csv парсим его
    file = list(csv.DictReader(file, delimiter='#', quotechar='"'))

def login_generator(name):
    # Генерация логина из имени
    surname, name, pat = name.split()
    return f'{surname}_{name[0]}{pat[0]}'
def password_generator():
    # Генерация пароля состоящего из 10 символов состоящих из англиского алфовита (строчного и прописного) и цыфр
    password_comp = string.ascii_letters + string.digits
    return ''.join([random.choice(password_comp) for _ in range(10)])
for i in file:
    i['login'] = login_generator(i['ScientistName'])
    i['password'] = password_generator()
with open('scientist_password.csv', 'w', encoding='utf8', newline='') as new_file:
    # Создание нового csv файла с данными из scientist.txt и данными о логине и пароле
    new_file = csv.DictWriter(new_file,
                              fieldnames=['ScientistName', 'preparation', 'date', 'components', 'login', 'password'],
                              quotechar='"', delimiter='#')
    new_file.writeheader()
    new_file.writerows(file[1:])
