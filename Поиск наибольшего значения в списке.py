a_list = [13, 3, 6, 34, 45, 678]
largest = a_list[0]

for i in a_list:
    if i > largest:
        largest = i
print(largest)