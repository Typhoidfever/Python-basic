# Инструкция return используется в функциях когда они возвращают какое-то значение

# Инструкция return имеет два варианта использования

# Вариант 1 возврат без выражения

def happyNewYear(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")

    if not wishes:
        return
    print("Happy New Year!")


happyNewYear()
happyNewYear(False)  # Если функции happyNewYear() во время вызова передан аргумент False, инструкция return прервёт


# выполнение программы, тогда вызов функции без аргумента приведёт к полному выполнению кода

# Вариант 2 возврат с выражением

def boringFunction():
    return 123


x = boringFunction()

print("The boringFunction has returned its result. Result is:", x)  # Инструкция return моментально препывает


# выполнение функции, оценивает значение выражения и возвращает его как резултат работы функции сохранённый в переменной
# х


# В качестве аргумента созданной функции может быть передан список

def sumOfList(lst):
    sum = 0

    for i in lst:
        sum += i

    return sum


print(sumOfList([5, 4, 3]))  # Функция принемает в качестве фргумента список и возвращает его сумму


# Функция может возвращать список в качестве результата своей работы

def strangeListFunction(n):
    strangeList = []

    for i in range(0, n):
        strangeList.insert(0, i)

    return strangeList


print(strangeListFunction(10)) # Функция принемает значение длины списка и возвращает список длины n в котором элементы
# следуют от большего к меньшему
