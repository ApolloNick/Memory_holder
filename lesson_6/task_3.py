def match_the_value(x):
    keys_for_my_dict = enumerate(alphabet)
    my_dict = dict((key, value) for key, value in keys_for_my_dict)
    return my_dict


alphabet = ['a', 'b', 'c', 'd', 'e']
print(match_the_value(alphabet))

