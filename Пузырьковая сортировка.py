my_list = [10, 2, 6, 8, 4] # Создание списка для сортировки
swapped = True # Переменная созданная для введения цикла while

while swapped: # Цикл перестановки
    swapped = False # Перестановка не произведена
    for i in range(len(my_list) - 1): # Для сортировки необходимо провести 5 сравнений
        if my_list[i] > my_list[i + 1]: # Введение условия для перестановки
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # Осуществление перестановки
print(my_list)

# Сортировка списка заданного пользователем

userList = [] # Создание пустого списка
swapped = True
num = int(input("Enter the list length: ")) # Указание длины списка

for i in range(num):
    val = float(input("Enter your value: "))
    userList.append(val) # Введение элементов и добавление их в список

while swapped: # Сортировка
    swapped = False
    for i in range(len(userList) - 1):
        if userList[i] > userList[i+1]:
            swapped = True
            userList[i], userList[i + 1] = userList[i + 1], userList [i]
print(userList)

    