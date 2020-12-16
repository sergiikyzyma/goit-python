intVariable1, intVariable2, intResult, intVariable = 0, 0, 0, 0
floatVariable1, floatVariable2, floatResult, floatVariable = 0.0, 0.0, 0.0, 0.0
strOperation = ''
flag = False
while strOperation != '=':
    value = input("Enter a number or a operation, please: ")    # Приложение принимает один операнд или один оператор за один цикл запрос-ответ.
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            strOperation = value
        else:
            if not flag:
                floatVariable1 = value
                flag = True
            elif flag:
                floatVariable2 = value
                flag = False
    else:
            if not flag:
                intVariable1 = value
                flag = True
            elif flag:
                intVariable2 = value
                flag = False
    if strOperation == '+' and intVariable1 != 0 and intVariable2 != 0:
        intResult = intVariable1 + intVariable2
        intVariable2 = intResult
        strOperation = ''
    elif strOperation == '+' and floatVariable1 != 0 and floatVariable2 != 0:
        floatResult = floatVariable1 + floatVariable2
        floatVariable2 = floatResult
        strOperation = ''
    else:
        if strOperation == '-' and intVariable1 != 0 and intVariable2 != 0:
            intResult = intVariable1 - intVariable2
            intVariable2 = intResult
            strOperation = ''
        elif strOperation == '-' and floatVariable1 != 0 and floatVariable2 != 0:
            floatResult = floatVariable1 - floatVariable2
            floatVariable2 = floatResult
            strOperation = ''
        else:
            if strOperation == '*' and intVariable1 != 0 and intVariable2 != 0:
                intResult = intVariable1 * intVariable2
                intVariable2 = intResult
                strOperation = ''
            elif strOperation == '*' and floatVariable1 != 0 and floatVariable2 != 0:
                floatResult = floatVariable1 * floatVariable2
                floatVariable2 = floatResult
                strOperation = ''
            else:
                if strOperation == '/':
                    if intVariable2 == 0:
                        print("You must entering operands firstly befor operation")
                    elif floatVariable2 == 0:
                        print("You must entering operands firstly befor operation")
                    else:
                        floatResult = intVariable1 / intVariable2
                        floatResult = floatVariable1 / floatVariable2
                        floatVariable2 = floatResult
                        strOperation = ''
else:
    if intResult != 0:
        print("Result = ", intResult)
    elif floatResult != 0:
        print("Result = ", floatResult)