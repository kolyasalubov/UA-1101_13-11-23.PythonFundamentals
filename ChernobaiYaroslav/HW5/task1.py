transformationList = list(range(int(input("Enter the quantity of numbers you wish to transform from int to float: "))))

print(f"Your list before the tranformation of elements to float: {transformationList}")

for i in transformationList:
    transformationList[i] = float(transformationList[i])
else:
    print(f"Your list after the tranformation of elements to float: {transformationList}")