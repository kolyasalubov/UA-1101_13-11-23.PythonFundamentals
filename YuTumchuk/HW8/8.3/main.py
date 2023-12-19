import calc as ca

initial_reguest = input("Write, which figure's area you want to calculate (rectangle, triangle or circle)?")
if initial_reguest == "rectangle":
    ca.rectangle_area()
elif initial_reguest == "triangle":
    ca.triangle_area()
elif initial_reguest == "circle":
    ca.circle_area()
else:
    print("You typed something else, please re-run program and type exact name of the figure")