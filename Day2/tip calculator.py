print("Welcome to the Tip Calculator!")
x = float(input("What was the total bill? "))
y = float(input("how much tip would you like to give?"))
z = int(input("How many people will split the bill?"))

total = (x + y)/z

rounded_total = round(total, 2)

print(f'Each person should pay: ${rounded_total}')
print("Thank you for using the Tip Calculator!")    