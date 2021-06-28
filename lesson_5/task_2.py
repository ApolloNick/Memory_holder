def users_input():
    our_input = input("Enter some text: ")
    return f"Amount of symbols is {len(our_input)} ", f"Amount of entered words is {len(our_input.split())} "


print(users_input())

