# **The Hangman Game**
## **Overview**

Hangman is a classic word-guessing game where players try to figure out a hidden word by guessing letters, one at a time. The game is typically played with two participants—one who thinks of a word and the other who tries to guess it. The game can also be played solo or with a computer.

Basic Rules:
Word Selection: One player thinks of a secret word and provides the number of letters in the word, represented by blanks (_ _ _ _ _).

Guessing: The other player (or players) guesses a letter. If the guessed letter is in the word, it replaces the corresponding blank spaces. If it's incorrect, a part of the "hangman" figure is drawn.

Drawing the Hangman: The game usually involves drawing a stick figure of a man being hanged. For each incorrect guess, a body part (head, torso, arms, legs) is added, and after a set number of incorrect guesses (often 6 or 7), the game ends in a loss for the guesser.

Winning and Losing:

Win: The game is won if the player guesses all the letters in the word before the hangman figure is fully drawn.
Loss: The game is lost if the guesser runs out of chances (i.e., if the hangman is fully drawn and the word remains incomplete).

The game is Python-based and uses a game Board class, functions, for loops, while loops and if/elif/else statements to achieve the desired outcome.

It features space-based ASCII art, and contains various references to hangman characters.


Click [here](https://battleships-1977.herokuapp.com/) to see the final deployment of the game

![Am I Responsive Screenshot](assets/images/bs1977-am-i-responsive.png)
![Am I Responsive Screenshot](assets/images/bs1977-am-i-responsive-name.png)

​
## Table of contents:
1. [**Site Overview**](#site-overview)
1. [**Planning stage**](#planning-stage)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
    * [***Site Aims***](#site-aims)
    * [***Lucid Chart***](#lucid-chart)
    * [***Color Scheme***](#color-scheme)
    * [***Typography***](#typography)
1. [**Current Features**](#current-features)
    * [***Data Module***](#data-module)
    * [***Start Screen***](#start-screen)
    * [***Pre-Game***](#pre-game)
    * [***Gameplay***](#gameplay)
    * [***Game Over***](#game-over)
1. [**Future-Enhancements**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
1. [**Deployment**](#deployment)
1. [**Tech**](#tech)
1. [**Credits**](#credits)
    * [**Content**](#content)
    * [**Media**](#media)
    * [**Honourable mentions**](#honorable-mentions)
​
## **Planning Stage**

<br>

#### **Target Audiences:**
* People who likes word games.
* People who want to improve their vocabulary.
* People who to play hangman game online.
* People who wants to get rid of boredom and entertain themselves.
* Aspiring coders who want to learn python coding through this game.

​
#### **User Stories:**
* As a user, I want to understand the premise of the game.
* As a user, I want to quickly learn and understand the rules of the game and its instructions.
* As a user, I want a clean and simple user interface (UI).
* As a user, I want the game to run smoothly and bug-free.
* As a user, I want to be able to choose whether or not to play again when the game ends.
* As a user, I want to be able to win against the computer.

​
#### **Site Aims:**
* To offer the user a smooth and bug free version of a classic game with a slightly different twist.
* To provide a clean and simple interface for the user with no need to reference external sources.
* To provide clear instructions and a win condition.
* To provide an enjoyable user experience of playing battleships.
* To provide an interesting and entertaining Star Wars-based version of the game.

<br>

#### **Lucid Chart:**

To help with the planning stages​​ of this project, I used [LucidChart](https://www.lucidchart.com)
This proved to be very useful tool when it came to visualising the various processes involved in recreating a Battleships style game. Whilst the concept is quite simple, the logic involved proved slightly more difficult.

This is the flow chart which assisted the development of the game:


![Lucid Chart](assets/images/BS1977chart.png)


<br>​

#### **Colour Scheme:**
​

* Not in the scope of this project, however I used cyan text for the start screen to evoke a connection with the Star Wars theme. I then used yellow for the subsequent text for the same reason.

​
#### **Typography**
​
* Not in the scope of this project.

​<br>


## **Features**

#### **Data Model**

* The game uses a Board class. It is used to create instances of the player and CPU and guess boards. Only the player and player_guess boards are printed to the terminal through the display_boards method. The class stores the board size, board owner and shield strength. There are methods to input ship coordinates, populate the board, logic for CPU guesses. There are also methods to check and validate user input as well as prevent any ships overlapping.
​
#### **Start Screen** 

![Screenshot of start screen](assets/images/bs77-start-screen.png)

* The start screen features the iconic Star Wars introduction: "A long time ago, in a galaxy far, far away..." Beneath that is some very basic ASCII art depicting stars. There a short time delay using the time.sleep() function to allow the user to process the screen. They are then prompted to press enter.

![Screenshot of player name input](assets/images/bs77-name-input.png)

* The os.sys("clear") function is used to clear the screen and the user is then presented with ASCII text intended to emulate the Star Wars movie font. They are prompted to enter their name using the get_name function which stores the username in a variable for use in the game. They are then presented with a short welcome message and short backstory explaining enemy ships have entered the area. The user can press enter to proceed to the next screen.

#### **Pre-Game**

![Screenshot of ship types](assets/images/bs77-ship-types.png)

* The same os function is used to clear the terminal once again. The ship_type method is called so the user is presented with the four different types of ships at their disposal, along with the size of each. The ships are displayed sequentially in descending size order, on a slight delay using the time library.

![Screenshot of legend](assets/images/bs77-legend.png)

* Upon pressing enter, the game_rules function is called to display the symbols which will be used on the game boards. Once the user has processed the information, they are prompted to press enter again.

* The following text explains the win condition which states that ten hits will be enough to win the game. There is a final prompt to press enter.

![Screenshot of win condition](assets/images/bs77-win-condition.png)


![Screenshot of player board and prompt to enter ship direction](assets/images/bs77-choose-direction.png)

* os is used to clear the screen once again and the player board is printed to the terminal. It displays the player name and the shield strength at the starting value of 10. The place_ships method is called so the player is asked to place each ship by choosing whether it will be aligned horizontally or vertically. Any input other than 'h'/'H' or 'v'/'V' will be invalid and the user will be asked to try again. The process will loop until all ships have been assigned coordinates.

#### **Gameplay**

![Screenshot of player hitting ship](assets/images/bs77-hit-ship.png)

* The populate_boards method adds the user and CPU ships to their respective boards. The user cannot see where the CPU ships are. The game is set up so the user goes first. The player_attack method takes input from the user to guess enemy ship coordinates on the x and y axes. The first CPU guess is a random choice on the board. Upon a successful hit, the CPU will attempt to guess on an adjacent tile. Click the highlighted text to see screenshots of the player entering invalid [row](assets/images/bs77-invalid-row.png) or [column](assets/images/bs77-invalid-column.png) coordinates. The user cannot enter the same coordinates twice. Most of the game logic is in the play_game function which handles updating and appending the relevant boards. It also handles decrementing the shield counter. The game will continue to run until either the player or CPU shield counters reaches zero.


#### **Game Over** 
![Screenshot of play again option](assets/images/bs77-play-again.png)
![Screenshot of choosing not to play again](assets/images/bs77-play-again-no.png)

* Upon winning or losing the game, an ASCII-based message is displayed before the user is given the option of playing a new game. If this option is chosen, the game resets and starts from the beginning. If the user chooses to quit, they are presented with s short message in keeping with the theme of the game.

<br>

​
## **Future-Enhancements**
​
There can be many areas where the game can be enhanced. But due to project tight deadline and due to the challenges the scope was limited
Further enhancements can be as follows.
​
* Adding a timer while guessing a letter.
* Introduce different categories. (Currently only flower names/words are guessed.)
* Option to randlomly quitting the game in between.
* An hint system to get a user about the word

​
## **Testing Phase**
​
**Functionality**

* Implementation 🏭: Check whether user is able to play game from start to finish
* Test 🧪: Played the game locally many times.
* Result 🏆: The game worked as expected
* Verdict ✅: PASS

<br>

* Implementation 🏭: Check whether tests are passed for valid character.
* Test 🧪: Test the game with all the possible valid characters.
* Result 🏆: Game worked as per expected result.
* Verdict ✅: PASS.

<br>

* Implementation 🏭: Check whether game worked as expected for invalid characters.
* Test 🧪: I played the game on a local terminal with invalid character. Validation was not present.
* Result 🏆: Tests didnt work as expected results
* Verdict ✅: FAIL

<br>

* Implementation 🏭: Check 
* Test 🧪: I played the 
* Result 🏆: The 
* Verdict ✅: Test passed.
<br>
​

**Validators**

* The PEP8 Online Validator was down when creating this project, however I added a PEP8 validator to my workspace by running the command: "pip3 install pycodestyle". The results can be found [here](assets/images/bs1977-pycodestyle.png)

* The validator flags a number of minor warnings, all of which are related to the use of the ASCII art used in the start screen, win screen and lose screen functions. In my final mentor session, I was informed these are inconsequential and can essentially be ignored as they do not affect the program itself.

​
​
## **Bugs**
​
Some of the bugs were identified during testing. They are listed below.

* 🐞 - Initially the ascii charcater for hangmans head was towards left and were not in align with hands and legs. 
* ⚒️ - Didnt checkj properly the alingmments of the ascii characters which makes the hangman.
* ✅ - Added a space towards left of the ascii character which makes the head.

<br>

* 🐞 - When the duplicate characters are entered, there was no validation.
* ⚒️ - Since validating duplicate entries of the character was missing.
* ✅ - Added a new method to validate the duplicate entries.

​<br>

* 🐞 - User could enter special characters, digits or anything 
* ⚒️ - The implementation for valid characters was not in the place.
* ✅ - Implemented the valid character checking, if invalid character is enetred error is thrown to the user.

<br>

* 🐞 - Menu list was wrongly ordered
* ⚒️ - 
* ✅ - I

<br>


<br>

## **Unfixed Bugs**

* All the bugs which have been identified have been fixed and there are no unknow defects.

## **Deployment**

## ***Final Deployment to Heroku:***  
  
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
1. **Log in to Heroku** or create an account if required.
1. **click** the button labeled **New** from the dashboard in the top right corner, just below the header.
1. From the drop-down menu **select "Create new app"**.
1. **Enter a unique app name**. I chose battleships-1977 for this project, for reasons stated above.
1. Once the web portal shows the green tick to confirm the name is original **select the relevant region.** In my case, I chose Europe as I am in the UK.
1.  When happy with your choice of name and that the correct region is selected, **click** on the **"Create app" button**.
1. This will bring you to the project "Deploy" tab. From here, navigate to the **settings tab** and scroll down to the **"Config Vars" section**. 
1. **Click** the button labelled **"Reveal Config Vars"** and **enter** the **"key" as port**, the **"value" as 8000** and **click** the **"add"** button.
1. Scroll down to the **buildpacks section of the settings page** and click the button labeled **" add buildpack," select "Python," and click "Save Changes"**.
1. **Repeat step 11 but** this time **add "node.js" instead of python**. 
   * ***IMPORTANT*** The buildpacks must be in the correct order. If node.js is listed first under this section, you can click on python and drag it upwards to change it to the first buildpack in the list.
1. Scroll back to the top of the settings page, and **navigate to the "Deploy" tab.**
1. From the deploy tab **select Github as the deployment method**.
1. **Confirm** you want to **connect to GitHub**.
1. **Search** for the **repository name** and **click** the **connect** button next to the intended repository.
1. From the bottom of the deploy page **select your preferred deployment type** by follow one of the below steps:  
   * Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.  
   * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment. 

The final deployment can be viewed [here](https://)
​
## **Tech**
​
Have used the following technologies to build the Hangman project:
​
- Python

## **Libraries**

The following library was used:

* Random - Used to generate random choice of words to be selected to play the game.


## **Software**

The following software was used:

- VS Code : To create code and pushing it to the github
- Git (Gitpod and Github) : Used for version controlling.
- Heroku is used for deploying the project.
- Lucid Chart is used to create the flow chart of the project.

### **Media:**

* Not in scope for the current project.
​
<br>


## **Credits**

* A youtube tutorial which helped me to understand and build logic for hangman game was really great.
[Bro Code](https://www.youtube.com/watch?v=ag8NtD1e0Kc). Based on this tutorial, I have used his all his logic to build the game. then later it is enhanced with metors guidance and suggestions.

* Another youtube tutorial related to hangman game was very helpful initially to understand on how to play the game. The course is by [Triple S Games](https://www.youtube.com/watch?v=cGOeiQfjYPk) 

* Course material in Scrimba was also very helpful for me to understand python in a short time. [Scrimba-Python](https://scrimba.com/learn-python-c03/~00)

* I have also used Chat-GPT to understand the Hangman game and its features. [Chat-GPT](https://chatgpt.com/)

### **Honourable mentions**
* Many thanks to my mentor, Richard Wells, who is always very helping and guiding me whenever I needed. He is very dedicated and kind person who gave me valuable feedback and ideas to enhance the project. He is true inspirational and motivational for me in my current journey.
* Many thanks to code institute student support, they always helped with python errors and tutored me whenever required.
* Many thanks to code institute community in slack. 
* Many thanks to family and friends who are always an inspiration to me.
