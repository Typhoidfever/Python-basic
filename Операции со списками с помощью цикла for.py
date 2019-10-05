a_list = [] # Создание пустого списка

for i in range(10):
    a_list.append(i + 1) # Добавление в список 10 элементов с помощью метода  append() и цикла for
print(a_list)

for i in range(10):
    a_list.insert(0, i+1) # Добавление в список 10 элементов с помощью метода  insert() и цикла for.
    # При этом элементы добавляются в список в обратном порядке
print(a_list)

# Определение суммы всех элементов списка

b_list = [10, 7, 1, 3, 56]
total = 0

for i in range(len(b_list)): # Переменная i принемает значения по индексу элемента в списке и добавляет каждый элемент
    # в переменную тотал в которой происходит их суммирование с каждой итерацией цикла
    total += b_list[i]
print(total)

c_list = [12, 45, 67, 1090]
total = 0

for i in c_list:
    total += i
print(total)

# Изменение порядка следования элементов в списке (инверсия)

d_list = [10, 123, 5, 6, 1234]
length = len(d_list)

for i in range(length // 2):
    d_list[i], d_list[length - 1 -i] = d_list [length - 1 - i], d_list[i]
print(d_list)