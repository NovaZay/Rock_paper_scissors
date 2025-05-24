import random
import keyboard
import threading
import sys

stop_key = "F10"

# Función que se ejecuta en segundo plano
def check_for_exit():
    keyboard.wait(stop_key)
    print(f"\nSe ha pulsado {stop_key}. Cerrando el programa...")
    sys.exit()

# Lanzamos el hilo
exit_thread = threading.Thread(target=check_for_exit, daemon=True)
exit_thread.start()

# Lógica del juego
initial_chosen = random.randint(1,3)
chosen = 0

if initial_chosen == 1:
    chosen = "Rock"
elif initial_chosen == 2:
    chosen = "Paper"
else:
    chosen = "Scissors"

while True:
    print("====================================")
    print("Rock, paper, or scissors")
    user_chosen = input(str("What will you choose? "))

    print(f"The machine chose {chosen}")

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
