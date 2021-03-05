import re

def input_error(func):
    def inner(adress_book, com):
        my_error_1 = "Missing name in database!"
        my_error_2 = "Wrong phone-number (must be in format XXX-XXX-XX-XX)!"
        my_error_3 = "You maked the fail by inputing the command!"
        my_error_4 = "You maked the fail by inputing the number of arguments!"
        my_error_5 = "You wrote wrong the compound commmnd 'good bye'!"
        my_error_6 = "You wrote wrong the compound command 'show all'!"
        try:
            res = func(adress_book, com)
        except KeyError:
            return my_error_1
        except ValueError:
            return my_error_2
        except UnboundLocalError:
            return my_error_3
        except IndexError:
            return my_error_4
        except TypeError:
            return my_error_5
        except NameError:
            return my_error_6
        else:
            return res
    return inner

def hello():
    return "How can I help you?"

def add(adress_book, name, phone):
    if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", phone):
        adress_book[name] = phone
        return "added " + name + " " + phone
    else:
        raise ValueError

def change(adress_book, name, phone):
    if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", phone):
        adress_book.pop(name)
        adress_book[name] = phone
        return "chahged " + name + " " + phone
    else:
        raise ValueError

def phone(adress_book, name):
    phone = adress_book.pop(name)
    adress_book[name] = phone
    return phone

def showall(adress_book):
    return str(adress_book)

def ausgang():
    return "Good bye!"

@input_error
def parser(adress_book, com):
    commands = {"hello": hello, "add": add, "change": change, "phone": phone, "show all": showall, "exit": ausgang, "close": ausgang, "good bye": ausgang}
    
    if com[0] == "exit" or com[0] == "close":
        result = handler(commands[com[0]])
    elif com[0] == "good" and len(com) > 1:
        if com[1] == "bye":
            result = handler(commands[com[0] + " " + com[1]])
        else:
            raise TypeError
    elif com[0] == "hello":
        result = handler(commands[com[0]])
    elif com[0] == "add":
        result = handler(commands[com[0]], adress_book, com[1], com[2])
    elif com[0] == "change":
        result = handler(commands[com[0]], adress_book, com[1], com[2])
    elif com[0] == "phone":
        result = handler(commands[com[0]], adress_book, com[1])
    elif com[0] == "show" and len(com) > 1:
        if com[1] == "all":
            result = handler(commands[com[0] + " " + com[1]], adress_book)
        else:
            raise NameError
    return result

def handler(func, *arg):
    return func(*arg)

def main():
    adress_book = dict()
    result = ""
    
    print("{:>20}{:<300}".format("Your assistent: ", "Hello"))
    while result != "Good bye!":
        command = input("{:>20}".format("User: "))
        com = command.lower().split(" ")
        result = parser(adress_book, com)
        print("{:>20}{:<300}".format("Your assistent: ", result))

if __name__ == "__main__":
    main()
