def running_day():
    x = int(input("Enter how many kilometres sportsman ran for the first day: "))
    y = int(input("Enter how many kilometres you'd like him to reach: "))
    day = 1
    while y > x:
        x *= 1.1
        day += 1
    print(day)
running_day()
