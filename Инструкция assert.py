# Инструкция assert оценивает выражение и если оно является True то исполняет дальнейшие действия. В противном случае
# пробрасывает исключение AssertionError

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)