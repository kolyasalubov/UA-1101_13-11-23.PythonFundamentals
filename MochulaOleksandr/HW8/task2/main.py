import class_s
input1 = input("what is the figure? ")
if input1 == "circle":
    input_r =float(input("what is the radius? "))
    print(class_s.sircle_area(input_r))
elif input1 == "rectangle":
    input_w = float(input("what is widh? "))
    input_h = float(input("what is high? "))
    print(class_s.area_rect(input_w,input_h))
elif input1 == "triangle":
    input_w = float(input("what is a? "))
    input_h = float(input("what is h? "))
    print(class_s.area_triangle(input_w,input_h))
else: 
    print("Sorry no are for you today")
