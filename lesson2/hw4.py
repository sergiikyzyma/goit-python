import os
intVariable, intResult, flag, isOperand, isOperator = 0, 0, 0, 0, 0
floatVariable, floatResult = 0.0, 0.0
strOperation, strForResult = '', 'Expression = '

while strOperation != '=':                                          # Приложение выводит результат вычислений когда получает от пользователя =.
    os.system("clear")
    value = input("Enter the number or the operation, please: ")    # Приложение принимает один операнд или один оператор за один цикл запрос-ответ.
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            strOperation = value
            isOperator += 1                                         # Пользователь по очереди вводит числа и операторы.
            isOperand = 0
            if strOperation == '+' or strOperation == '-':
                intResult = 0
                floatResult = 0
            elif strOperation == '*' or strOperation == '/':
                intResult = 1
                floatResult = 1
            elif strOperation == '=':
                continue
            else:
                intVariable, intResult, flag, isOperand, isOperator = 0, 0, 0, 0, 0
                floatVariable, floatResult = 0.0, 0.0
                strOperation, strForResult = '', 'Expression = '
                print("You maked the fail by input")               # Приложение корректно обрабатывает ситуацию некорректного ввода.
                input("Press any key to reenter")
                continue
        else:
            floatVariable = value
            isOperand += 1                                          # Пользователь по очереди вводит числа и операторы.
            isOperator = 0
    else:
            intVariable = value
            isOperand += 1                                          # Пользователь по очереди вводит числа и операторы.
            isOperator = 0
    finally:
        if isOperand == 2:                                          # Если пользователь вводит оператор два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
            intVariable, intResult, flag, isOperand, isOperator = 0, 0, 0, 0, 0
            floatVariable, floatResult = 0.0, 0.0
            strOperation, strForResult = '', 'Expression = '
            print("You entered 2 operands successively, please reenrer again/n")
            input("Press any key to reenter")
            continue
        elif isOperator == 2:                                       # Если пользователь вводит число два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
            intVariable, intResult, flag, isOperand, isOperator = 0, 0, 0, 0, 0
            floatVariable, floatResult = 0.0, 0.0
            strOperation, strForResult = '', 'Expression = '
            print("You entered 2 oprrators successively, please reenrer again/n")
            input("Press any key to reenter")
            continue

    if strForResult == 'Expression = ' and intVariable != 0:
        strForResult += f'{intVariable} '
    elif strForResult == 'Expression = ' and floatVariable != 0.0:
        strForResult += f'{floatVariable} '
    if strOperation == '+' and intVariable != 0:                    # Все операции приложение выполняет по мере поступления одну за одной.
        intResult += intVariable
        flag += 1
        if flag == 2:
            strForResult += f'{strOperation} {intVariable} '
            intVariable = intResult
            strOperation = ''
            flag = 0
    elif strOperation == '+' and floatVariable != 0:
        floatResult += floatVariable
        flag += 1
        if flag == 2:
            strForResult += f'{strOperation} {floatVariable} '
            floatVariable = floatResult
            strOperation = ''
            flag = 0

    elif strOperation == '-' and intVariable != 0:                  # Все операции приложение выполняет по мере поступления одну за одной.
        if flag == 0:
            intResult = intVariable
        elif flag == 1:
            intResult -= intVariable
        flag += 1
        if flag == 2:
            strForResult += f'{strOperation} {intVariable} '
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
            strForResult += f'{strOperation} {floatVariable} '
            floatVariable = floatResult
            strOperation = ''
            flag = 0
            
    elif strOperation == '*' and intVariable != 0:                  # Все операции приложение выполняет по мере поступления одну за одной.
        intResult *= intVariable
        flag += 1
        if flag == 2:
            strForResult += f'{strOperation} {intVariable} '
            intVariable = intResult
            strOperation = ''
            flag = 0
    elif strOperation == '*' and floatVariable != 0:
        floatResult *= floatVariable
        flag += 1
        if flag == 2:
            strForResult += f'{strOperation} {floatVariable} '
            floatVariable = floatResult
            strOperation = ''
            flag = 0

    elif strOperation == '/' and intVariable != 0:                  # Все операции приложение выполняет по мере поступления одну за одной.
        if flag == 0:
            intResult = intVariable
        elif flag == 1:
            intResult /= intVariable
        flag += 1
        if flag == 2:
            strForResult += f'{strOperation} {intVariable} '
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
            strForResult += f'{strOperation} {floatVariable} '
            floatVariable = floatResult
            strOperation = ''
            flag = 0

else:
    print(f"\t\t\t{strForResult}\t\t\tResult (operands are integer) = {intResult} \t\t\tResult (operands are float) = {floatResult}")    # Приложение заканчивает свою работу после того, как выведет результат вычисления.