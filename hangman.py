import random

# List of predefined words
words = ["python", "computer", "college", "student", "project"]

# Randomly select a word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses allowed
attempts = 6

print("=" * 40)
print("        WELCOME TO HANGMAN")
print("=" * 40)
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", " ".join(guessed_letters))
    print("Remaining Attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        attempts -= 1
        print("Wrong Guess!")

# Final Result
print("\n" + "=" * 40)

if "_" not in guessed_word:
    print("🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("Game Over!")
    print("The correct word was:", word)

print("=" * 40)