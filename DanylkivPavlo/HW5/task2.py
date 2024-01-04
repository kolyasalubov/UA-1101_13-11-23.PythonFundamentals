user_input = int(float(input("Enter the last number: ")))
numbers = [0,1]
sum_of_two_numbers = 0

while sum_of_two_numbers < user_input:
    sum_of_two_numbers = numbers[0] + numbers[1]
    if sum_of_two_numbers < user_input:
        numbers[0] = numbers[1]
        numbers[1] = sum_of_two_numbers
        print(sum_of_two_numbers)