import sys

"""
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

print(sys.path)

surname_to_search = "Spielberg"
surnames_statistic_list = ["Stephen_Spielberg_salary_statistic.xlsx", "Jeff_Mikelson_salary_year.xlsx", "Bosh_Ray_salary.xlsx"]
surnames_income = {"Mikelson": 25000, "Bosh": 16000}
taxes_pay = {"Mikelson", "Bosh"}
not_proper_declaration = []
statistic_flag = False
for statistic in surnames_statistic_list:
    if statistic.find(surname_to_search):
        statistic_flag = True

if statistic_flag:
    not_proper_declaration.append("statistic_list")
if surname_to_search in surnames_income.keys():
    not_proper_declaration.append("income")
if surname_to_search in taxes_pay:
    not_proper_declaration.append("taxes")

print(not_proper_declaration)

price = 80
discount_percent = 20
def discount(price, discount_percent):
    price *= discount_percent / 100
    return price
final_price = price - discount(price, discount_percent)
print(price, final_price)

def add_premium(salary_dict, premium_percent = 20):
    for name, salary in salary_dict.items():
        salary *= (100 + premium_percent) / 100
        salary_dict[name] = salary
    return salary_dict
print(add_premium({"Spielberg": 8000, "Bosh": 1200, "Khamraev": 11000}))

def is_prime(n, d=3):
    if n <= d: return n > 1    
    elif not n % 2 or not n % 3: return False   
    else:
        j = 5
        for i in range(j, j ** 2 <= n, 6):
            if not n % i or not n % (i + 2): return False   
        return True
print(" 7 ", is_prime(7))

import math

def shift_variations_count(workers_list, shift_count):
    n = 10
    for _ in workers_list:
        n += 1
    print(workers_list," ", n, " ", shift_count)
    return math.factorial(n) / (math.factorial(shift_count) * math.factorial(n - shift_count))
print(shift_variations_count(surnames_statistic_list, 3))
"""
lines = ["Central 6000", "Centra 600", "Centr 60", "tral 12000", "Ceral 16000"]
summa = 0
for _ in lines:
    line = _.split()
    summa += float(line[1])
print(summa)
"""
orders = ["Big chicken:active", "Big:active", "chicken:active"]        
fh = open("text.txt", "a")
for order in orders:
    fh.writelines(order + "\n")
fh.close()
fd = open("text.txt", "r")
lines = fd.readlines()
count = 0
for _ in lines:
    line = _.split(":")
    if line[1][:-1] == "active":        
        count += 1
fd.close()        
print(count)

def is_equal(utf_8_pass, utf_16_pass):
    if utf_8_pass.decode("utf-8") == utf_16_pass.decode("utf-16"):
        return True
    else:
        return False
print(is_equal(lines[0].encode("utf-8"), lines[0].encode("utf-16")))

import shutil
def create_archive(path, file_name, employee_citizenship):
    with open(path + "/" + file_name, "ab") as fh:
        for name, citizenship in employee_citizenship.items():
            temp = str(name) + citizenship + "\n"
            fh.write(temp.encode())
    shutil.make_archive("backup", "zip", path)

    return file_name
my_dict = dict()
for i, my_str in enumerate(lines):
    my_dict[i] = my_str
create_archive(shutil.os.getcwd(), "text.bin", my_dict)

def comments_to_show(comment_dict={}):
    comment_list = []
    new_comment_list = []
    for comment in comment_dict.items():
        comment_list.append(comment)
    comment_list.sort(key=lambda x: x[1], reverse=True)
    for new_comment in comment_list[:3]:
        new_new_comment = new_comment[0].removeprefix("<comment>").removesuffix("</comment>").strip()
        new_comment_list.append(new_new_comment)
    comment_result = "\n".join(new_comment_list)
    result = comment_result.replace("\t", "")
    return result

print(comments_to_show({"vdgfg": 23, "cnjdn": 34, "av": 3, "23": 7, "nmnm": 9}))
"""

def translate_surnames(surnames):
    alphabet_rus = ("а", "б", "е", "и", "к", "о", "р", "н", "т", "с", "л")
    alphabet = ("a", "b", "e", "i", "k", "o", "r", "n", "t", "s", "l")
    map = dict()
    for i, _ in enumerate(alphabet_rus):
        map[ord(alphabet_rus[i])] = alphabet[i]
        map[ord(alphabet_rus[i].upper())] = alphabet[i].capitalize()
    name = surnames.translate(map)
    return name
print(translate_surnames("Сергей"))

def formatted_comments(comments_dict):
    new_comment = []
    for comment in comments_dict.items():
        new_comment.append("|{:^20}|{:>20}|".format(comment[0], comment[1]))
        print("|{:^20}|{:>20}|".format(comment[0], comment[1]))
    return new_comment
formatted_comments({"Nice service": 100, "Polite waitresses": 39, "Delicious food": 80})

import re
def structure_recipe(order):
    # res = re.sub(("\d"), " ", recipe)
    # result = re.sub((";"), "\n", res)
    res = re.findall("[:][ ]\d+", order)
    i = 0
    summa = 0
    for _ in res:
        summa += int(res[i][2:])
        i += 1
    print(i, " ", res)
    return summa
print(structure_recipe("dheud37r6: 7473t46;dheud37r6: 743t46;dheud37r6: 773t46;"))
