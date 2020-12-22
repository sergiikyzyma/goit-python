import os
flag, isOperand, isOperator = 0, 0, 0
Variable, Result = 0.0, 0.0
strOperation, strForResult = '', 'Expression = '

while strOperation != '=':                                                                # Приложение выводит результат вычислений когда получает от пользователя =.
    os.system("clear")
    value = input("Enter the number or the operator (+, -, *, /, =), please: ")           # Приложение принимает один операнд или один оператор за один цикл запрос-ответ.
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            strOperation = value
            isOperator += 1                                                               # Пользователь по очереди вводит числа и операторы.
            isOperand = 0
            if strOperation == '+' or strOperation == '-':
                Result = 0
            elif strOperation == '*' or strOperation == '/':
                Result = 1
            elif strOperation == '=':
                continue
            else:
                flag, isOperand, isOperator = 0, 0, 0
                Variable, Result = 0.0, 0.0
                strOperation, strForResult = '', 'Expression = '
                print("You maked the fail by input of operator, please reenrer again")    # Приложение корректно обрабатывает ситуацию некорректного ввода.
                input("Press any key to reentering")
                continue
        else:
            Variable = value
            isOperand += 1                                                                # Пользователь по очереди вводит числа и операторы.
            isOperator = 0
    else:
            Variable = value
            isOperand += 1                                                                # Пользователь по очереди вводит числа и операторы.
            isOperator = 0
    finally:
        if isOperand == 2:                                                                # Если пользователь вводит оператор два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
            flag, isOperand, isOperator = 0, 0, 0
            Variable, Result = 0.0, 0.0
            strOperation, strForResult = '', 'Expression = '
            print("You entered 2 operands successively, please reenrer again/n")
            input("Press any key to reentering")
            continue
        elif isOperator == 2:                                                             # Если пользователь вводит число два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
            flag, isOperand, isOperator = 0, 0, 0
            Variable, Result = 0.0, 0.0
            strOperation, strForResult = '', 'Expression = '
            print("You entered 2 oprrators successively, please reenrer again/n")
            input("Press any key to reentering")
            continue

    if strForResult == 'Expression = ' and Variable != 0:
        strForResult += f'{Variable} '
    if strOperation == '+' and Variable != 0:                                          # Все операции приложение выполняет по мере поступления одну за одной.
        Result += Variable
        flag += 1
        if flag == 2:
            strForResult += f'{strOperation} {Variable} '
            Variable = Result
            strOperation = ''
            flag = 0

    elif strOperation == '-' and Variable != 0:                                        # Все операции приложение выполняет по мере поступления одну за одной.
        if flag == 0:
            Result = Variable
        elif flag == 1:
            Result -= Variable
        flag += 1
        if flag == 2:
            strForResult += f'{strOperation} {Variable} '
            Variable = Result
            strOperation = ''
            flag = 0
            
    elif strOperation == '*' and Variable != 0:                                        # Все операции приложение выполняет по мере поступления одну за одной.
        Result *= Variable
        flag += 1
        if flag == 2:
            strForResult += f'{strOperation} {Variable} '
            Variable = Result
            strOperation = ''
            flag = 0

    elif strOperation == '/' and Variable != 0:                                        # Все операции приложение выполняет по мере поступления одну за одной.
        if flag == 0:
            Result = Variable
        elif flag == 1:
            Result /= Variable
        flag += 1
        if flag == 2:
            strForResult += f'{strOperation} {Variable} '
            Variable = Result
            strOperation = ''
            flag = 0

else:
    print(f"\t\t\t{strForResult}\t\t\tResult = {Result}")                              # Приложение заканчивает свою работу после того, как выведет результат вычисления.