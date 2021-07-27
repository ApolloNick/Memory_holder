def users_input():
    info = input("Enter text file for writing: ")
    return info


def write_file(data):
    with open('users_input.txt', 'w') as file:
        file.write('\n'.join(data.split()))
        file.write("\n")


write_file(users_input())