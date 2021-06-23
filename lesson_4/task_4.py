def stairs_of_range():
    integer_number = int(input("Enter integer value till or equal nine: "))
    support_var = []
    if integer_number <= 9:
        for value in range(1, integer_number):
            support_var.append(str(value))
            variable_for_iterating = "".join(support_var)
            print(variable_for_iterating)
    else:
        print("You number don't fit in for this task. Try another one!")


stairs_of_range()


