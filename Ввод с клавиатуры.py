#  Ввод данных с клавиатуры осуществляется с помощью функции input()
nameUser = input()
cityUser = input()

print("Your name is {0}. Your city is {1}.". format(nameUser, cityUser)) # Форматирование с использованием метода
# format()


nameUser = input ("Put your name: ")
cityUser = input ("Put your city: ")

print("Your name is {0}. Your city is {1}.". format(nameUser, cityUser))

# Функция input() принимает и выводит строки. Для вывода чисел необходимо проводить явное преобразования типов с помощью
# функций int() или float()

qtyOranges = input("How many oranges? ")
priceOranges = input ("What is a price? ")

qtyOranges = int(qtyOranges)
priceOranges = float(priceOranges)

sumOranges = qtyOranges * priceOranges

print("Please, pay", sumOranges,  "dollars")



# Примеры

userName = input("What is your name? ")
userAge = input("How old are you? ")
userCity = input("Where do you live? ")

print("This is ", userName)
print("It is ", userAge)
print("(S)he is from ", userCity)


value1 = int(input())
value2 = int(input())
value3 = int(input())
value4 = int(input())

sum1 = value1 + value2
sum2 = value3 + value4

print("The answer is %.2f" % (sum1 / sum2)) # Си-подобное форматирование с ограничением вывода до двух знаков после
# запятой
