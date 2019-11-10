import math  # Подключение модулей к проектуосуществялется с помощью ключевого слова import + название модуля

print(math.sin(math.pi / 2))  # Для использования имён из модуля в проекте к названию переменных, функций и методов
# добавляется указание на модуль через точку слева от имени (определение пространства имён)

from math import pi, sin  # Подключение отдельного элемента из модуля

print(sin(pi / 2))

from math import *  # Импортирование всех элементов модуля (является небезопасным в связи с возможным конфликтом имён)

print(sin(pi / 2))

import math as trigonometry # Подключение существующего модуля в проект под пользовательским именем осуществляется с
# помощью ключевого слова as

print(trigonometry.sin(trigonometry.pi / 2))

