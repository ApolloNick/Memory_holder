current_number = int(input("Please enter an integer number: "))
number_greater = current_number + 1
number_less = current_number - 1
number_list = [current_number, number_greater, number_less]
next_number = "The next number for the number " + str(number_list[0]) + " is " + str(number_list[1])
print(next_number)

previous_number = "The previous number for the number " + str(number_list[0]) + " is " + str(number_list[2])
print(previous_number)