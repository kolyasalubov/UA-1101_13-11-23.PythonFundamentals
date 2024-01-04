################### Task1 ##################################
# def age_analyser():
#     age=input("What's your age? ")
#     try:
#         if age.isdigit() and int(age)>0:
#             if int(age)%2==0:
#                 print("The number is even.")
#             else:
#                 print("The number is odd.")
#         else:
#             raise ValueError
#     except ValueError:
#         print("You cant have negative or non-digit age.")
#
# age_analyser()

################### Task2 ##################################

def day_of_week():
    week={
        "1":"Sunday",
          "2":"Monday",
          "3":"Tuesday",
          "4":"Wednesday",
          "5":"Thursday",
          "6":"Friday",
          "7":"Saturday"
    }
    day_number=input("Enter number of the day of the week:")
    try:
        if day_number.isdigit() and int(day_number)<=7:
            day_week=week[day_number]
            print(day_week)
        else:
            raise ValueError
    except ValueError:
        print("You typed something wrong.")

day_of_week()