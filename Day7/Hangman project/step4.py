word_list = ["calm","bright","strong"]
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

import random

#what we need to do in step 4:
#1.create a variable live to keep the track of lives and set live = 6

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    

    for letter in (chosen_word):
        if letter == guess:
            display += (letter + " ")
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += (letter + " ")
        else:
            display += "_ "
            
    print(display)
    
#2.if guess is not a letter in the chosen word , then reduce lives by 1. if lives goes down to 0 , then the game should stop and print you loose.
    if guess not in (chosen_word):
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose")

 
    if "_" not in display:
        game_over = True
        print("You win")

#3. print ascii art from the stages that corresponds to the number of lives u have.
    print(stages[lives])