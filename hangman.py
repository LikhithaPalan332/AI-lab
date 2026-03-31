import random

stages = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''', r'''
   +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
   +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

words_list = [
    "python", "java", "computer", "program", "hangman",
    "keyboard", "internet", "variable", "function", "developer"
]

def get_word():
    return random.choice(words_list)

def hangman():
    chosen_word = get_word()
    display = ["_"] * len(chosen_word)
    guessed_letters = set()

    end_of_loop = False
    lives = 6

    print("\n-------------Welcome to Hangman-------------\n")
    print("Guess the word:- ", ' '.join(display))
    print(f"Lives: {lives}")

    while not end_of_loop:
        guess = input("Guess a Letter: ").lower()

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        else:
            guessed_letters.add(guess)

        if guess not in chosen_word:
            lives -= 1

        for index, char in enumerate(chosen_word):
            if char == guess:
                display[index] = guess

        print(' '.join(display))
        print(f"Lives: {lives}")
        print(stages[6 - lives])

        if "_" not in display:
            print("You Win!")
            end_of_loop = True

        if lives == 0:
            print("You Lose")
            print(f"The word was: {chosen_word}")
            end_of_loop = True

while True:
    ask = input("Do you want to play Hangman? (y/n): ").lower()
    if ask in ('y', 'yes'):
        hangman()
    elif ask in ('n', 'no'):
        print("Program Exit Successful")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
