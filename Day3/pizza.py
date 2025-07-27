print("Welcome to python pizza deliveries!")
pizza_type = input("what size of pizza you like to take:  \n1.Large(L)\n2.Medium(M)\n3.Small(S)\n Write down the size(L/M/S): ")
if pizza_type not in ["M","m","L","l","S","s"]:
    print("you have entered wrong inputs")
else:
    pepperoni_add = input("do you want pepperoni on your pizza: \n1.yes(y)\n2.no(n)\n (y/n): ")
    cheese_add = input("do you want extra cheese on your pizza: \n1.yes(y)\n2.no(n)\n (y/n): ")
    delivery_or_not = input("do you want it delivered or not: \n1.yes(y)\n2.no(n)\n (y/n): ")
    if pizza_type == "L":
        price = 80
        if pepperoni_add == "y":
            price += 10
        if cheese_add == "y":
            price += 5
    elif pizza_type == "M":
        price = 60
        if pepperoni_add == "y":
            price += 8
        if cheese_add == "y":
            price += 5
    elif pizza_type == "S":
        price = 40
        if pepperoni_add == "y":
            price += 5
        if cheese_add == "y":
            price += 5
    print(f"your size of pizza is: {pizza_type}\nwith pepperoni: {pepperoni_add}\nwith extra cheese: {cheese_add}\ntotal cost is: {price}$")

    if delivery_or_not == "y":
        final_price = price + 30
        delivery_address = input("add delivery address:")
        print(f"your delivery address is {delivery_address}\nIt will cost you extra 30$ delivery charge so your final bill is:{final_price} $")
    else:
        final_price = price
        print(f"your final bill is{final_price} $")

    print("have a great day")