import json
import random

def load_words_with_hints(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [(entry['word'], entry['hint']) for entry in data]

def word_guesser_game():
    while True:
        words_with_hints = load_words_with_hints('words_with_hints.json')
        word, hint = random.choice(words_with_hints)
        guessed_word = ["_"] * len(word)
        guessed_letters = set()
        attempts_left = 6

        print("=================================")
        title = "hangman".upper()
        print(title.center(30,"="))
        print("You have 6 attempts to guess the word. Goodluck!")
        print("=================================")
        print(f"Hint: {hint}")
        print(".................................")
        print(" ".join(guessed_word))

        while attempts_left > 0:
            guess = input("Guess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please guess a single letter.")
                continue
            
            if guess in guessed_letters:
                print("You have already guessed that letter.")
                print(".................................")
                continue
            
            guessed_letters.add(guess)
            
            if guess in word:
                for idx, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[idx] = guess
                print("Good guess!")
                print(".................................")
            else:
                attempts_left -= 1
                print(f"Wrong guess. You have {attempts_left} attempts left.")
                print(".................................")
            
            print(" ".join(guessed_word))
            
            if "_" not in guessed_word:
                print("Congratulations! You guessed the word.\n")
                break
        else:
            print(f"Sorry, you've run out of attempts. The word was '{word}'.")
            print(".................................")

        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ("yes", "no"):
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        if play_again == "no":
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    word_guesser_game()
