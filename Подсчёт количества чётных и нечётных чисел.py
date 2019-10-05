even_number = 0
odd_number = 0

number = int(input("Enter the number: "))

while number != 0:
    if number % 2 == 1:
        odd_number += 1
    else:
        even_number += 1

    number = int(input("Enter the number: "))

print("Odd number count ", odd_number)
print("Even number count ", even_number)
