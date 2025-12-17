welcome_message = """
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║    Welcome to the Ultimate Hangman Challenge!                 ║
║                                                                ║
║    🎯 Guess the hidden word letter by letter                  ║
║    💀 You have 6 lives - use them wisely!                    ║
║    🏆 Save the hangman and win the game                      ║
║                                                                ║
║              Good luck and have fun! 🎮                       ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
"""

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

game_over_win = """
🎉 CONGRATULATIONS! 🎉
You saved the hangman!
You are a true word master! 🏆
"""

game_over_lose = """
💀 GAME OVER! 💀
The hangman has been hanged...
Better luck next time! 😔
"""