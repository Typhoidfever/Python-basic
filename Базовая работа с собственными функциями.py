# Создание собственной функции производится с использованием инструкции def

def new_func():  # определение функции
    print("spam")
    print("spam")
    print("spam")  # Тело функции


new_func()  # Вызов функции


def hello(name):  # Определение функции с параметром name который передаёт в функцию переменную содержащую строку
    # введённую с клавиатуры
    print("Hello ", name)


name = input("Enter your name: ")

hello(name)


# Передача параметров функции по позиции

def my_func(firstName, lastName):
    print("Hello my name is ", firstName, lastName)


my_func("Name", "Second Name")
my_func("Second Name", "Name")


# Передача параметров функции по ключевому слову

def my_func2(firstName, lastName):
    print("Hello my name is ", firstName, lastName)


my_func2(firstName="Name", lastName="Second Name")  # Для передачи параметра функции по ключевому слову используется
# оператор присвоения
my_func2(lastName="Second Name", firstName="Name")


# Функции с предопределёнными параметрами

def introduction(firstName, lastName="Smith"):  # При создании функции один из параметров которые она принемает был
    # предопределён
    print("Hello my name is ", firstName, lastName)


introduction("John")  # При вызове функции с предопределённым параметром достаточно определить оставшиеся.
# Если все параметры которые принемает функция предопределены во время вызова функции в скобках ничего не указывают
