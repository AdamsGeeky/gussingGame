import random
import pygame

# Initialize pygame
pygame.init()

# Load sound files
correct_sound = pygame.mixer.Sound("./sounds/correct.wav")
incorrect_sound = pygame.mixer.Sound("./sounds/incorrect.wav")
background_music = pygame.mixer.Sound("./sounds/background_music.wav")

# Function to play correct guess sound
def play_correct_sound():
    correct_sound.play()

# Function to play incorrect guess sound
def play_incorrect_sound():
    incorrect_sound.play()

# ANSI escape codes for color
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
END_COLOR = '\033[0m'

# Function with argument level to play the game
def guess_the_number(level):
    if level == 1:
        max_number = 10
    elif level == 2:
        max_number = 20
    elif level == 3:
        max_number = 30
    else:
        print(f"{RED}❌ Invalid level. Please choose a level between 1 and 3.{END_COLOR}")
        return
    secret_number = random.randint(1, max_number)
    
    attempts = 0

    print(f"🎮 Welcome to Level {level} of the Number Guessing Game!")
    background_music.play()
    print(f"🤔 The system is thinking of a number between 1 and {max_number}.")

    while True:
        try:
            player_guess = int(input("🤷 Enter your guess: "))
        except ValueError:
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
        print("📲 The next version of the game will be Android-based. Stay tuned!")
    else:
        next_level = level + 1
        play_next_level = input(f"Do you want to play Level {next_level}? (yes/no): ").lower()
        if play_next_level == 'yes':
            guess_the_number(next_level)
        else:
            background_music.play()
            print("👋 Thanks for playing!")

# Start the game by calling the guess_the_number function
print("👋 Welcome to the Number Guessing Game!")
background_music.play()    
while True:
    try:
        level = int(input("Choose a level (1, 2, or 3): "))
        if level not in [1, 2, 3]:
            raise ValueError(f"{RED}❌ Invalid level. Please choose a level between 1 and 3.{END_COLOR}")
        break
    except ValueError as e:
        print(e)
guess_the_number(level)

