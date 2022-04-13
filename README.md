# H's Hangman

H's Hangman is a Python terminal game, which runs in the Code Institue mock terminal on Heroku.

Users pick a catergory and a word from that catergory will be randomly generated. The user has to try to guess the word before with allocated guesses.

## How to play 
- H's Hangman is based on the classic paper and pencil guessing game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))
- In this version of hangman game, the player enters the game with a choice of catergories. The player has to choose a listed catergory in order to begin the game.
- Once a catergory has been chosen the computer will think of a random word in relation to the chosen catergory. For exmaple if the user chooses capital cities the word would be a city somewher in the world.
- The player gets to know how many letters the word contains by the amount of underscores and the default diagram of hangman is printed.
- The player inputs a-z characters in a bid to guess the word. Everytime a correct character is entered the computer will tell them its correct and place the letter on the correct underscore, the hangman diagram will not change.
- Everytime the player guesses incorrect the computer will tell them its incorrect, add the letter to the incorrect list and the diagram of hangman will gain an element/body part.
- The player has 6 guesses all together to guess all the letters in the word before the completed diagram would mean the games been lost.
- A simple yes(y) or no(n) at the end will let the player play again at end the game.

## Features
# Welcome message/Landing page

# Catergory choice 

# After catergory selection

# Hangman game

# Play again function



## Testing

For all testing documentation, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The site was deployed to Heroku. The steps to deploy are as follows: 
  - From the Heroku dashboard, click the “Create new app” button.
  - Once the app has been created, click on "Settings" tab.
  - The next step is to add a couple of buildpacks to the application. Python first and then Node.js in the order as shown below;

  ![Buildpacks](documentation/buildpacks.png)
  - From there head to the "Deploy" tab, select the deployment method to GitHub and connect your GitHub account.
  - Using the search button, such for the repository name (h_hangman in my case) and click "Connect" to link up.
  - Scroll down and click "Deploy Branch" in the manual section. The page will be deployed and ready to view in a few seconds.

### Local Deployment

In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/henrysevern/h_hangman.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/henrysevern/h_hangman)

  ## Credits 

  - Hangman ASCII art was taken from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
  - ASCII art was taken from https://www.asciiart.eu/
  - Clear function, restart function, delay function with assistance from https://stackoverflow.com/
  - Random words list taken from https://futureofworking.com/40-hardest-words-to-guess-in-hangman/
  - Animals words list taken from https://gist.github.com/atduskgreg/3cf8ef48cb0d29cf151bedad81553a54

