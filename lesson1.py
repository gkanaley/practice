# Variable assignment and basic condition statements
cheese = 13
head = 21
# print(cheese / head)


if cheese == 13 or head == 1:
    print(f"cheese is {cheese} and head is {head}")
elif cheese == 14:
    print("Cheese is 14")
else:
    print("No matches")
print("Hello world")


# Enter a number and if you want to quit, type q.
# This shows the importance of "formatted strings" or f strings
# cmd = input("Type a number\n")
# while cmd != 'q':
#     head = int(cmd)
#     cheese = 5 * head
#     print(f"I typed in {cmd}. Head times cheese is {head * cheese}")
#     cmd = input("Try again?\n")

