current_number = int(input("Please enter an integer number: "))
number_greater = current_number + 1
number_less = current_number - 1
next_number = "The next number for the number " + str(current_number) + " is " + str(number_greater)
print(next_number)

previous_number = "The previous number for the number " + str(current_number) + " is " + str(number_less)
print(previous_number)