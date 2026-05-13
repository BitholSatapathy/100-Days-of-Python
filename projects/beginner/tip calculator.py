print("Welcome to tip calculator")
total_bill = float(input("whats the total bill ?"))
added_tip = float(input("want to add tip ?"))
split = int(input("how many person u want to split the bill ?"))

z = (total_bill+added_tip)/split
final_total = round(z,2)

print(f"per person the bill is: {final_total}")
