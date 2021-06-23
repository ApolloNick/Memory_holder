factorial = 1
number_for_factorial = int(input("Enter a number to find factorial: "))
if number_for_factorial < 0:
    print("We can't find factorial of negative number")
elif number_for_factorial == 0:
    print("Factorial for zero is 1")
else:
    for number in range(1, number_for_factorial + 1):
        factorial = factorial * number
    print(f"The factorial number of  {number_for_factorial} is {factorial}")