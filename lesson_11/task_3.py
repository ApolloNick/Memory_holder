name_list = ["ШАЛАШ", "КАЗАК", "ДЕД", "ДОХОД", "13231", "White", "Black", "Gray", "Git", "Push"]


def change_place(list_of_data, n):
    n = -n % len(list_of_data)
    return list_of_data[n:] + list_of_data[:n]


print(change_place(name_list, 6))
