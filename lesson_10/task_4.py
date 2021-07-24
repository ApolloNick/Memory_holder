def change_string(some_string, previous_item, desired_item, times_of_repeat):
    return some_string.replace(previous_item, desired_item, times_of_repeat)


print(change_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1))
