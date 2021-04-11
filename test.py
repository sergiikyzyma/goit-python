import sys
import pathlib
import os
from collections import UserDict

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

lines = ["Central 6000", "Centra 600", "Centr 60", "tral 12000", "Ceral 16000"]
summa = 0
for _ in lines:
    line = _.split()
    summa += float(line[1])
print(summa)

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


def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, "a") as fh:
        fh.write(additional_info)
    with open(path, "r") as fd:
        fd.seek(start_pos)
        result = fd.readline(count_chars)
    return result


print(file_operations("text.txt", "Ich liebe dich!!!", 5, 7))


def flatten(data):
    if data == []:
        return []
    temp = []
    if type(data[0]) == list:
        first = flatten(data[0])
        second = flatten(data[1:])
        return first + second
    else:
        temp.append(data[0])
        first = temp
        second = flatten(data[1:])
        return first + second


print(flatten([1, 2, [3, 4, [5, 6]], 7]))


def decode(data):
    res = []
    count = len(data)
    if data == []:
        return []
    elem1 = data[0::2]
    elem2 = data[1::2]
    for _ in range(elem2[0]):
        res.append(elem1[0])
    else:
        res += decode(data[2:])
    if data[count:] == []:
        return res


print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))

def encode(data):
    temp, temp_count, count = [], 0, len(data)
    if data == []:
        return []
    if data == [""]:
        return 0
    while len(data[temp_count:]) != 0:
        if len(data) == 1:
            temp_count += 1
            break
        if temp_count == 0:
            temp_count += 1
        if data[temp_count - 1] == data[temp_count]:
            temp_count += 1
        else:
            break
    temp.append(data[temp_count - 1])
    temp.append(temp_count)
    temp += encode(data[temp_count:])
    if data[count:] == []:
        return temp

def encode(data):
    if len(data) == 0:
        return []
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index = index + 1
    current = [data[0], index]
    return current + encode(data[index : len(data)])


print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))

class A(UserDict):
    def __init__(self):
        self.name = "aaa"
        self.phone = [123]


class B(A):
    def __init__(self):
        self.name = "bbb"
        self.phone = [345]
        self.data = {}

    def func(self, name, phone):
        self.name = "petia"
        self.phone.append(phone)
        self.data[self.name] = self.phone
        self.data[name] = self.phone


my1 = A()
my2 = B()
print(my1.name, " ", my1.phone, " ", my2.name, " ", my2.phone)
my2.func("vasia", 5747564785)
print(my1.name, " ", my1.phone, " ", my2.name, " ", my2.phone, " ", my2)

from datetime import datetime
from datetime import timedelta


def get_days_from_today(date):
    date_list = date.split("-")
    date_value = datetime(
        year=int(date_list[0]), month=int(date_list[1]), day=int(date_list[2])
    )
    delta = timedelta(weeks=5)
    time_delta = datetime.now().date() - date_value.date()
    return (time_delta - delta).days


print(get_days_from_today("2021-10-09"))

import random


def random_winners(count, user_dict):
    names = list(user_dict.keys())
    if count <= len(names):
        random.shuffle(names)
        return random.sample(names, count)
    else:
        return "Error"


print(random_winners(2, {"Spielberg": 8000, "Bosh": 1200, "Khamraev": 11000}))

import collections


def to_named(tup):
    Person = collections.namedtuple(
        "Person", ["id", "surname", "discount", "city", "age"]
    )
    person = Person(tup["id"], tup["surname"], tup["discount"], tup["city"], tup["age"])
    return person


print(
    to_named(
        {"id": 12, "surname": "Ivanov", "discount": 23, "city": "Kijow", "age": 35}
    )
)

import collections


def count_activity(clients_activity):
    clients = []
    for activity in clients_activity:
        clients.extend(activity)
    dict_clients = collections.Counter(clients)
    return dict_clients.most_common(3)


print(
    count_activity(
        [["Edvardson", "Damriel", "Mbape", "Columb"], ["Edvardson", "Mbape", "Mbape"]]
    )
)

from collections import deque


def form_deque(clients_id, max_len):
    q = deque(maxlen=max_len)
    for client_id in clients_id:
        q.append(client_id)
    while q[0] % 2:
        elem = q.popleft()
        q.append(elem)

    return q


qqq = [101, 202, 363, 104, 205, 306, 107, 268, 309, 410]
random.shuffle(qqq)
print(form_deque(qqq, 5))


def modify_lists(list_for_dict, pow_dict, list_for_list, add_num):
    my_dict = {i: i ** pow_dict for i in list_for_dict}
    my_list = [i + add_num for i in list_for_list]
    return (my_dict, my_list)


print(modify_lists([1, 2, 3], 3, [1, 2, 3], 3))


def caching():
    cache = {}

    def inner(n):
        cache[0] = 1
        cache[1] = 1
        if not n in cache.keys():
            res = inner(n - 1) + inner(n - 2)
            cache[n] = res
        print(cache)
        return cache[n]

    return inner


print(caching()(3))


def discount_carr(discount):
    def real_cost(cost):
        return cost - (cost * discount)

    return real_cost


my = discount_carr(0.1)
print(my(450))


def generator_string(str=""):

    for ch in str:
        try:
            ch = int(ch)
        except Exception:
            yield 0
        else:
            yield ch


def sum(str):
    summa = 0
    for s in generator_string(str):
        summa += s
    return summa


print(sum("Ivanov 124 with 3-year experience and 24 dollars in pocket"))


def filter_letters(surnames_list):
    new_list = []
    for surnames in surnames_list:
        for j in filter(lambda x: x.isnumeric(), surnames):
            surnames = surnames.replace(j, "")
        new_list.append(surnames)
    return new_list


print(filter_letters(["Ed5ard4on", "Da2riel", "Mb1pe", "Col9m0"]))


class Employees:
    def __init__(self, surnames, group):
        self.employees_dict = {}
        for index, surname in enumerate(surnames):
            self.employees_dict[index] = surname
        self.group = group

    def __setitem__(self, key, value):
        self.employees_dict[key] = value

    def __getitem__(self, item):
        return self.employees_dict[item]


managers = Employees(["Edvardson", "Damriel", "Mbape", "Columb"], "managers")
print(managers.employees_dict, " ", managers.group)


class Client:
    def __init__(self, client_list, discount):
        self.client_list = client_list
        self.discount = discount
        self.current_client = 0

    def __next__(self):
        if self.current_client < len(self.client_list):
            self.current_client += 1
            return self.client_list[self.current_client - 1]
        raise StopIteration

    def __iter__(self):
        return self


for elem in Client(["Edvardson", "Damriel", "Mbape", "Columb"], 0.1):
    print(elem)

from copy import deepcopy


class FoodComponent:
    def __init__(self, product_names, weight, price):
        self.product_names = product_names
        self.weight = weight
        self.price = price

    def __str__(self):
        return f"Product {str(self.product_names)}, weight = {self.weight}, price = {self.price}"

    def __add__(self, other):
        my1 = copy(self)
        my1.product_names = self.product_names + " " + other.product_names
        my1.weight = self.weight + other.weight
        my1.price = self.price + other.price
        return my1

    def __sub__(self, other):

        my2 = copy(self)
        if self.product_names.find(other.product_names) != -1:
            my2.product_names = self.product_names.replace(other.product_names, "")
            my2.weight = self.weight - other.weight
            my2.price = self.price - other.price
            return my2
        else:
            return self

my_recipe_1 = FoodComponent("cheese", 23, 78)
my_recipe_2 = FoodComponent("tomate", 35, 45)
my_recipe_3 = FoodComponent("sparsza", 5, 4)
my_recipe_4 = FoodComponent("fish red", 35, 450)
my_recipe_5 = my_recipe_1 + my_recipe_2 + my_recipe_3 + my_recipe_4
my_recipe_6 = my_recipe_5 - my_recipe_2
print(my_recipe_1, " ", my_recipe_2, " ", my_recipe_5, " ", my_recipe_6)

class FoodComponent:
    def __init__(self, product_names, weight, price):
        self.product_names = product_names
        self.weight = weight
        self.price = price

    def __str__(self):
        return f"Product {str(self.product_names)}, weight = {self.weight}, price = {self.price}"

    def __add__(self, other):
        my1 = deepcopy(self)
        my1.product_names += other.product_names
        my1.weight += other.weight
        my1.price += other.price
        return my1

    def __sub__(self, other):
        my2 = deepcopy(self)
        for product_name in other.product_names:
            if product_name in my2.product_names:
                my2.product_names.remove(product_name)
                my2.weight -= other.weight
                my2.price -= other.price
                return my2
        return self


my_recipe_1 = FoodComponent(["cheese"], 23, 78)
my_recipe_2 = FoodComponent(["tomate"], 35, 45)
my_recipe_3 = FoodComponent(["sparsza"], 5, 4)
my_recipe_4 = FoodComponent(["fish red"], 35, 450)
my_recipe_5 = my_recipe_1 + my_recipe_2 + my_recipe_3 + my_recipe_4
my_recipe_6 = my_recipe_5 - my_recipe_4 - my_recipe_3
print(my_recipe_1, " ", my_recipe_2, " ", my_recipe_5, " ", my_recipe_6)

import re


def total_price(order):
    s = 0
    my_order = re.findall("[: ]\d+", order)
    for i in my_order:
        s += int(i)
    return s


print(total_price("Название_1: 1 Название_2: 5 Название_3: 7"))
import re


def find_password(passwords):
    password = re.search("[a-zA-Z]{5}[0-9]{5}", passwords)
    return password.group()


print(find_password("abcde12345vbdhvbhd47ty74"))

from copy import deepcopy, copy


class Customer:
    def __init__(self, surname, id, attributes):
        self.surname = surname
        self.id = id
        self.attributes = attributes

    def __eq__(self, other):
        if self.surname == other.surname and self.id == other.id:
            return True
        return False

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["id"] *= 4
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.id /= 4

    def __copy__(self):
        copy_surname = copy(self.surname)
        copy_id = copy(self.id)
        copy_attributes = copy(self.attributes)
        copy_obj = Customer(copy_surname, copy_id, copy_attributes)
        return copy_obj

    def __deepcopy__(self):
        copy_obj = deepcopy(Customer(self.surname, self.id, self.attributes))
        return copy_obj


def create_incremented_customer(customer):
    new_customer = customer.__deepcopy__()
    new_customer.id += 1
    return new_customer


print(create_incremented_customer(Customer("Ivaniv", 111, "age:31, phone:1435435")))
"""
temp = os.getcwd()
print(temp)
os.chdir(temp)
qqq = "Bye by my friend"
temp = ["Bye by", "Exit", "Thank you", "That`s all"]
for i in temp:
    print(qqq.startswith(i))
    print(qqq.split(i)[0], "    ", qqq)
    input()
if 'a' not in 'adrrdxfdxfdad':
    print("Ich liebe dich")
