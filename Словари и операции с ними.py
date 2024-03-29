# Словари - неупорядоченное множество пар ключ-значение

# Создание словаря и получение элементов по ключу

a_dict = {'server': 'db.python3.org', 'database': 'mysql'}  # Создание словаря содержащего две пары ключ-значение
print(a_dict)
print(a_dict['server'])  # Получение значения по ключу

# Изменение словаря

a_dict['database'] = 'blog'  # Изменение значения аффилированного с ключом
print(a_dict)
a_dict['user'] = 'mark'  # Добавление новой пары ключ-значение
print(a_dict)
a_dict['User'] = 'mark'  # Демонстрация регистрозависимости ключа - Ключ 'User' - другой ключ
print(a_dict)
a_dict.update({'web_server': 'nginx'})  # Добавление новой пары ключ-значение с помощью метода update()
print(a_dict)

# Словари со смешанными значениями

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
print(len(SUFFIXES))  # Возврат количества элементов словаря вызовом функции len()
print(1000 in SUFFIXES)  # Определение наличия определённого ключа в словаре
print(SUFFIXES[1024])  # Получение набора значений аффилированных с ключом
print(SUFFIXES[1000][3])  # Получение конкретного элемента из списка по порядковому номеру. Список является
# значением словаря, доступным по ключу '1000'

# Удаление и очистка словарей

# Удаление элементов словаря или целого словаря производится с помощью метода del()

del a_dict["server"]  # Удаление одной пары ключ-значение
print(a_dict)

b_dict = {'1': '2', '3': '4'}
print(b_dict)
del b_dict

# Очистка словаря осуществляется с помощью метода clear()

a_dict.clear()  # Метод возвращает пустой словарь
print(a_dict)

# Копирование элементом одного словаря в другой осуществляется с помощью метода copy()

b_dict = {'1': '2', '3': '4'}
c_dict = b_dict.copy()
print(c_dict)
