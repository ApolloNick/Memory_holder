dictionary = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}


def check_value_for_dict(dictionary):
    updated_dictionary = {key:value for key, value in dictionary.items() if value is not None}
    return updated_dictionary


print(check_value_for_dict(dictionary))