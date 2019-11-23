# Так как строки представляют собой фактически списки символов с ними можно оперировать как со списками но без
# возможности использовать некоторые их методы (append() и т.д.)

# Индексация строк

exampleString = 'Hello World!'

for ix in range(len(exampleString)):
    print(exampleString[ix], end=' ')

print()

# Итерация сквозь строку

exampleString = 'Hello World!'

for ch in exampleString:
    print(ch, end=' ')
print()

# Разрезание строки

print(exampleString[1 : 4])

# Использование проверки на in и not

print("l" in exampleString)
print("c" not in exampleString)
print('v' in exampleString)
print('H' not in exampleString)

