a_set =set(range(10))
print(a_set)
print({x**2 for x in a_set}) # Генератор расчитывает квадраты каждого элемента множества чисел
print({x for x in a_set if x % 2 ==0})
print({2**x for x in range(10)})