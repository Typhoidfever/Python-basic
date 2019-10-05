# None - специальная константа означающая пустое значение

print(type(None)) # Констатнта None относится к особому классу NoneType
print(None == False) # None не тождественно False (выражение вернёт False)
print(None == 0)  # None не тождественно 0 (выражение вернёт False)
print(None == None) # None тождественно None (выражение вернёт True)
x = None # Значение None можно присвоить переменной
print(x == None) # выражение вернёт True
y = None
print(y == x) # выражение вернёт True аналогично случаю None == None
