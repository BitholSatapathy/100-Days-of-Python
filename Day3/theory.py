# #control flow , if else statements
# water_level = int(input("what is your water level?"))
# if water_level >80:
#     print("drain the water")
# else :
#     print("water level is fine")


# #ticket system for roller coaster
# height = float(input("what is your height in cm?"))
# if height >= 120:
#     print("you can move forward")
# elif height == 119:
#     print("wish you have taken some d..gs")
# else :
#     print("you are not allowed for this ride")

# #modulo operator % = remainder
# a = int(input("enter a number"))
# b = int(input("enter another number"))
# c = a % b
# print(f"the remainder is {c}")

# #check iof number is odd or even
# a = int(input("enter a number: "))
# b = a % 2
# if b == 0:
#     print(f"{a} is a even number")
# else:
#     print(f"{a} is a odd number")

# #nested statements and elif statements
# height = float(input("what is your height (in cm): "))
# if height >= 120:
#     print("your can enjoy the ride")
#     age = int(input("what is your age:"))
#     if age >= 18:
#         print("pay 200$")
#     elif age <= 12:
#         print("pay 100$")
#     else:
#         print("pay 150$")
# else:
#     print("you can't enter the ride")

# #multiple if statements in succession
# height = float(input("what is your height (in cm): "))
# if height >= 120:
#     print("your can enjoy the ride")
#     age = int(input("what is your age:"))
#     if age >= 18:
#         payment = 200
#     elif age <= 12:
#         payment = 100
#     else:
#         payment = 150
#     photo = input("Do you need a photo? (y/n) :")
#     if photo == "y":
#         print(f"you have to pay {payment + 30}$")
#     if photo == "n":
#         print(f"you have to pay {payment + 30}$")
# else:
#     print("you can't enter the ride")

#logical operators (and,or,not)
height = float(input("what is your height (in cm): "))
if height >= 120:
    print("your can enjoy the ride")
    age = int(input("what is your age:"))
    if age >= 18:
        payment = 200
    elif age <= 12:
        payment = 100
    elif age>=45 and age<=55:
        print("every thing is on us take a ride!")
    else:
        payment = 150
    photo = input("Do you need a photo? (y/n) :")
    if photo == "y":
        print(f"you have to pay {payment + 30}$")
    if photo == "n":
        print(f"you have to pay {payment + 30}$")
else:
    print("you can't enter the ride")