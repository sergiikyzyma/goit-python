import re

def input_error():
    pass

def hello():
    return "How can I help you?"

def add(adress_book, name, phone):
    if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", phone):
        adress_book[name] = phone
        return "added " + name + " " + phone
    else:
        return "false phone-number (must be in format XXX-XXX-XX-XX)"

def change(adress_book, name, phone):
    try:
        adress_book.pop(name)
    except KeyError:
        return "missing name in database"
    if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", phone):
        adress_book[name] = phone
        return "chahged " + name + " " + phone
    else:
        return "false phone-number (must be in format XXX-XXX-XX-XX)"

def phone(adress_book, name):
    try:
        phone = adress_book.pop(name)
    except KeyError:
        return "missing name in database"
    adress_book[name] = phone
    return phone

def showall(adress_book):
    return str(adress_book)

def ausgang():
    return "Good bye!"

def parser(adress_book, com):
    commands = {"hello": hello, "add": add, "change": change, "phone": phone, "show all": showall, "exit": ausgang, "close": ausgang, "good bye": ausgang}
    
    if com[0] == "exit" or com[0] == "close":
        result = handler(commands[com[0]])
    elif com[0] == "good" and len(com) > 1:
        result = handler(commands[com[0] + " " + com[1]]) if com[1] == "bye" else "You wrote wrong 'good bye'"
    elif com[0] == "hello":
        result = handler(commands[com[0]])
    elif com[0] == "add" and len(com) > 2:
        result = handler(commands[com[0]], adress_book, com[1], com[2])
    elif com[0] == "change" and len(com) > 2:
        result = handler(commands[com[0]], adress_book, com[1], com[2])
    elif com[0] == "phone" and len(com) > 1:
        result = handler(commands[com[0]], adress_book, com[1])
    elif com[0] == "show" and len(com) > 1:
        result = handler(commands[com[0] + " " + com[1]], adress_book) if com[1] == "all" else "You wrote wrong 'show all'"
    else:
        result = "You maked the fail by inputing the command or the number of params!"
    return result

def handler(func, *arg):
    return func(*arg)

def main():
    adress_book = dict()
    result = ""

    while result != "Good bye!":
        command = input("{:>20}".format("User: "))
        com = command.lower().split(" ")
        result = parser(adress_book, com)
        print("{:>20}{:<300}".format("Your assistent: ", result))

if __name__ == "__main__":
    main()
