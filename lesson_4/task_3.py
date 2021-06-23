def range_for_list_of_numbers():
    number_a = int(input("Enter an A number for task 3: "))
    number_b = int(input("Enter an B number for task 3: "))
    list_of_numbers = list(range(number_a, number_b + 1))
    if number_b > number_a:
        list_of_numbers.sort()
    else:
        list_of_numbers.sort(reverse=True)
    return list_of_numbers


print(range_for_list_of_numbers())

print(list(range(8, 4)))