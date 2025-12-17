word_list = ["calm","bright","strong"]

import random
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)

#what we need to do in step 3:
#1.use while loop let the user guess again

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    #2.update the forloop so that if we guessed a correct letter from the chosen_word it should keep that with we guessing the next correct word and add all that to display variable.

    for letter in (chosen_word):
        if letter == guess:
            display += (letter + " ")
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += (letter + " ")
        else:
            display += "_ "
            
    print(display)
    
    if "_" not in display:
        game_over = True
        print("You win")