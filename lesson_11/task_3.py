name_list = ["ШАЛАШ", "КАЗАК", "ДЕД", "ДОХОД", "13231"]


def adjust_indention(list_of_data, n):
    if n > 0:
        print(str(list_of_data).rjust(n))
    elif n < 0:
        print(str(list_of_data).ljust(n))
    else:
        print("You don't change an indention")


adjust_indention(name_list, 50)
