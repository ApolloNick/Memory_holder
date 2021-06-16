integer_number = int(input("Enter the year which you would like to check: "))
if integer_number % 4 == 0 and integer_number % 100 != 0:
    print("Yes, it's a leap year")
elif integer_number % 400 == 0:
    print("Yes, it's a leap year")
else:
    print("No")