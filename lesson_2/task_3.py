v = int(input("Enter rider speed: "))
if v > 0:
    abs(v)
if v < 0:
    -abs(v)


t = int(input("Enter time: "))
s = v / t
if s > 100:
    print("You distance is already competed" )
else:
    print("You stopped on a distance " + str(s) + "km")
