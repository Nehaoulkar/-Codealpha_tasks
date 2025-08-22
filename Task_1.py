import random

print("Welcome to Hangman game!")
word_list = ["apple", "banana", "lemon", "mango", "orange"]

word_to_guess = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Guess the word, one letter at a time.")

while incorrect_guesses < max_incorrect:

    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word.strip())

    if all(letter in guessed_letters for letter in word_to_guess):
        print("\n Congratulations! You guessed the word:", word_to_guess)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print(f" Wrong guess! You have {max_incorrect - incorrect_guesses} tries left.")

if incorrect_guesses == max_incorrect:
    print("\n Game Over! The word was:", word_to_guess)
