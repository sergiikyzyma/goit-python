from helpers import BOT_HANDLERS, filter_text, get_intent, get_action, get_answer_by_intent
from collections import UserDict
from datetime import datetime
from datetime import timedelta
import clean
import os
import pathlib
import pickle
import random
import re


class NameError1(Exception):
    pass


class NameError2(Exception):
    pass


class NameError3(Exception):
    pass


class NameError4(Exception):
    pass


class NameError5(Exception):
    pass


class NameError6(Exception):
    pass


class NameError7(Exception):
    pass

class NameError8(Exception):
    pass


def input_error(func):
    def inner(com, arg, adress_book):
        my_error_1 = "You wrote wrong the second key or it's missing"
        my_error_2 = "Wrong phone-number (must be in format XXX-XXX-XX-XX) or birthday (must be in format XX-XX-XXXX)!"
        my_error_3 = "You maked the fail by inputing the command!"
        my_error_4 = "You maked the fail by inputing the number of arguments!"
        my_error_5 = "You wrote wrong the compound commmnd 'good bye'!"
        my_error_6 = "You wrote wrong the compound command 'show all'!"
        my_error_7 = "Missing name in database!"
        my_error_8 = "Phone-number in database is not exiest yet!"
        my_error_9 = "Date of birthday in database is not exiest yet!"
        my_error_10 = "E-mail in database is not exiest yet!"
        my_error_11 = "Address of living in database is not exiest yet!"
        my_error_12 = "You maked the fail by inputing the path to the folder!"
        try:
            res = func(com, arg, adress_book)
        except KeyError:
            return my_error_1
        except ValueError:
            return my_error_2
        except UnboundLocalError:
            return my_error_3
        except IndexError:
            return my_error_4
        except NameError1:
            return my_error_5
        except NameError2:
            return my_error_6
        except NameError3:
            return my_error_7
        except NameError4:
            return my_error_8
        except NameError5:
            return my_error_9
        except NameError6:
            return my_error_10
        except NameError7:
            return my_error_11
        except NameError8:
            return my_error_12
        else:
            return res

    return inner


@input_error
def parser(com, arg, my_adressbook):
    commands = {
        #--------------------intents--------------------
        "exit": my_adressbook.ausgang,
        "hello": my_adressbook.hello,
        "help": my_adressbook.help,
        "show": my_adressbook.showall,
        #--------------------actions--------------------
        "clean":clean.main,
        "add": my_adressbook.add,
        "change": my_adressbook.change,
        "delete": my_adressbook.delete,
        "find": my_adressbook.findall,
        "name": my_adressbook.findname,
        "phone": my_adressbook.findphone,
        "birthday": my_adressbook.findbirthday,
        "email": my_adressbook.findemail,
        "address": my_adressbook.findaddress,
    }
    arguments = {
        #--------------------intents--------------------
        "show": "<nothing>",
        "hello": "<nothing>",
        "help": "<nothing>",
        "exit": "<nothing>",
        #--------------------actions--------------------
        "clean":"<the path to the folder for cleaning>",
        "add": "<name> <value>",
        "change": "<name> <old_value> <new_value>",
        "delete": "<name> <value>",
        "find": "<second_key (all, phone, birthday, email, address)> <name>",
        "name": "<part or full name>",
        "phone": "<part or full phone-number>",
        "birthday": "<part or full date of birthday>",
        "email": "<part or full email>",
        "address": "<part or full address>",
    }
    print(com, "    ", arg)
    input()
    #--------------------intents--------------------
    if com in BOT_HANDLERS["intents"]["exit"]["examples"]:
        result = commands["exit"]()
    elif com in BOT_HANDLERS["intents"]["hello"]["examples"]:
        result = commands["hello"]()
    elif com in BOT_HANDLERS["intents"]["help"]["examples"]:
        result = commands["help"](commands, arguments)
    elif com in BOT_HANDLERS["intents"]["show"]["examples"]:
        result = commands["show"]()
    #--------------------actions--------------------
    elif com in BOT_HANDLERS["actions"]["clean"]["examples"]:
        if pathlib.Path(arg).is_dir():
            temp_path = os.getcwd()
            commands["clean"](arg)
            os.chdir(temp_path)
            result = "This folder was sorted and cleaned"
        else:
            raise NameError8
    elif com in BOT_HANDLERS["actions"]["add"]["examples"]:
        result = commands["add"](arg[0], arg[1])
    elif com in BOT_HANDLERS["actions"]["change"]["examples"]:
        result = commands["change"](arg[0], arg[1], arg[2])
    elif com in BOT_HANDLERS["actions"]["delete"]["examples"]:
        result = commands["delete"](arg[0], arg[1])
    elif com in BOT_HANDLERS["actions"]["find"]["examples"]:
        result = commands["find"](arg[0], arg[1])
    elif com in BOT_HANDLERS["actions"]["name"]["examples"]:
        result = commands["name"](arg[0])
    elif com in BOT_HANDLERS["actions"]["phone"]["examples"]:
        result = commands["phone"](arg[0])
    elif com in BOT_HANDLERS["actions"]["birthday"]["examples"]:
        result = commands["birthday"](arg[0])
    elif com in BOT_HANDLERS["actions"]["email"]["examples"]:
        result = commands["email"](arg[0])
    elif com in BOT_HANDLERS["actions"]["address"]["examples"]:
        result = commands["address"](arg[0])
    return result

def split_command(com):
    intents = ["exit", "help", "hello", "show"]
    actions = ["clean", "add", "change", "delete", "find", "name", "phone", "birthday", "address"]
    for intent in intents:
        for example in BOT_HANDLERS["intents"][intent]["examples"]:
            example = example.lower()
            if re.match(example, com):
                return example, com.split(example)[0].strip()
    for action in actions:
        for example in BOT_HANDLERS["actions"][action]["examples"]:
            example = example.lower()
            if re.match(example, com):
                return example, com.split(example)[1].strip()
    return "Error", "Error"

class Adressbook(UserDict):
    def add_Record(self, name, value, type_value="phone"):
        if self.data == dict():
            myRecord = {name: {type_value: value}}
        else:
            myRecord = self.data
        return myRecord

    def change_Record(self, name, value):
        self.data.update({name: value})
        return self.data

    def iterator(self):
        item = self.data.popitem()
        yield str(item)


class Field(Adressbook):
    def __init__(self):
        self.__value = ""

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    def is_name(self, field):
        for key in self.data.keys():
            if key == field:
                return True


class Phone(Field):
    def is_phone(self, field):
        for value_list in self.data.values():
            for v in value_list["phone"]:
                if v == field:
                    return True


class Birthday(Field):
    def is_birthday(self, field):
        for v in self.data.values():
            if v["birthday"] == field:
                return True


class Email(Field):
    def is_email(self, field):
        for value_list in self.data.values():
            for v in value_list["email"]:
                if v == field:
                    return True


class Address(Field):
    def is_address(self, field):
        for v in self.data.values():
            if v["address"] == field:
                return True


class Record(Name, Phone, Birthday, Email, Address):
    def __init__(self):
        self.name = ""
        self.phone = []
        self.birthday = ""
        self.email = []
        self.address = ""
        self.data = {}

    def __add_item_phone(self, name, phone):
        if "phone" in self.data[name]:
            self.data[name]["phone"].append(phone)
        else:
            self.data[name]["phone"] = [phone]

    def __add_item_email(self, name, email):
        if "email" in self.data[name]:
            self.data[name]["email"].append(email)
        else:
            self.data[name]["email"] = [email]

    def __add_phone(self, name, phone):
        if not self.is_name(name):
            self.data = self.add_Record(name, {"phone": [phone]})
            self.data = self.change_Record(name, {"phone": [phone]})
        else:
            self.__add_item_phone(name, phone)
            self.data = self.change_Record(name, self.data.get(name))
        answer = random.choice(BOT_HANDLERS["actions"]["add"]["responses"])
        temp = "I added phone-number"
        return answer + ": " + temp

    def __add_birthday(self, name, birthday):
        if not self.is_name(name):
            self.data = self.add_Record(name, {"birthday": birthday}, "birthday")
            self.data = self.change_Record(name, {"birthday": birthday})
        else:
            self.data[name]["birthday"] = birthday
            self.data = self.change_Record(name, self.data.get(name))
        answer = random.choice(BOT_HANDLERS["actions"]["add"]["responses"])
        temp1 = "I added date of birthday"
        temp2 = str(self.day_to_birthday(name)) + " days to birthday"
        return answer + ": " + temp1 + " - " + temp2

    def __add_email(self, name, email):
        if not self.is_name(name):
            self.data = self.add_Record(name, {"email": [email]}, "email")
            self.data = self.change_Record(name, {"email": [email]})
        else:
            self.__add_item_email(name, email)
            self.data = self.change_Record(name, self.data.get(name))
        answer = random.choice(BOT_HANDLERS["actions"]["add"]["responses"])
        temp = "I added email"
        return answer + ": " + temp

    def __add_address(self, name, address):
        if not self.is_name(name):
            self.data = self.add_Record(name, {"address": address}, "address")
            self.data = self.change_Record(name, {"address": address})
        else:
            self.data[name]["address"] = address
            self.data = self.change_Record(name, self.data.get(name))
        answer = random.choice(BOT_HANDLERS["actions"]["add"]["responses"])
        temp = "I added address"
        return answer + ": " + temp

    def __change_phone(self, name, old_phone, new_phone):
        if self.is_name(name):
            if self.is_phone(old_phone):
                self.data[name]["phone"].remove(old_phone)
                self.__add_item_phone(name, new_phone)
                self.data = self.change_Record(name, self.data.get(name))
                answer = random.choice(BOT_HANDLERS["actions"]["change"]["responses"])
                temp = "I changed phone-number"
                return answer + ": " + temp
            else:
                raise NameError4
        else:
            raise NameError3

    def __change_birthday(self, name, old_birthday, new_birthday):
        if self.is_name(name):
            if self.is_birthday(old_birthday):
                self.data[name]["birthday"] = new_birthday
                self.data = self.change_Record(name, self.data.get(name))
                answer = random.choice(BOT_HANDLERS["actions"]["change"]["responses"])
                temp1 = "I changed date of birthday"
                temp2 = str(self.day_to_birthday(name)) + " days to birthday"
                return answer + ": " + temp1 + " - " + temp2
            else:
                raise NameError5
        else:
            raise NameError3

    def __change_email(self, name, old_email, new_email):
        if self.is_name(name):
            if self.is_email(old_email):
                self.data[name]["email"].remove(old_email)
                self.__add_item_email(name, new_email)
                self.data = self.change_Record(name, self.data.get(name))
                answer = random.choice(BOT_HANDLERS["actions"]["change"]["responses"])
                temp = "I changed email"
                return answer + ": " + temp
            else:
                raise NameError6
        else:
            raise NameError3

    def __change_address(self, name, old_address, new_address):
        if self.is_name(name):
            if self.is_address(old_address):
                self.data[name]["address"] = new_address
                self.data = self.change_Record(name, self.data.get(name))
                answer = random.choice(BOT_HANDLERS["actions"]["change"]["responses"])
                temp = "I changed address"
                return answer + ": " + temp
            else:
                raise NameError7
        else:
            raise NameError3

    def __delete_phone(self, name, phone):
        if self.is_name(name):
            if self.is_phone(phone):
                self.data[name]["phone"].remove(phone)
                self.data = self.change_Record(name, self.data.get(name))
                answer = random.choice(BOT_HANDLERS["actions"]["delete"]["responses"])
                temp = "I deleted phone-number"
                return answer + ": " + temp
            else:
                raise NameError4
        else:
            raise NameError3

    def __delete_birthday(self, name, birthday):
        if self.is_name(name):
            if self.is_birthday(birthday):
                self.data[name].pop("birthday")
                self.data = self.change_Record(name, self.data.get(name))
                answer = random.choice(BOT_HANDLERS["actions"]["delete"]["responses"])
                temp = "I deleted date of birthday"
                return answer + ": " + temp
            else:
                raise NameError5
        else:
            raise NameError3

    def __delete_email(self, name, email):
        if self.is_name(name):
            if self.is_email(email):
                self.data[name]["email"].remove(email)
                self.data = self.change_Record(name, self.data.get(name))
                answer = random.choice(BOT_HANDLERS["actions"]["delete"]["responses"])
                temp = "I deleted email"
                return answer + ": " + temp
            else:
                raise NameError6
        else:
            raise NameError3

    def __delete_address(self, name, address):
        if self.is_name(name):
            if self.is_address(address):
                self.data[name].pop("address")
                self.data = self.change_Record(name, self.data.get(name))
                answer = random.choice(BOT_HANDLERS["actions"]["delete"]["responses"])
                temp = "I deleted address"
                return answer + ": " + temp
            else:
                raise NameError7
        else:
            raise NameError3

    def add(self, name, value):
        self.value = value
        if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", self.value):
            return self.__add_phone(name, self.value)
        elif re.match(r"\d{2}-\d{2}-\d{4}", self.value):
            _ = datetime.strptime(self.value, "%d-%m-%Y")
            return self.__add_birthday(name, self.value)
        elif re.match(r"[A-Za-z0-9]*\@\w*\.[a-z]{3}", self.value):
            return self.__add_email(name, self.value)
        elif re.match(r"\w*", self.value):
            return self.__add_address(name, self.value)
        else:
            raise ValueError

    def change(self, name, old_value, new_value):
        self.value = new_value
        if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", self.value):
            return self.__change_phone(name, old_value, self.value)
        elif re.match(r"\d{2}-\d{2}-\d{4}", self.value):
            return self.__change_birthday(name, old_value, self.value)
        elif re.match(r"[A-Za-z0-9]*\@\w*\.[a-z]{3}", self.value):
            return self.__change_email(name, old_value, self.value)
        elif re.match(r"\w*", self.value):
            return self.__change_address(name, old_value, self.value)
        else:
            raise ValueError

    def delete(self, name, value):
        self.value = value
        if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", self.value):
            return self.__delete_phone(name, self.value)
        elif re.match(r"\d{2}-\d{2}-\d{4}", self.value):
            return self.__delete_birthday(name, self.value)
        elif re.match(r"[A-Za-z0-9]*\@\w*\.[a-z]{3}", self.value):
            return self.__delete_email(name, self.value)
        elif re.match(r"\w*", self.value):
            return self.__delete_address(name, self.value)
        else:
            raise ValueError

    def findall(self, arg, name):
        if self.is_name(name):
            answer = random.choice(BOT_HANDLERS["actions"]["find"]["responses"])
            temp = str(self.day_to_birthday(name)) + " days to birthday"
            if arg == "all":
                return answer + " " + str(self.data.get(name)) + " - " + temp
            elif arg == "phone" or arg == "birthday":
                return answer + " " + str(self.data.get(name).get(arg)) + " - " + temp
            elif arg == "email" or arg == "address":
                return answer + " " + str(self.data.get(name).get(arg)) + " - " + temp
            else:
                raise KeyError
        else:
            raise NameError3

    def hello(self):
        return random.choice(BOT_HANDLERS["intents"]["hello"]["responses"])

    def showall(self):
        result = ""
        serialized_data = pickle.dumps(self.data, 5)
        while True:
            try:
                result += "\n\t\t\t" + str(next(self.iterator()))
            except KeyError:
                self.data = pickle.loads(serialized_data)
                answer = random.choice(BOT_HANDLERS["actions"]["showall"]["responses"])
                return answer + " " + result

    def ausgang(self):
        return random.choice(BOT_HANDLERS["intents"]["exit"]["responses"])

    def day_to_birthday(self, name):
        my_date_str = self.data[name]["birthday"]
        my_date = datetime.strptime(my_date_str, "%d-%m-%Y")
        date_birthday = timedelta(days=my_date.timetuple().tm_yday)
        date_now = timedelta(days=datetime.now().timetuple().tm_yday)
        oldyear = timedelta(days=datetime(year=1, month=12, day=31).timetuple().tm_yday)
        newyear = timedelta(days=datetime(year=1, month=1, day=1).timetuple().tm_yday)
        if date_birthday == date_now:
            result = 0
        elif date_birthday > date_now:
            result = date_birthday - date_now
        else:
            result = (oldyear - date_now) + (date_birthday - newyear)
        return result.days

    def bot(self, question):
        intent = get_intent(question)
        action = get_action(question)

        # finding ready answer
        if intent:
            answer = get_answer_by_intent(intent)
            if answer:
                return answer
                
        answer = get_answer_by_action(action, question)
        if answer:
            return answer
        
        # any answer
        answer = get_failure_phrase()
        return answer

    def help(self, commands, arguments):
        result = "You can to write next commands for working with me:"
        for command in commands.keys():
            result += "\n\t\t\t" + str(command) + " " + str(arguments[command])
        answer = random.choice(BOT_HANDLERS["intents"]["help"]["responses"])
        return answer + " " + result

    def findname(self, part_name):
        result = ""
        for name in self.data.keys():
            if re.findall(part_name, name):
                temp = str(self.day_to_birthday(name)) + " days to birthday"
                result += "\n\t\t\t" + str(name) + " " + str(self.data[name]) + " - " + str(temp)
        if result:
            answer = random.choice(BOT_HANDLERS["actions"]["name"]["responses"])
            return answer + " " + result
        else:
            raise NameError3

    def findphone(self, part_phone):
        result = ""
        for name in self.data.keys():
            if "phone" in self.data[name]:
                for elem in self.data[name]["phone"]:
                    if re.findall(part_phone, elem):
                        temp = str(self.day_to_birthday(name)) + " days to birthday"
                        result += "\n\t\t\t" + str(name) + " " + str(elem) + " - " + str(temp)
        if result:
            answer = random.choice(BOT_HANDLERS["actions"]["phone"]["responses"])
            return answer + " " + result
        else:
            raise NameError4

    def findbirthday(self, part_birthday):
        result = ""
        for name in self.data.keys():
            if "birthday" in self.data[name]:
                temp = self.data[name]["birthday"]
                if re.findall(part_birthday, temp):
                    temp_str = str(self.day_to_birthday(name)) + " days to birthday"
                    result += "\n\t\t\t" + str(name) + " " + str(temp) + " - " + str(temp_str)
        if result:
            answer = random.choice(BOT_HANDLERS["actions"]["birthday"]["responses"])
            return answer + " " + result
        else:
            raise NameError5

    def findemail(self, part_email):
        result = ""
        for name in self.data.keys():
            if "email" in self.data[name]:
                for elem in self.data[name]["email"]:
                    if re.findall(part_email, elem):
                        result += "\n\t\t\t" + str(name) + " " + str(elem)
        if result:
            answer = random.choice(BOT_HANDLERS["actions"]["email"]["responses"])
            return answer + " " + result
        else:
            raise NameError6

    def findaddress(self, part_address):
        result = ""
        for name in self.data.keys():
            if "address" in self.data[name]:
                temp = self.data[name]["address"]
                if re.findall(part_address, temp):
                    result += "\n\t\t\t" + str(name) + " " + str(temp)
        if result:
            answer = random.choice(BOT_HANDLERS["actions"]["address"]["responses"])
            return answer + " " + result
        else:
            raise NameError7


def main():
    my_record = Record()
    my_record.data = {
        "ivanov": {
            "phone": ["006-222-33-33", "073-888-78-89"],
            "birthday": "25-09-1953",
        },
        "petrov": {
            "phone": ["098-333-44-44", "063-999-45-56"],
            "birthday": "07-03-1983",
        },
        "sidorov": {
            "phone": ["050-444-55-66"],
            "birthday": "14-12-1998",
        },
        "petrenko": {
            "phone": ["098-777-44-44", "050-444-55-66"],
            "birthday": "07-07-1983",
        },
        "sidorenko": {
            "phone": ["098-777-44-44", "050-444-55-66"],
            "birthday": "03-09-1983",
        },
    }

    result = ""
    key = ""

    if pathlib.Path("my.bin").is_file():
        with open("my.bin", "rb") as file:
            my_record = pickle.load(file)

    print("{:>20}{:<300}".format("Your assistent: ", "Hello"))
    while True:
        if key == "" in my_record.data.keys():
            my_record.data.pop(key)
        command = input("{:>20}".format("User: "))
        kommande, argumente = split_command(command)
        if kommande != "clean":
            argumente = argumente.lower().split(" ")
        result = parser(kommande, argumente, my_record)
        print("{:>20}{:<300}".format("Your assistent: ", result))
        if result in BOT_HANDLERS["intents"]["exit"]["responses"]:
            break

    with open("my.bin", "wb") as file:
        pickle.dump(my_record, file, 5)


if __name__ == "__main__":
    main()