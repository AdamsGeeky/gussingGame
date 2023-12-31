# Import the 'random' library for generating random numbers
import random
import time
# Import the 'pygame' library for game development and multimedia applications
import pygame
from pygame.locals import *  # Import QUIT and other constants

# Initialize the pygame library
pygame.init()

def display_winners_award():
    # Set up the window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Winner's Award")
    
    # Load the award image
    award_image = pygame.image.load("award.png")  # Replace "winner_award.png" with the actual image file
    
    # Get the size of the image
    image_width, image_height = award_image.get_size()
    # Calculate the position to center the image
    x = (screen_width - image_width) // 2
    y = (screen_height - image_height) // 2

    # Main loop for displaying the image
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
     # Clear the screen
        screen.fill((255, 255, 255))  # Fill with white background color
        
        # Display the award image centered on the screen
        screen.blit(award_image, (x, y))
        
        pygame.display.update()
    
    pygame.quit()


# Load sound files using pygame's mixer module
# 'pygame.mixer.Sound' is used to load and manage sound effects and music in the game.

# Load the 'correct' sound effect
correct_sound = pygame.mixer.Sound("./sounds/correct.wav")

# Load the 'incorrect' sound effect
incorrect_sound = pygame.mixer.Sound("./sounds/incorrect.wav")

# Load the background music
background_music = pygame.mixer.Sound("./sounds/background_music.wav")

# Function to play the correct guess sound
# This function plays the 'correct' sound effect when the player guesses the correct number.

def play_correct_sound():
    correct_sound.play()

# Function to play the incorrect guess sound
# This function plays the 'incorrect' sound effect when the player's guess is incorrect.

def play_incorrect_sound():
    incorrect_sound.play()

# ANSI escape codes for color
# These ANSI escape codes are used to add colored text to the console output.
# They are used for providing colorful feedback to the player during the game.

RED = '\033[91m'  # Red color
GREEN = '\033[92m'  # Green color
YELLOW = '\033[93m'  # Yellow color
END_COLOR = '\033[0m'  # Reset color

# Function to start the game
# This function handles the initial setup of the game, including level selection and game start.

def start_game():
    print("👋 Welcome to the Number Guessing Game!")

    while True:
        try:
            # Prompt the player to choose a game level (1, 2, or 3)
            level = int(input("Choose a level (1, 2, or 3): "))
            
            # Check if the chosen level is valid (1, 2, or 3)
            if level not in [1, 2, 3]:
                raise ValueError(f"{RED}❌ Invalid level. Please choose a level between 1 and 3.{END_COLOR}")
            break
        except ValueError as e:
            print(e)

    # Start the number guessing game with the chosen level
    guess_the_number(level)
"""
Function to play the number guessing game
This function is the main game logic where the player guesses the number.
It also handles different game levels and provides feedback to the player.
"""
def guess_the_number(level):
    # Calculate the maximum number based on the chosen level
    max_number = level * 10

    # Generate a random secret number between 1 and the calculated maximum
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"🎮 Welcome to Level {level} of the Number Guessing Game!")
    background_music.play()
    print(f"🤔 The system is thinking of a number between 1 and {max_number}.")

    while True:
        try:
            # Prompt the player to enter their guess
            player_guess = int(input("🤷 Enter your guess: "))
        except ValueError:
            # Handle invalid input (non-integer)
            print(f"{RED}❌ Invalid input. Please enter a valid number.{END_COLOR}")
            continue

        attempts += 1

        if player_guess < secret_number:
            print(f"{YELLOW}👇 Too low! Try again.{END_COLOR}")
            play_incorrect_sound()
        elif player_guess > secret_number:
            print(f"{YELLOW}👆 Too high! Try again.{END_COLOR}")
            play_incorrect_sound()
        else:
            play_correct_sound()
            print(f"{GREEN}🎉 Congratulations! You've guessed the number {secret_number} in {attempts} attempts!{END_COLOR}")
            background_music.stop()
            break

    if level == 3:
        print(f"{GREEN}🏆 Congratulations! You have completed all levels!")
        play_correct_sound()
        display_winners_award()
        print("📲 The next version of the game will be Android-based. Stay tuned!")
        time.sleep(5)
    else:
        next_level = level + 1
        while True:
            play_next_level = input(f"Do you want to play Level {next_level}? (yes/no): ").lower()

            if play_next_level == 'yes':
                guess_the_number(next_level)
                break  # Break the loop if 'yes' is entered
            elif play_next_level == 'no':
                background_music.play()
                print("👋 Thanks for playing!")
                break  # Break the loop if 'no' is entered
            else:
                print(f"{RED}❌ Invalid choice. Please enter{END_COLOR} {GREEN}'yes' or 'no' {END_COLOR}.")

# Start the game by calling the start_game function
start_game()
