import math

def amount_of_entered_numbers():
    sequence_of_integer_numbers = 1
    attempts = -1
    list_of_attempts = []
    while sequence_of_integer_numbers != 0:
        sequence_of_integer_numbers = int(input("Enter your integer number for checking: "))
        attempts += 1
        list_of_attempts.append(sequence_of_integer_numbers)
    return attempts


def sum_of_numbers():
    sequence_of_integer_numbers = 1
    list_of_attempts = []
    while sequence_of_integer_numbers != 0:
        sequence_of_integer_numbers = int(input("Enter your integer number for checking: "))
        list_of_attempts.append(sequence_of_integer_numbers)
        if sequence_of_integer_numbers == 0:
            list_of_attempts.pop(-1)
    sum_of_numbers = sum(list_of_attempts)
    return sum_of_numbers


def multiply_of_entered():
    sequence_of_integer_numbers = 1
    list_of_attempts = []
    while sequence_of_integer_numbers != 0:
        sequence_of_integer_numbers = int(input("Enter your integer number for checking: "))
        list_of_attempts.append(sequence_of_integer_numbers)
        if sequence_of_integer_numbers == 0:
            list_of_attempts.pop(-1)
    multiply_of_numbers = math.prod(list_of_attempts)
    return multiply_of_numbers


def average_value():
    sequence_of_integer_numbers = 1
    list_of_attempts = []
    while sequence_of_integer_numbers != 0:
        sequence_of_integer_numbers = int(input("Enter your integer number for checking: "))
        list_of_attempts.append(sequence_of_integer_numbers)
        if sequence_of_integer_numbers == 0:
            list_of_attempts.pop(-1)
    average = sum(list_of_attempts)/len(list_of_attempts)
    return average

def max_value():
    sequence_of_integer_numbers = 1
    attempts = -1
    list_of_attempts = []
    while sequence_of_integer_numbers != 0:
        sequence_of_integer_numbers = int(input("Enter your integer number for checking: "))
        attempts += 1
        list_of_attempts.append(sequence_of_integer_numbers)
        if sequence_of_integer_numbers == 0:
            list_of_attempts.pop(-1)
    max_value = max(list_of_attempts)
    index_of_max_value = list_of_attempts.index(max_value)
    return [index_of_max_value, max_value]


def even_and_odd_numbers():
    sequence_of_integer_numbers = 1
    list_of_attempts = []
    while sequence_of_integer_numbers != 0:
        sequence_of_integer_numbers = int(input("Enter your integer number for checking: "))
        list_of_attempts.append(sequence_of_integer_numbers)
        if sequence_of_integer_numbers == 0:
            list_of_attempts.pop(-1)
    odd_numbers = [odd_number for odd_number in list_of_attempts if odd_number % 2 == 1]
    length_of_odd = len(odd_numbers)
    even_numbers = len(list_of_attempts) - length_of_odd
    return "Odd numbers: ", length_of_odd, "Even numbers: ", even_numbers


def second_of_a_value_number():
    sequence_of_integer_numbers = 1
    list_of_attempts = []
    while sequence_of_integer_numbers != 0:
        sequence_of_integer_numbers = int(input("Enter your integer number for checking: "))
        list_of_attempts.append(sequence_of_integer_numbers)
        if sequence_of_integer_numbers == 0:
            list_of_attempts.pop(-1)
    list_of_attempts.sort()
    second_value = list_of_attempts[-2]
    return second_value


def elements_equal_max_value():
    sequence_of_integer_numbers = 1
    list_of_attempts = []
    while sequence_of_integer_numbers != 0:
        sequence_of_integer_numbers = int(input("Enter your integer number for checking: "))
        list_of_attempts.append(sequence_of_integer_numbers)
        if sequence_of_integer_numbers == 0:
            list_of_attempts.pop(-1)
    max_value = max(list_of_attempts)
    list_of_max_value = []
    for number in list_of_attempts:
        if number == max_value:
            list_of_max_value.append(number)
    return len(list_of_max_value)


print(elements_equal_max_value())

