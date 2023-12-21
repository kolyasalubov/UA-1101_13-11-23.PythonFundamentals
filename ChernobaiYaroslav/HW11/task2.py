def numsAsDays(num: int):
    days = {1: "Monday", 
            2: "Tuesday", 
            3: "Wednesday", 
            4: "Thursday", 
            5: "Friday",
            6: "Saturday",
            7: "Sunday"}
    if num not in range(1,8):
        raise Exception("There's only 7 days in the week.")
    return days[num]

try:
    print(numsAsDays(int(input("Enter a number of the day of the week: "))))
except ValueError as e:
    print(f"Error! {e}")
