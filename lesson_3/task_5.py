import random
random_number = random.randrange(1, 10)

tries = 0
amount_of_tries = 3
while amount_of_tries > tries:
    users_input = int(input("Enter a number in range from 1 to 10: "))
    tries += 1
    if users_input == random_number:
        print("You won!")
    else:
        print("You lose!")