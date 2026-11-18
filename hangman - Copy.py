
import random

WORDS = ["python", "developer", "internship", "algorithm", "variable"]
MAX_WRONG = 6

HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
]


def display_state(word, guessed_letters, wrong_guesses):
    """Print the hangman drawing, the masked word and guessed letters."""
    print(HANGMAN_STAGES[len(wrong_guesses)])
    masked = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\nWord:  {masked}")
    print(f"Wrong guesses ({len(wrong_guesses)}/{MAX_WRONG}): {', '.join(wrong_guesses) or 'none'}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'none'}\n")


def get_guess(guessed_letters):
    """Ask the player for a valid, not-yet-guessed single letter."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_round():
    """Play one full game of Hangman. Returns True if the player won."""
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = []

    print("\nI'm thinking of a word. You can miss up to", MAX_WRONG, "times.")

    while len(wrong_guesses) < MAX_WRONG:
        display_state(word, guessed_letters, wrong_guesses)

        if all(letter in guessed_letters for letter in word):
            print(f"🎉 Congratulations! You guessed the word: {word.upper()}")
            return True

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses.append(guess)
            print(f"❌ Sorry, '{guess}' is not in the word.")

    display_state(word, guessed_letters, wrong_guesses)
    print(f"💀 Game over! The word was: {word.upper()}")
    return False


def main():
    print("=" * 40)
    print("        WELCOME TO HANGMAN")
    print("=" * 40)

    wins = losses = 0
    while True:
        if play_round():
            wins += 1
        else:
            losses += 1
        print(f"\nScore -> Wins: {wins} | Losses: {losses}")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGame exited. Goodbye!")
