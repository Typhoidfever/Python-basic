import time

for i in range(100): # Инструкция break прерывает выполнение цикла
    if i == 6:
        break
    print("Inside the loop ", i)
    time.sleep(1)
print ("Outside the loop")


for i in range(1, 10): # Инструкция continue возвращает выполнение цикла в его начало
    if i == 4:
        continue
    print ("Inside the loop ", i)
    time.sleep(1)
print("Outside the loop")
