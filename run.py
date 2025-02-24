# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import WORDS

"""
Dictionary of Key and tuple values, key to describe no of incorrect guesses, tuple to store ascii art character to hangman
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
            can_continue == True
            print("Thank you for playing Hangman")
            exit()
        else:
            print("Invalid choice. Please try again")


def play_game(): 
    answer = random.choice(WORDS)  #randomly select a word from the list
    hint = ["_"] * len(answer)  #create a hint list with the same length as the answer

    trials = 0    #initialize the number of trials (Wrong answers) to 0
   
    guessed_letters = set()    #initialize the set of guessed letters in a set
    is_running = True #When initially run this program, set the value to true, once we finish the game turn this to a false


    while is_running:
        display_hangman(trials) #call the function to display the hangman
        display_hint(hint) #call the function to display the hint
        #display_answer(answer)  #call the function to display the answer (for testing purposes)
        guess = input("enter a letter: ").lower() #ask the user to enter a letter and convert it to lowercase

        if len(guess) != 1 or not guess.isalpha(): #check if the user entered more than one letter
            print("Invalid input")
            continue

        if guess in guessed_letters: #check if the guess is in the set of guessed letters
            print(f"You already guessed the letter {guess}")
            continue

        guessed_letters.add(guess) #add the guess to the set of guessed letters
        
        if guess in answer: #check if the guess is in the answer
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] =guess
        else:
            trials += 1

        if "_" not in hint: #check if the hint list has no more underscores
            display_hangman(trials)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif trials >= len(hangmanart) -1: #check if the number of trials is greater than or equal to the length of the hangman art
            display_hangman(trials)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


def display_instructions():
    print("Instructions to play the game")
    print("1. The computer will randomly select a word from the list")
    print("2. You have to guess the word by entering a letter")
    print("3. You have 6 chances to guess the word")
    print("4. If you guess the word before 6 chances, you win")
    print("5. If you don't guess the word before 6 chances, you lose")
    input("Please enter to go back to the menu")
    menu()    


def main():
    menu() #main function
   
    
if __name__ == "__main__":
    main()
