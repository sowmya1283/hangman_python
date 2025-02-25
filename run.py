import random
from words import WORDS

"""
Dictionary of Key and tuple values, key to describe no of incorrect guesses,
tuple to store ascii art character to hangman
"""
hangmanart = {
    0: (" ",
        " ",
        " "),
    1: (" o",
        " ",
        " "),
    2: (" o",
        "|",
        " "),
    3: (" o",
        "/|",
        ""),
    4: (" o",
        "/|\\",
        ""),
    5: (" o",
        "/|\\",
        "/"),
    6: (" o",
        "/|\\",
        "/ \\")
}


def display_hangman(trials):
    """
    Function to display the hangman
    """
    print("********")
    for line in hangmanart[trials]:
        print(line)
    print("********")


def display_hint(hint):
    """
    Function to display the hint
    """
    print(" ".join(hint))


def display_answer(answer):
    """
    Function to display the answer
    """
    print(" ".join(answer))


def menu():
    """
    Function to display the menu
    """
    print("********")
    print("HANGMAN")
    print("********")
    print("Menu")
    print("1. New Game")
    print("2. Instructions")
    print("3. Exit")
    can_continue = False
    while not can_continue:
        choice = input("Enter your choice: ")
        if choice == "1":
            can_continue = True
            play_game()
        elif choice == "2":
            can_continue = True
            display_instructions()
        elif choice == "3":
            can_continue = True
            print("Thank you, now you are exited the game.")
            exit()
        else:
            print("Invalid choice. Please try again")


def play_game():
    """
    Function to play the game
    Randomly select a word from the list and start the game
    Then check the guessed letter with the answer
    and display the hangman and hint
    """
    answer = random.choice(WORDS)
    hint = ["_"] * len(answer)
    trials = 0

    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(trials)
        display_hint(hint)
        guess = input("enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input, please enter a single letter")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter {guess}")
            continue

        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            trials += 1

        if "_" not in hint:
            display_hangman(trials)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif trials >= len(hangmanart) - 1:
            display_hangman(trials)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False
            

def display_instructions():
    """
    Function to display the instructions of the game
    """
    print("Instructions to play the game")
    print("1. The computer will randomly select a word from the list")
    print("2. You have to guess the word by entering a letter")
    print("3. You have 6 chances to guess the word")
    print("4. If you guess the word before 6 chances, you win")
    print("5. If you don't guess the word before 6 chances, you lose")
    input("Please enter to go back to the menu")
    menu()


def main():
    """
    Main function calling the menu to start the game
    """
    menu()


if __name__ == "__main__":
    main()