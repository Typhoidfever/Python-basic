# Работа с файлами и каталогами в python осуществляется с помошью модуля os

import os # Подключение модуля к проекту

# Определение и изменение рабочего каталога

print(os.getcwd()) # Получение значения текущего рабочего каталога вызовом метода os.getcwd()
os.chdir('/home/typhoid/PycharmProjects') # Смена текущего каталога вызовом метода os.chdir()
print(os.getcwd())
os.chdir('/home/typhoid/PycharmProjects/untitled')

# Работа с именами файлов и каталогов

print(os.path.join('/home/typhoid/PycharmProjects/untitled', 'trial.py')) # Составление пути к каталогу из одной или
 # нескольких частей вызовом метода os.path.join()
print (os.path.expanduser('~')) # Определение пути к каталогу пользователя вызовом метода s.path.expanduser()

# Разбиение путей на составные части инструментами метода os.path()

pathname = '/home/typhoid/PycharmProjects/untitled/trial.py'
print(os.path.split(pathname)) # Дробление полного пути и возврат кортежа из имени пути и имени файла с помощью
# инструмента os.path.split()
(dirname, filename) = os.path.split(pathname)
print(dirname)
print(filename)
(shortname, extension) = os.path.splitext(filename) # Дробление имени файла и возврат кортежа из имени файла и
# расширения с помощью инструмента os.path.splitext()
print(shortname)
print(extension)

# Получение содержимого каталога

os.chdir('/home/typhoid/PycharmProjects')
import glob # Импорт модуля globe, который принемает шаблон, содержащий символы-джокеры и возвращающий пути всех
# файлов соответствующих им
print(glob.glob('/*.xml'))
os.chdir('/home/typhoid/PycharmProjects/untitled')
print(glob.glob('**.py'))

# Получение сведений о файле

metadata = os.stat('trial.py') # Возврат объекта содержащего метаданные о файле с помощью метода os.stat()
print(metadata.st_mtime) # Возврат информации сколько времени в секундах прошло с начала эры Unix в момент изменения
# файла
import time # Подключение модуля для работы со временем Time из стандартной библиотеки python
print(time.localtime(metadata.st_mtime)) # Преобразование времени из секунд с начала эры в более удобный формат c
# помощью метода time.localtime()
print(metadata.st_size) # Получение размера файла с помощью свойства st_size метода os.stat()
print(os.path.realpath('trial.py')) # Получение абсолютного пути к файлу с помощью метода os.path.realpath()
