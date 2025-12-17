import random

#what we need to do in step 5:
#1.update the word list  to use the "word_list" from hangman_words.py
from hangman_words import word_list
from hangman_arts import welcome_message
from hangman_arts import stages
from hangman_arts import game_over_win
from hangman_arts import game_over_lose

lives = 6

#2.import the logos from hangman_arts.py and print it at the start of the game

print(welcome_message)

chosen_word = random.choice(word_list)
#print(chosen_word) #TODO: Remove this line for final version

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
#3.update the code below to tell the user how many lives he has left

    guess = input(f"You have {lives} lives left. Guess a letter: ").lower()
    
#4.if the user has entered a letter which he has already guessed , let them know and dont deduct life for this .
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue
    else:
        guessed_letters.append(guess)
        
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

#5.if the letter not in chosen_word , print the letter and let them know that the letter not in the word.

    if guess not in (chosen_word):
        print(f"Sorry, '{guess}' is not in the word.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(game_over_lose)

    if "_" not in display:
        game_over = True
        print(game_over_win)
    
    print(stages[lives])

#6.when you saying u win u loose decorate it little bit