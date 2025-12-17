word_list = ["Calm","Bright","Strong"]

#what we need to do in step 1:
#1.randomly choose a word from the word_list and assign it to a variable chosen_word and print it.

import random
chosen_word = random.choice(word_list)
print(chosen_word)

#2.ask user to guess a letter and assign it to a variable guess and make guess lowercase.

guess = input("Guess a letter: ").lower()
print(guess)

#3.check if the letter user guessed (guess) is one of thee letter in the chosen_word , print "Right" if it is , or wrong if it is not .

for letter in (chosen_word):
    if letter == guess:
        print("Right")
    else:
        print("Wrong")