import random

rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''   
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = '''    
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
print("welcome to rock paper scissors game , type 0 for rock , type 1 for paper , type 2 for scissors")
user_chose = input("type what you chose:")

if user_chose in ["0", "1", "2"]:
    if user_chose == "0":
        print(f"you chose rock\n{rock}")
    elif user_chose == "1":
        print(f"you chose paper\n{paper}")
    elif user_chose == "2":
        print(f"you chose scissors\n{scissors}")
else:
    print("Invalid choice! Please enter 0, 1, or 2")
    exit()
    
random_number = random.randint(0,2)

print("opponent chooses:")
if random_number == 0:
    print(f"rock\n{rock}")
elif random_number == 1:
    print(f"paper\n{paper}")
elif random_number == 2:
    print(f"scissors\n{scissors}")

if user_chose == str(random_number):
    print("It's a tie!")
elif (user_chose == "0" and random_number == 2):
    print("You win! 🎉")
elif (user_chose == "1" and random_number == 0):
    print("You win! 🎉")
elif (user_chose == "2" and random_number == 1):
    print("You win! 🎉")
else:
    print("You lose! 😢")