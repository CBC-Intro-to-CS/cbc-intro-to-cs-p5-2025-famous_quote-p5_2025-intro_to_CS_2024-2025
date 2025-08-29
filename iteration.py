# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print("Blastoff!")

# purchase_tickets = True
# while purchase_tickets:
#     print("Type '0' to exit")
#     age = int(input("How old are you: "))

#     if age >= 1 and age <= 3:
#         print("Your ticket is free!")
#     elif age >= 4 and age <= 11:
#         print("Your ticket is $10.00")
#     elif age >= 12:
#         print("Your ticket is $15.00")
#     elif age == 0:
#         purchase_tickets = False

# print("Thank you for purchasing tickets!")

# count = 0
# for nums in [3, 41, 12, 9, 74, 15]:
#     count = count + 1
# print("Count: " + str(count))

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()} is a magician.")

# print("Thank you, everyone. That was a good show!")

# Using the Range Function
for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)