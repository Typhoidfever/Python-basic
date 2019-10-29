# Обычная модификация


def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):
    print(n, factorialFun(n))


# Рекурсивная модификация (Рекурсия - функция вызывающая сама себя)


def factorial(m):
    if m == 1:  # Условие остановки
        return 1
    else:
        return m * factorial(m - 1)


print(factorial(int(input("Your number: "))))
