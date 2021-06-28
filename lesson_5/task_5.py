side_of_square = int(input("Enter the side of square: "))
def square(side_of_square):
    perimeter = side_of_square * 4
    area = side_of_square ** 2
    diagonal = float(side_of_square * 2 ** 0.5)
    return "Perimeter is ", perimeter, "Area of square is ", area, "Diagonal of square is ", format(diagonal, '.2f')


print(square(side_of_square))