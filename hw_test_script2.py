def test_hw2_question1and2(var, var_type=int):
    passed = False
    if not isinstance(var, list):
        print("hw_list1 one is not a list. Remember a list is surrounded by []")
    else:
        if len(var) > 0:
            for idx, val in enumerate(var):
                if not isinstance(val, var_type):
                    print("Not all values in the list were integers. Try again.")
                    break
            if len(var) == 3:
                passed = True
            else:
                print("Did not add exactly three integers to the list.")
        else:
            print("The created list had no items. Make sure to enter values inside the list.")

    print(f"Question {'1' if isinstance(var_type, int) else '2'} passed:", passed)
    return passed


def test_hw2_question3(var):
    passed = False
    if len(var) == 4 and isinstance(var[-1], int) and var[-1] == 10:
        passed = True
    print(f"Question 3 passed:", passed)
    return passed


def test_hw2_question4(var_list, last_value):
    passed = False
    if last_value == 10 and len(var_list) == 3:
        passed = True
    print(f"Question 4 passed:", passed)
    return passed


def test_hw2_question5(var_list):
    passed = False
    if len(var_list) == 6:
        for var in var_list[:3]:
            if not isinstance(var, int):
                break
        for var in var_list[3:]:
            if not isinstance(var, str):
                break
        passed = True
    else:
        print("The items from list 2 were not properly added to hw_list1.")
    print(f"Question 5 passed:", passed)
    return passed


def test_hw2_question6(var_list):
    passed = False
    if len(var_list) == 4:
        for var in var_list[:2]:
            if not isinstance(var, int):
                break
        for var in var_list[2:]:
            if not isinstance(var, str):
                break
        passed = True
    else:
        print("Make sure you sliced right! Remember, the left of the colon is inclusive and the right of the colon is exclusive.")
    print(f"Question 6 passed:", passed)
    return passed
