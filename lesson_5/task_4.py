import random


def remover_for_numbers():
    list_of_random_numbers = []
    length_of_list = len(list_of_random_numbers)
    while length_of_list < 10:
        list_of_random_numbers.append(random.randrange(0, 1000))
        length_of_list +=1
    for index, number in enumerate(list_of_random_numbers):
        if number % 2 != 0:
            list_of_random_numbers[index] = 0
    return list_of_random_numbers


print(remover_for_numbers())

