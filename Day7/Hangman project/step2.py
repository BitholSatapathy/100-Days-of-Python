word_list = ["Calm","Bright","Strong"]

import random
chosen_word = random.choice(word_list)
print(chosen_word)

#what we need to do in step 2:
#1.create an placeholder which should have same number of _ as of the number of letters in chosen_word .

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)


guess = input("Guess a letter: ").lower()

#2.create a display which puts the guess letters in the right place . 

display = ""


for letter in (chosen_word):
    if letter == guess:
        display += (letter + " ")
    else:
        display += "_ "

print(display)
