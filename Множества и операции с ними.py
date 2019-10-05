# Множества - структуры для не упорядоченного хранения уникальных элементов

# Создание, добавление и поиск элементов множества

a_set = {1, 2} # создание множества
a_set.add(4) # Добавление элемента в множество вызовом метода add()
print(a_set)
print(len(a_set)) # Определение длины множества
a_set.add(1)
print(a_set)
a_set.update({5, 6, 7}) # добавление нескольких элементов во множество вызовом метода update()
print(a_set)
a_set.update({8, 9, 10}, {15, 20, 25})
print(a_set)
a_set.update([30, 40, 50])

# Удаление элементов из множества

print(a_set)
a_set.discard(25) # удаление элемента из множества вызовом метода discard()
print(a_set)
a_set.remove(1) # удаление элемента из множества вызовом метода remove()
print(a_set)
print(a_set.pop()) # удаление случайного элемента из множества и возврат его значения вызавом метода pop()
a_set.clear()
print(a_set)

# Объединение и сравнение множеств

a_set = {1, 2, 4, 5, 6, 7, 8, 9, 10, 40, 15, 50, 20, 25, 30}
print(30 in a_set)
print(95 in a_set)
b_set = {1, 2, 12, 34, 56, 78}
print(a_set)
print(a_set.difference(b_set)) # создание нового множества из элементов которые есть в одном множестве но нет
# в другом вызовом метода difference()
print(a_set.union(b_set)) # создание нового множества объединяющее элементы двух других вызовом метода union()
print(a_set.intersection(b_set)) # создание нового множество содержащее элементы которые есть как в первом так и во
# втором множестве вызовом метода intersection()
print(a_set.symmetric_difference(b_set)) # создание множества содержащего уникальные элементы из обоих множеств
# вызовом метода symmetric_difference()
print(b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set))
print(b_set.union(a_set) == a_set.union(b_set))
print(b_set.intersection(a_set) == a_set.intersection(b_set))
print(b_set.difference(a_set) == a_set.difference(b_set))
print(a_set.issubset(b_set)) # Определиение, является ли одно подмножество частью другого вызовом метода issubset()

