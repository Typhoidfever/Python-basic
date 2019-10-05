import os, glob
metadata_dict = {f: os.stat(f) for f in glob.glob('*.py')} # Генератор словаря с элементом f в качестве ключа и элементом
# os.stat(f) в качестве значения
print(type(metadata_dict))
print(list(metadata_dict.keys())) # В качестве ключей используются имена файлов полученные с помощю функции
# glob.glob('*.py')
print(metadata_dict['trial.py'].st_size) # Определение размера файла

#  Включение условия if и фильтрация входной последовательности с помошью выражения-условия для каждого элемента

import trial
trial_dict = {os.path.splitext(f)[0]: trial.approximate_size(meta.st_size) for f, meta in metadata_dict.items()
              if meta.st_size > 1200}
# При создании словаря отфильровываются файлы с размером менее 1200 байт. Отобраные элементы используются для построения
# словаря ключами которого являются имена файлов без расширения os.path.splitext(f)[0] а значениями приблизительный
# размер каждого файла  trial.approximate_size(meta.st_size)
print(list(trial_dict.keys()))
print(trial_dict['Словари и операции с ними']) # Значение для каждого ключа подбирается с помощью функции
# approximate_size()

# Перестановка местами пары ключ-значение с помощью генератора словарей

a_dict = {1: 'a', 2: 'b', 3: 'c'}
print({value:key for key, value in a_dict.items()}) # Перестановка пар ключ-значение. Работает только если элементы
# словаря не изменяемы
