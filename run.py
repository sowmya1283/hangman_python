# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
words =("apple", "orange", "banana", "coconut", "pineapple")

#dictionary of Key and tuple values, key to describe no of incorrect guesses, tubple to store ascii art character to hangman
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
    print("********")
    for line in hangmanart[trials]:
        print(line)
    print("********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
   
    answer = random.choice(words)  #randomly select a word from the list
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

        if guess in guessed_letters:
            print(f"You already guessed the letter {guess}")
            continue

        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] =guess
        else:
            trials += 1

        if "_" not in hint:
            display_hangman(trials)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif trials >= len(hangmanart) -1:
            display_hangman(trials)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False
 
if __name__ == "__main__":
    main()
