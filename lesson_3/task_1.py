users_number = int(input("Enter three digit number: "))
result = 0
while users_number > 0:
    digit = users_number % 10
    # to find the last number in users_number
    result = result + digit
    users_number = users_number // 10
    # to remove the last number in users_number
print("Your sum is: ", result)