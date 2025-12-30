import time
from random import randint

WIDTH_CLI = 80
LEVELS = {
    "Easy": 10,
    "Medium": 5,
    "Hard": 3
}
MIN = 1
MAX = 100

recordes: list[dict] = []
for key in LEVELS.keys():
    data = {"level": key, "attempts": None , "time": None}
    recordes.append(data)

def iniciar_game():
    while True:
        escolha_pc = randint(MIN, MAX)  # número novo a cada jogo

        print("")
        print(" Welcome to the Number Guessing Game! ".center(WIDTH_CLI, "="))

        # Seleção de dificuldade
        while True:
            try:
                print("\nPlease select a difficulty level:\n")
                for i, (k, v) in enumerate(LEVELS.items()):
                    print(f"{i + 1}. {k} ({v} chances)")

                level: int = int(input("Enter your choice: "))
                chances = list(LEVELS.values())[level - 1]
                level_name = list(LEVELS.keys())[level - 1]
                break
            except (ValueError, IndexError):
                print(f"\nInvalid choice. Choose between 1 and {len(LEVELS)}.")

        print(f"\nGreat! You selected the {level_name} level.")
        print("Let's start the game!\n")

        tentativas = 0
        time_start = time.perf_counter()

        # Loop principal do jogo
        while chances > 0:
            print(" Game ".center(WIDTH_CLI, "="))
            print(f"{chances} chance(s) left.")

            try:
                escolha = int(input("Enter your guess: "))

                if escolha < MIN or escolha > MAX:
                    raise ValueError

                tentativas += 1

                if escolha == escolha_pc:
                    time_end = time.perf_counter()
                    print(f"\nCongratulations! You guessed the number in {tentativas} attempts.")
                    print(f"You win in {time_end - time_start:.2f} seconds.\n")

                    recorde = recordes[level-1]

                    if recorde["attempts"] is None:
                        recorde["attempts"] = tentativas
                        recorde["time"] = time_end - time_start
                        print("\n\nFirst record for this level!\n\n")
                    elif tentativas < recorde["attempts"]:
                        recorde["attempts"] = tentativas
                        recorde["time"] = time_end - time_start
                        print("\n\nNew record beaten!\n\n")



                    if tentativas < recordes[level-1]["attempts"]:
                        print("recorde batido")



                    break

                elif escolha > escolha_pc:
                    print("Incorrect! The number is less than your guess.\n")
                else:
                    print("Incorrect! The number is greater than your guess.\n")

                chances -= 1

            except ValueError:
                print(f"Please enter a number between {MIN} and {MAX}.\n")

        else:
            time_end = time.perf_counter()
            print(f"You lose! The number was {escolha_pc}.")
            print(f"Time spent: {time_end - time_start:.2f} seconds.\n")

        # Reinício controlado
        reiniciar = input("New game? (y/n): ").strip().upper()
        if reiniciar != "Y":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    iniciar_game()
