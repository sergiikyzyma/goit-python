'''
import string
surname = 'Stephen Spielberg'
letters = (set(surname) & set(string.ascii_uppercase)) | ((set(surname) & set(string.ascii_lowercase)) ^ set('abcde'))
#letters = (set(surname.upper()) | set(surname[5: ].lower())) ^ set(' ')
print(letters)

products_list = ['Вертел', 'Курица', 'Соус', 'Сыр']
products_copy = products_list.copy()
products_reversed = sorted(products_copy, reverse = True)
first_and_third_list = [products_reversed[0], products_reversed[2]]
print(first_and_third_list)

first_string = "Andreev King Larson".lower()
first_list = first_string.split()
second_string = "Swan Ali Guanjo".lower()
second_list = second_string.split()
third_list = first_list.copy()
third_list.extend(second_list)
third_list.sort(reverse = True)
print(third_list)

salary_office_1 = {'Dickens': 15000, 'Bonmarito': 12000, 'Isabalaev': 14000, 'Clinton': 9000}
salary_office_2 = {'Mikelson': 18000, 'Chopin': 20000, 'Kritov': 9000}
salary_office_3 = {'Larson': 9000, 'Kong': 10000}

dickens = salary_office_1.pop('Dickens')
salary_office_3.setdefault('Dickens', dickens)
salary_office_2_copy = salary_office_2.copy()
salary_office_1.update(salary_office_2_copy)
salary_office_2.clear()
mikelson_salary = salary_office_1.get('Mikelson')
print(salary_office_3)

salary_dict = {'Dickens': 15000, 'Bonmarito': 12000, 'Isabalaev': 14000, 'Clinton': 9000}
min_salary = 20000
min_salary_key = ""
for salary_key, salary in salary_dict.items():
    if salary < min_salary:

        min_salary_key = salary_key
        min_salary = salary

salary_dict[min_salary_key] += salary_dict[min_salary_key]*0.24
print(min_salary_key, salary_dict[min_salary_key])

answer1 = ('Spielberg', '30.02.1998', 100, False)
answer2 = ('Lilith', '21.05.1995', 150, True)
answer3 = ('Morbius', '23.01.1999', 200, True)
answer_list = [answer1, answer2, answer3]
surname_list = []
for answer in answer_list:
    for i in answer:
        if i == True:
            surname_list.append(answer[0])
print(surname_list)
surname_set = set('Spielberg'), set('Andreev'), set('Giovanna')
print(surname_set)

secret_ingredients = {'Лаваш', 'Специальная приправа', 'Курица', 'Особый соус'}
ingredients_to_add = {'Соль', 'Лаваш'}
ingredients_to_delete = {'Особый соус', 'Укроп'}

for ingredient1 in secret_ingredients|ingredients_to_add:
    secret_ingredients.add(ingredient1)

for ingredient2 in secret_ingredients&ingredients_to_delete:
    secret_ingredients.remove(ingredient2)

print(secret_ingredients)

first_file = 'Marcel_capitalE_e_la_ViLle.txt'
second_file = 'Kyiv_misto_Stolyzya.ipbn'
third_file = 'Toronto_CITY_CAPital.txt'
fourth_file = 'Berlin_Hauptstadt.txt'
file_names = [first_file, second_file, third_file, fourth_file]
correct_names = []
names = []
for name in range(len(file_names)):
    if file_names[name].endswith('txt') and not file_names[name].startswith('Berlin'):
        names.append(file_names[name].lower())
        print(names)
correct_names = names.copy()
print(correct_names)

import os
import sys

path = sys.argv[1]
while True:
    try:
        files = os.listdir(path)
    except NotADirectoryError:
        path = input("\nReenter your directory, please ")
        continue
    except FileNotFoundError:
        path = input("\nReenter your directory, please ")
        continue
    else:
        break

print(files)

def func(*seqs):
    result = 0
    for i in range(len(seqs)):
        if type(seqs[i]) == int or type(seqs[i]) == float:
            result += seqs[i]
        else:
            print(seqs[i])
    return result

def custom_map(func, *seqs):
    result = []
    for j in range(len(seqs)):
        print(seqs[j])
    result.append(func(*seqs))
    return result

print("result = ", custom_map(func, 2, 3, 5, (-3, 34)))
'''
NAME = "Business District"
URL = "Website"
with open("2018_Seattle_Business_Districts.csv", "r") as fm:
    with open("2018_Seattle_Business_Districts.html", "a") as html:
        html.write("<html><head>2018_Seattle_Business_Districts</head><body><ul>")
        header = []
        for line in fm:
            data = line.split(",")
            data[-1] = data[-1][:-1]
            if header == []:
                header = data
                name_index = header.index(NAME)
                url_index = header.index(URL)
                continue
            name_data = data[name_index]
            url_data = data[url_index]
            print("\n", name_data, " ", url_data, "\n")
            html.write(f"<li><a href='{url_data}'>{name_data}</a></li>")
        html.write("</ul></body></html>")
