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
    if strOperation == '+' and intVariable1 != 0 and intVariable1 != 0:
        intResult = intVariable1 + intVariable2
        intVariable2 = intResult
        strOperation = ''
    elif strOperation == '+' and floatVariable1 != 0 and floatVariable1 != 0:
        floatResult = floatVariable1 + floatVariable2
        floatVariable2 = floatResult
        strOperation = ''
    else:
        if strOperation == '-' and intVariable1 != 0 and intVariable1 != 0:
            intResult = intVariable1 - intVariable2
            intVariable2 = intResult
            strOperation = ''
        elif strOperation == '-' and floatVariable1 != 0 and floatVariable1 != 0:
            floatResult = floatVariable1 - floatVariable2
            floatVariable2 = floatResult
            strOperation = ''
        else:
            if strOperation == '*' and intVariable1 != 0 and intVariable1 != 0:
                intResult = intVariable1 * intVariable2
                intVariable2 = intResult
                strOperation = ''
            elif strOperation == '*' and floatVariable1 != 0 and floatVariable1 != 0:
                floatResult = floatVariable1 * floatVariable2
                floatVariable2 = floatResult
                strOperation = ''
            else:
                if strOperation == '/' and intVariable1 != 0 and intVariable1 != 0:
                    if intVariable2 == 0:
                        print("You must entering operands firstly befor operation")
                    else:
                        intResult = intVariable1 / intVariable2
                        intVariable2 = intResult
                        strOperation = ''
                elif strOperation == '/':
                    if intVariable2 == 0:
                        print("You must entering operands firstly befor operation")
                    else:
                        floatResult = floatVariable1 / floatVariable2
                        floatVariable2 = floatResult
                        strOperation = ''
    '''try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            strOperation = value
        else:
            floatVariable = value
    else:
            intVariable = value
    if strOperation == '+' and intVariable != 0:
        intResult += intVariable
        flag += 1
        if flag == 2:
            intVariable = 0
    elif strOperation == '+' and floatVariable != 0:
        floatResult += floatVariable
        flag += 1
        if flag == 2:
            intVariable = 0
    else:
        if strOperation == '-' and intVariable != 0:
            intResult -= intVariable
            flag += 1
            if flag == 2:
                intVariable = 0
        elif strOperation == '-' and floatVariable != 0:
            floatResult -= floatVariable
            flag += 1
            if flag == 2:
                intVariable = 0
        else:
            if strOperation == '*' and intVariable != 0:
                intResult *= intVariable
                flag += 1
                if flag == 2:
                    intVariable = 0
            elif strOperation == '*' and floatVariable != 0:
                floatResult *= floatVariable
                flag += 1
                if flag == 2:
                    intVariable = 0
            else:
                if strOperation == '/' and intVariable != 0:
                    intResult /= intVariable
                    flag += 1
                    if flag == 2:
                        intVariable = 0
                elif strOperation == '/' and floatVariable != 0:
                    floatResult /= floatVariable
                    flag += 1
                    if flag == 2:
                        intVariable = 0'''
else:
    if intResult != 0:
        print("Result = ", intResult)
    elif floatResult != 0:
        print("Result = ", floatResult)