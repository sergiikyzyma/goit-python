from adressbook import Record, NameError1, NameError2, NameError3, NameError4, NameError5, NameError6, NameError7, NameError8, NameError9, NameError10
from helpers import BOT_HANDLERS, INTENTS, ACTIONS, TAGS
import clean
import os
import pathlib
import pickle
import random
import re


def input_error(func):
    def inner(com, arg, adress_book):
        my_error_1 = "You wrote wrong the second key or it's missing"
        my_error_2 = "Wrong phone-number (must be in format XXX-XXX-XX-XX), or birthday (must be in format XX-XX-XXXX), or e-mail, or address!"
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
        my_error_13 = "Missing note in database!"
        my_error_14 = "Missing tag in database!"
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
        except NameError9:
            return my_error_13
        except NameError10:
            return my_error_14
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
        "addcontact": my_adressbook.addcontact,
        "addnotes": my_adressbook.addnotes,
        "changecontact": my_adressbook.changecontact,
        "changenotes": my_adressbook.changenotes,
        "deletecontact": my_adressbook.deletecontact,
        "deletenotes": my_adressbook.deletenotes,
        "findcontact": my_adressbook.findcontact,
        "findbytag":my_adressbook.findbytag,
        "name": my_adressbook.findname,
        "phone": my_adressbook.findphone,
        "birthday": my_adressbook.findbirthday,
        "email": my_adressbook.findemail,
        "address": my_adressbook.findaddress,
        "peaple":my_adressbook.givepeaplebirthday,
    }
    arguments = {
        #--------------------intents--------------------
        "show": "<nothing>",
        "hello": "<nothing>",
        "help": "<nothing>",
        "exit": "<nothing>",
        #--------------------actions--------------------
        "clean":"<the path to the folder for cleaning>",
        "addcontact": "<name> <value>",
        "addnotes": "<name> <tag> <value>",
        "changecontact": "<name> <old_value> <new_value>",
        "changenotes": "<name> <tag> <old_value> <new_value>",
        "deletecontact": "<name> <value>",
        "deletenotes": "<name> <tag> <value>",
        "findcontact": "<second_key (all, phone, birthday, email, address)> <name>",
        "findbytag":"<tag> for searching",
        "name": "<part or full name>",
        "phone": "<part or full phone-number>",
        "birthday": "<part or full date of birthday>",
        "email": "<part or full email>",
        "address": "<part or full address>",
        "peaple":"<number>",
    }
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
    elif com in BOT_HANDLERS["actions"]["addcontact"]["examples"]:
        result = commands["addcontact"](arg[0], arg[1])
    elif com in BOT_HANDLERS["actions"]["addnotes"]["examples"]:
        result = commands["addnotes"](arg[0], arg[1], arg[2])
    elif com in BOT_HANDLERS["actions"]["changecontact"]["examples"]:
        result = commands["changecontact"](arg[0], arg[1], arg[2])
    elif com in BOT_HANDLERS["actions"]["changenotes"]["examples"]:
        result = commands["changenotes"](arg[0], arg[1], arg[2], arg[3])
    elif com in BOT_HANDLERS["actions"]["deletecontact"]["examples"]:
        result = commands["deletecontact"](arg[0], arg[1])
    elif com in BOT_HANDLERS["actions"]["deletenotes"]["examples"]:
        result = commands["deletenotes"](arg[0], arg[1], arg[2])
    elif com in BOT_HANDLERS["actions"]["findcontact"]["examples"]:
        result = commands["findcontact"](arg[0], arg[1])
    elif com in BOT_HANDLERS["actions"]["findbytag"]["examples"]:
        result = commands["findbytag"](arg[0])
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
    elif com in BOT_HANDLERS["actions"]["peaple"]["examples"]:
        result = commands["peaple"](arg[0])
    elif com in BOT_HANDLERS["failure_phrases"] or com == None:
        result = random.choice(BOT_HANDLERS['failure_phrases'])
    return result

def split_command(com):
    for intent in INTENTS:
        for example in BOT_HANDLERS["intents"][intent]["examples"]:
            if re.match(example, com):
                return example, com.split(example)[0].strip()
    for action in ACTIONS:
        for example in BOT_HANDLERS["actions"][action]["examples"]:
            if re.match(example, com):
                return example, com.split(example)[1].strip()
    return 'failure_phrases', random.choice(BOT_HANDLERS['failure_phrases'])


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
        with open("addressbook.bin", "rb") as file:
            my_record = pickle.load(file)

    print("{:>20}{:<300}".format("Your assistent: ", "Hello"))
    while True:
        if key == "" in my_record.data.keys():
            my_record.data.pop(key)
        command = input("{:>20}".format("User: "))
        kommande, argumente = split_command(command)
        if kommande not in BOT_HANDLERS["actions"]["clean"]["examples"]:
            argumente = argumente.lower().split(" ")
        result = parser(kommande, argumente, my_record)
        print("{:>20}{:<300}".format("Your assistent: ", result))
        if result in BOT_HANDLERS["intents"]["exit"]["responses"]:
            break

    with open("addressbook.bin", "wb") as file:
        pickle.dump(my_record, file, 5)


if __name__ == "__main__":
    main()
