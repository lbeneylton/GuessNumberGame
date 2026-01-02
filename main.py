import os
import time
from random import randint
from time import sleep

# ================== CONFIGURAÇÕES ==================
WIDTH_CLI = 80

LEVELS = {
    "Easy": 10,
    "Medium": 5,
    "Hard": 3
}

MIN = 1
MAX = 100
ESPERA = 2


# ================== UTILIDADES ==================
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ================== RECORDES ==================
recordes = {
    level: {"attempts": None, "time": None}
    for level in LEVELS
}


# ================== JOGO ==================
def iniciar_game():
    while True:
        clear()
        escolha_pc = randint(MIN, MAX)

        print("")
        print(" Welcome to the Number Guessing Game! ".center(WIDTH_CLI, "="))

        # -------- Seleção de dificuldade --------
        while True:
            try:
                print("\nPlease select a difficulty level:\n")
                for i, (k, v) in enumerate(LEVELS.items(), start=1):
                    print(f"{i}. {k} ({v} chances)")

                level = int(input("\nEnter your choice: "))
                level_name = list(LEVELS.keys())[level - 1]
                chances = LEVELS[level_name]
                break
            except (ValueError, IndexError):
                print(f"\nInvalid choice. Choose between 1 and {len(LEVELS)}.")

        print(f"\nGreat! You selected the {level_name} level.")
        print("Let's start the game!\n")
        sleep(ESPERA)

        clear()
        tentativas = 0
        time_start = time.perf_counter()

        # -------- Loop principal --------
        while chances > 0:
            clear()
            recorde = recordes[level_name]

            print(" Game ".center(WIDTH_CLI, "="))
            print(f"Level: {level_name}")
            print(f"Chances left: {chances}")
            print(f"Attempts used: {tentativas}")

            if recorde["attempts"] is not None:
                print(f"Record: {recorde['attempts']} attempts "
                      f"({recorde['time']:.2f}s)")

            print(f"\nChoose a number between {MIN} and {MAX}")

            # -------- Entrada do jogador --------
            try:
                escolha = int(input("Enter your guess: "))
                if not MIN <= escolha <= MAX:
                    raise ValueError
            except ValueError:
                print(f"\nPlease enter a valid number between {MIN} and {MAX}.")
                sleep(ESPERA)
                continue

            tentativas += 1

            # -------- Verificação --------
            if escolha == escolha_pc:
                time_end = time.perf_counter()
                tempo_total = time_end - time_start

                clear()
                print(" YOU WIN! ".center(WIDTH_CLI, "="))
                print(f"\nYou guessed the number in {tentativas} attempts.")
                print(f"Time: {tempo_total:.2f} seconds.")

                if (recorde["attempts"] is None or
                        tentativas < recorde["attempts"]):
                    recorde["attempts"] = tentativas
                    recorde["time"] = tempo_total
                    print("\n New record for this level! ")

                break

            elif escolha > escolha_pc:
                print("\nToo high!")
            else:
                print("\nToo low!")

            chances -= 1
            sleep(ESPERA)

        # -------- Derrota --------
        else:
            time_end = time.perf_counter()
            clear()
            print(" GAME OVER ".center(WIDTH_CLI, "="))
            print(f"\nYou lose! The number was {escolha_pc}.")
            print(f"Time spent: {time_end - time_start:.2f} seconds.")

        # -------- Reinício --------
        again = input("\nNew game? (y/n): ").strip().upper()
        if again != "Y":
            clear()
            print("\nThanks for playing!")
            break


# ================== MAIN ==================
if __name__ == "__main__":
    iniciar_game()
