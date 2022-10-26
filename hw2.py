import hw_test_script2

# The first part of this homework is a continuation of the second lesson. PLease move this into that lesson.
my_list = ["first", "second", "third", "fourth", "fifth", "sixth"]

# Slicing a list allows us to grab specific ranges of indexes within a list.
# To grab the first 3 items in the list, use the below. When using slices, the index provided on the right side of the
# colon is exclusive. So in the below example, the items at the 0, 1, and 2 indexes are retrieved, while 3 is the
# cutoff.
print(my_list[:3])

# To grab everything after the first three items in the list, do the below. The first index provided is inclusive.
print(my_list[3:])

# To collect a specific slice, provide a first and last index, but remember the second is exclusive.
print(my_list[2:5])

# The same concept can also be applied to start from the back of the list.
print(my_list[:-2], my_list[-4:-2])

#################################################### HW2 ####################################################
# # Do not comment out your answers after solving the question.
#
# ############# Question 1 #############
# # Create a list with 3 integer values. Once created and the test passes,
hw_list1 = [15, 16, 24]
hw_test_script2.test_hw2_question1and2(hw_list1)
#
# ############# Question 2 #############
# # Create a list with 3 string values
hw_list2 = ["one", "two", "three"]
#
hw_test_script2.test_hw2_question1and2(hw_list2, var_type=str)
#
# ############# Question 3 #############
# # Insert the integer 10 to the end of hw_list1. Enter the code below this line.
#
hw_list1.append(10)
#
hw_test_script2.test_hw2_question3(hw_list1)
#
# ############# Question 4 #############
# # Remove the last value of hw_list1 and set a new variable equal to that value. Pass that new variable into the
# # test_hw2_question4 method's second parameter.
last_item_on_list = hw_list1.pop()

hw_test_script2.test_hw2_question4(hw_list1, last_item_on_list)
#
# ############# Question 5 #############
# # Insert all the items in hw_list2 into hw_list1
#
hw_list1.extend(hw_list2)
print(hw_list1)
hw_test_script2.test_hw2_question5(hw_list1)
#
#
# ############# Question 6 #############
# # Use slicing to grab the last two integers and first two strings from hw_list1 after the previous question.
# # Pass the new variable as a parameter to test_hw2_question6
print(hw_list1)

josh_poop = hw_list1[1:5]
hw_test_script2.test_hw2_question6(josh_poop)
#  left side you start at that exact spot , right side is up to but does not include.