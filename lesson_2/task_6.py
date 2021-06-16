list_of_numbers = list(range(10, 101, 10))
number_for_checking = int(input("Enter number x: "))
prepared_number = abs(number_for_checking)
if prepared_number in list_of_numbers:
    print("Yeah, you chose the right one")
else:
    print("Sorry, you number out of range. Try again")

