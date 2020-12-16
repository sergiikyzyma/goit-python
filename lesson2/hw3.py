intVariable = 0
floatVariable = 0.0
strOperation = ''
flag = 0
while strOperation != '=':
    value = input("Enter a number or a operation, please: ")    # Приложение принимает один операнд или один оператор за один цикл запрос-ответ.
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            strOperation = value
            if strOperation == '+' or strOperation == '-':
                intResult = 0
                floatResult = 0
            elif strOperation == '*' or strOperation == '/':
                intResult = 1
                floatResult = 1
        else:
            floatVariable = value
    else:
            intVariable = value
    if strOperation == '+' and intVariable != 0:
        intResult += intVariable
        flag += 1
        if flag == 2:
            intVariable = intResult
            strOperation = ''
            flag = 0
    elif strOperation == '+' and floatVariable != 0:
        floatResult += floatVariable
        flag += 1
        if flag == 2:
            floatVariable = floatResult
            strOperation = ''
            flag = 0
    else:
        if strOperation == '-' and intVariable != 0:
            if flag == 0:
                intResult = intVariable
            elif flag == 1:
                intResult -= intVariable
            flag += 1
            if flag == 2:
                intVariable = intResult
                strOperation = ''
                flag = 0
        elif strOperation == '-' and floatVariable != 0:
            if flag == 0:
                floatResult = floatVariable
            elif flag == 1:
                floatResult -= floatVariable
            flag += 1
            if flag == 2:
                floatVariable = floatResult
                strOperation = ''
                flag = 0
        else:
            if strOperation == '*' and intVariable != 0:
                intResult *= intVariable
                flag += 1
                if flag == 2:
                    intVariable = intResult
                    strOperation = ''
                    flag = 0
            elif strOperation == '*' and floatVariable != 0:
                floatResult *= floatVariable
                flag += 1
                if flag == 2:
                    floatVariable = floatResult
                    strOperation = ''
                    flag = 0
            else:
                if strOperation == '/' and intVariable != 0:
                    if flag == 0:
                        intResult = intVariable
                    elif flag == 1:
                        intResult /= intVariable
                    flag += 1
                    if flag == 2:
                        intVariable = intResult
                        strOperation = ''
                        flag = 0
                elif strOperation == '/' and floatVariable != 0:
                    if flag == 0:
                        floatResult = floatVariable
                    elif flag == 1:
                        floatResult /= floatVariable
                    flag += 1
                    if flag == 2:
                        floatVariable = floatResult
                        strOperation = ''
                        flag = 0
else:
    if intResult != 0:
        print("Result = ", intResult)
    elif floatResult != 0:
        print("Result = ", floatResult)