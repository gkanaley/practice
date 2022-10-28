# Loops

# While loop: Evaluates the condition given and continues to iterate until the condition is false
lucky_numbers = [15, 16, 20, 23, 24]

# count = 0
# while count < 4:
#     if count % 2 == 0:
#         print(lucky_numbers[count])
#     else:
#         print("I don't print odd indexes")
#     count = count + 1

# for loop: Continues to iterate over the iterable until no more objects are left


for idx, digit in enumerate(lucky_numbers):
    print(f"Index: {idx}")
    print(f"Digit: {digit}")


# not conditions
even = 2
if not even % 2 == 1:
    print("We're here")
