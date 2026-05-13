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

print("welcome to rock paper scissors ,  type 0 for rock , type 1 for paper , type 1 for scissors")
user_chose = input("what your choice ?")

if user_chose in ["0","1","2"]:
    if user_chose == "0":
        print(f"you chose rock",rock)
    elif user_chose == "1":
        print(f"you chose paper",paper)
    elif user_chose == "2":
        print(f"you chose scissor",scissors)
else:
    print("invalid choice , please choose 0, 1, 2")
    exit()

random_number = random.randint(0,2)

print("opponent chooses :")
if random_number == 0:
    print(f"rock",rock)
elif random_number == 1:
    print(f"paper",paper)
else:
    print(f"scissors",scissors)

if user_chose == str(random_number):
    print("its a tie")
if user_chose == "0" and random_number == "2":
    print("you win")
elif user_chose == "1" and random_number == "0":
    print("you win")
elif user_chose == "2" and random_number == "1":
    print("you win")
else:
    print("you loose")