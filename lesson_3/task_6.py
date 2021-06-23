x_1 = int(input("Enter current position on horizontal: "))
y_1 = int(input("Enter current position on vertical: "))
x_2 = int(input("Enter the position for the move: "))
y_2 = int(input("Enter the position for the move: "))

delta_x = abs(x_2 - x_1)
delta_y = abs(y_2 - y_1)

if delta_x == 1 and delta_y == 2 or delta_x == 2 and delta_y == 1:
    print("You move will be done!")
else:
    print("Sorry, you choose the wrong position")
