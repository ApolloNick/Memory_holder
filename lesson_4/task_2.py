import math


def data_from_user():
    sequence_of_integer_numbers = 1
    list_of_data = []
    while sequence_of_integer_numbers != 0:
        sequence_of_integer_numbers = int(input("Enter your integer number for checking: "))
        list_of_data.append(sequence_of_integer_numbers)
    list_of_data.pop(-1)
    return list_of_data


def amount_of_attempts(list_of_data):
    return "Amount of attempts is", len(list_of_data)


def sum_of_numbers(list_of_data):
    return "Sum of numbers is ", sum(list_of_data)


def multiply_of_entered(list_of_data):
    multiply_of_numbers = math.prod(list_of_data)
    return "Multiply of numbers ", multiply_of_numbers


def average_value(list_of_data):
    average = sum(list_of_data)/len(list_of_data)
    return "Average value is ", average

def max_value(list_of_data):
    max_value = max(list_of_data)
    index_of_max_value = list_of_data.index(max_value)
    return "Max value ", [index_of_max_value, max_value]


def even_and_odd_numbers(list_of_data):
    odd_numbers = [odd_number for odd_number in list_of_data if odd_number % 2 == 1]
    length_of_odd = len(odd_numbers)
    even_numbers = len(list_of_data) - length_of_odd
    return "Odd numbers: ", length_of_odd, "Even numbers: ", even_numbers


def second_of_a_value_number(list_of_data):
    list_of_data.sort()
    list_of_data.pop(-1)
    second_value = max_value(list_of_data)
    return "The second max value is ", second_value


def elements_equal_max_value(list_of_data):
    max_value = max(list_of_data)
    list_of_max_value = []
    for number in list_of_data:
        if number == max_value:
            list_of_max_value.append(number)
    return "Quantity of elements equal max value is ", len(list_of_max_value)


def main():
    list_of_nums = data_from_user()
    function_to_call = [amount_of_attempts, sum_of_numbers, multiply_of_entered, average_value,
                        max_value, even_and_odd_numbers, second_of_a_value_number, elements_equal_max_value]
    for func in function_to_call:
        print(func(list_of_nums))


main()

