name_list = ["ШАЛАШ", "КАЗАК", "ДЕД", "ДОХОД", "13231"]


def check_name(sequence_of_names):
    for item in sequence_of_names:
        if item == item[::-1]:
            print("You win")
        else:
            print("You lose")


check_name(name_list)
