# This program is a Rock, Paper, Scissors game between the user and the machine.
#
# The program will randomly select one of the three options and the user has to
# type one of the three options to play.
#
# The program will then compare the user's choice with the machine's choice and
# print if the user won or lost.
#
# The program also has a feature to exit the game by pressing the F10 key.
#
# The program uses the threading library to run the check_for_exit function in
# the background, which checks if the user has pressed the F10 key.
#
# The program will then print a message saying that the program will be closed
# and then exit the program.

import random
import keyboard
import threading
import sys

# Define the key to exit the program
stop_key = "F10"

# Define the function to check for the exit key
def check_for_exit():
    # Wait for the exit key to be pressed
    keyboard.wait(stop_key)
    # Print a message saying that the program will be closed
    print(f"\nSe ha pulsado {stop_key}. Cerrando el programa...")
    # Exit the program
    sys.exit()

# Create a thread for the check_for_exit function
exit_thread = threading.Thread(target=check_for_exit, daemon=True)

# Start the thread
exit_thread.start()

# Initialize the randomly chosen option
initial_chosen = random.randint(1,3)
# Initialize the user's chosen option
chosen = 0

# Check which option the machine has chosen
if initial_chosen == 1:
    chosen = "Rock"
elif initial_chosen == 2:
    chosen = "Paper"
else:
    chosen = "Scissors"

# Start the main loop
while True:
    # Print the options
    print("====================================")
    print("Rock, paper, or scissors")
    # Ask the user for their choice
    user_chosen = input(str("What will you choose? "))

    # Print the machine's choice
    print(f"The machine chose {chosen}")

    # Check if the user has won or lost
    if initial_chosen == 1 and user_chosen == "Rock":
        print("It's a tie!")
    elif initial_chosen == 1 and user_chosen == "Paper":
        print("You won!")
    elif initial_chosen == 1 and user_chosen == "Scissors":
        print("You lost!")

    if initial_chosen == 2 and user_chosen == "Rock":
        print("You lost!")
    elif initial_chosen == 2 and user_chosen == "Paper":
        print("It's a tie!")
    elif initial_chosen == 2 and user_chosen == "Scissors":
        print("You won!")

    if initial_chosen == 3 and user_chosen == "Rock":
        print("You won!")
    elif initial_chosen == 3 and user_chosen == "Paper":
        print("You lost!")
    elif initial_chosen == 3 and user_chosen == "Scissors":
        print("It's a tie!")



# I personally only needed AI help creating the thread as I didn't even know what it was,
# i wanted the program to be waiting for the stop_key to be pressed and I didn't know how
# to do it since there was alredy a while True:
# the rest I did it myself, so probably unoptimized as f***
