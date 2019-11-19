# Модуль дает доступ к данным подлежащих платформ таким как оборудование, операционные системы и интерпретатор

from platform import platform

print(platform()) # Функция platform() предоставляет информацию об операционной системе и архитектуре ядра
print(platform(1))
print(platform(0, 1))

from platform import machine

print(machine())  # Функция machine() возврашает только архитектуру процессора

from platform import processor

print(processor()) # Функция processor() возвращает имя процессора (когда это разрешено)

from platform import system

print(system()) # Функция system() возвращает название опирационной системы

from platform import version

print(version()) # Функция version() возвращает информацию о версии операционной системы

from platform import python_implementation, python_version_tuple

print(python_implementation()) # Функция python_implementation() возвращает информацию о используемой реализации
# интерпретатора Python

for art in python_version_tuple(): # Функция python_version_tuple возвращает трёх элементный кортеж с информацией о
    # версии языка и номере патча
    print(art)

