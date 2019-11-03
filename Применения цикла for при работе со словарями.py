# Цикл for не может применятся со словарями на прямую. Для его применения необходимо проводить определённые
# преобразования

# Получение всех значений по всем ключам с помощью цикла for церез создание списка ключей

b_dict = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in b_dict:
        print(word, "->", b_dict[word])
    else:
        print(word, "->", "is not in a dictionary")

# Получение всех значений по всем ключам с помощью цикла for с использованием метода keys()

b_dict = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in b_dict.keys():  # Метод keys() возвращает список состоящий из ключей словаря
    print(key, "->", b_dict[key])

# Метод keys() может применятся совместно с функцией sorted() для упорядочивания ключей в списке

b_dict = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in sorted(b_dict.keys()):
    print(key, "->", b_dict[key])

# Получение всех значений по всем ключам с помощью цикла for с использованием метода items()

b_dict = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in b_dict.items():  # Метод items() возвращает два кортежа: кортеж ключей и кортеж значений и
    # споставляет элементы кортежей между собой при этом кортежи выступают в роли переменных для цикла
    print(english, "->", french)

# Получение списка значений с помощью метода values()

b_dict = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in b_dict.values():  # словари не способны возвращать ключи по значениям, поэтому метод values() просто
    # возвращает список значений словаря
    print(french)
