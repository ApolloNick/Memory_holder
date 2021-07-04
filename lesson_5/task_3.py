def figure_area(choice="triangle"):
    choice = input("Choose your type of figure: ")
    area = 0
    if choice == "triangle":
        base = float(input("Enter the length of base line: "))
        height = float(input("Enter the height length to the base line: "))
        area = 0.5 * base * height
    if choice == "square":
        any_line = float(input("Enter any line of a square: "))
        area = any_line ** 2
    return area


print(figure_area())