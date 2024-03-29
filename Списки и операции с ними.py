# Списки - упорядоченные множества произвольных объектов способных к динамическому изменению за счёт добавления\удаления
# элементов

a_list = ['A', 'B', 'C', 1, 2, 3] # Создание списка
print(a_list)

print(len(a_list)) # Определение размера списка функцией len()

# Разрезание списка

print(a_list[3]) # Получение элемента по индексу
print(a_list[1:4]) # Получение элементов между индексами 1 и 4
print(a_list[1:])  # Получение элементов после индекса 1
print(a_list[:3]) # Получение элементов до индекса 3

# Добавление элементов в список

a_list = a_list + [2.0, 'b'] # Добавление элементов в список с использованием оператор +
print(a_list)
a_list.append(True) # Добавление элементов список вызовом метода append()
print(a_list)
a_list.extend(['b', 11, '@']) # Добавление элементов в список вызовом метода extend()
print(a_list)
a_list.insert(2, '#') # Добавление элементов в список вызовом метода insert() с указанием на какую позицию добавить
# элемент
print(a_list)

# Разница в работе методов append() и extend()

a_list.append([10, 12, 13]) # Метод append() добавляет один список в другой в виде одного единого элемента
print(a_list)
a_list.extend(['x', 'y', 'z']) # Метод extend() добавляет каждый элемент одного списка в другой индивидуально
print(a_list)

# Поиск элемента в списке

print(a_list.count(12)) # Определение количества вхождения элементов в список вызовом метода count()
print('#' in a_list) # Определение наличия конкретного элемента в списке оператором in
print(a_list.index('B')) # Определение индекса первого вхождения элемента в список вызовом метода index()

# Удаление элементов из списка

del a_list[4] # Удаление элемента по его индексу в списке оператором del
print(a_list)
a_list.remove('b') # Удаление конкретного элемента вызовом метода remove()
print(a_list)
print(a_list.pop()) # Удаление последнего элемента списка и возврат его значения методом pop()
