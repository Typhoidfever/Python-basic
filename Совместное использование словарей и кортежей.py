schoolClass = {}  # Создание пустого словаря

while True:
    name = input("Enter the student name (or type exit to stop): ")  # Ввод и добавление имени в качестве ключа
    if name == 'exit':  # Условие прерывания цикла (введение текстового значения exit)
        break

    score = int(input("Enter the student score (1-10): "))  # Ввод и добавленя числа от 0 до 10 в качестве значения
    # доступного по ключу

    if name in schoolClass:
        schoolClass[name] += (score,)  # Если имя уже присутствует в словаре удлинить ассоциированный кортеж новым
        # значением с помощью оператора +=
    else:
        schoolClass[name] = (score,)  # Если имя отсутствует в словаре, присвоить ассоциированый кортеж ключу

for name in sorted(schoolClass.keys()):  # Итерация по сортированому списку ключей (имена)
    sum = 0  # создание переменных для вычесления среднего
    counter = 0
    for score in schoolClass[name]:  # Итерация через кортеж значений с обновлением суммы
        sum += score
        counter += 1
    print(name, ":", sum / counter)  # Выведение результата
