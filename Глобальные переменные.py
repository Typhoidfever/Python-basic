# Глобальные переменные создаются с помощью ключевого слова global


def myFunction():
    global var  # Переменная, объявленная глобальной не будет заново создаваться как внутри так и снаружи функции
    var = 2
    print("Do I know the variable? ", var)


var = 1
myFunction()
print(var)
