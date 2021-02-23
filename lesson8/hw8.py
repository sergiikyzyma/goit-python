from datetime import datetime
import random
import string

def congratulate(users):
    main_date = datetime.now()
    while main_date.weekday() != 6:                                                 # We are begining from the next monday
        try:
            temp1 = main_date.day + 1
            main_date = main_date.replace(day=temp1)
        except ValueError:
            temp2 = main_date.month + 1
            main_date = main_date.replace(month=temp2, day=1)
    else:
        for _ in range(30):                                                          # We are searching in next 30 days
            try:
                temp1 = main_date.day + 1
                main_date = main_date.replace(day=temp1)
            except ValueError:
                temp2 = main_date.month + 1
                main_date = main_date.replace(month=temp2, day=1)
            for user in users:
                temp = datetime.strptime(user["birthday"], "%d.%m.%y")
                if (main_date.month == temp.month and main_date.day == temp.day):   # We are searching birthdays
                    temp3 = temp.strftime("%A")
                    temp4 = temp.strftime("%d.%m")
                    if (temp.weekday() == 0 or temp.weekday() == 1 or temp.weekday() == 2 or temp.weekday() == 3 or temp.weekday() == 4):
                        print(f"{temp3}({temp4}) : {user['name']} \n")
                    else:
                        print(f"Monday({temp4}) : {user['name']} \n")

def main():
    users = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    
    for i in range(30):                                                             # We are creating databases of random employers
        day = str(random.randint(1, 28))
        mounth = str(random.randint(1, 12))
        year = str(random.randint(80, 99))
        users[i]["name"] = "".join(random.choices(string.ascii_letters, k=10)).capitalize()
        users[i]["birthday"] = day + "." + mounth + "." + year
    
    congratulate(users)

if __name__ == "__main__":
    main()
