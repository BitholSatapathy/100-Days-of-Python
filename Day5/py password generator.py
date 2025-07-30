import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to PyPassword Generator!")
letters_no = int(input("How Many letters would you like in your password? \n"))
symbols_no = int(input("How Many symbols would you like in your password? \n"))
numbers_no = int(input("How Many numbers would you like in your password? \n"))

password_random = []
for l in range (letters_no):
    l = random.choice(letters)
    password_random.append(l)
for n in range (numbers_no):
    n = random.choice(numbers)
    password_random.append(n)
for s in range (symbols_no):
    s = random.choice(symbols)
    password_random.append(s)

random.shuffle(password_random)

final_pass = ''
for f in password_random:
    final_pass += f
print(f"your password is : {final_pass}")