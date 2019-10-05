myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
tempList = []

for i in myList:
    if i not in tempList:
        tempList.append(i)
    elif i in tempList:
        continue

myList = tempList[:]
del tempList
print("The list with unique elements only")
print(myList)