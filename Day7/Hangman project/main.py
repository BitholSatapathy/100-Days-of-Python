import random
from hangman_words import word_list
from hangman_arts import welcome_message, stages, game_over_win, game_over_lose

lives = 6

print(welcome_message)

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    guess = input(f"You have {lives} lives left. Guess a letter: ").lower()
    
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