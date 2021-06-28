day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))


def is_date(day, month, year):
    if day < 1 or day > 31:
        print("False")
    elif month < 1 or month > 12:
        print("False")
    elif year < 1 or year > 9999:
        print("False")
    else:
        print("True")


is_date(day, month, year)


