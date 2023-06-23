import random
import os


print("CODEBREAKER GAME")
print("The objective is to guess the secret code in as few attempts as possible.\n")


def generate_random_code():
    code = ""
    for i in range(4):
        num = random.randint(0, 6)
        code = code + str(num)
    return code


def is_code_valid(code):
    validity = True
    for i in range(len(code)):
        if code == "" or not code[i].isdigit() :
            validity = False
            break
        if int(code[i]) < 1 or int(code[i]) > 6:
            validity = False
            break
    return validity


def evaluate_guess(code, guess):
    # o=number of positions that match but not in which position, x=number of colors that match but are in wrong positions
    evaluation = ""
    for i in range(len(guess)):
        if code[i] == guess[i]:
            evaluation = evaluation + "o"
    pos_found_guess = []
    pos_found_code = []
    for i in range(len(guess)):
        for j in range(len(code)):
            if i != j and i not in pos_found_guess and j not in pos_found_code and guess[i] == code[j]:
                pos_found_guess.append(i)
                pos_found_code.append(j)
                evaluation = evaluation + "x"
                break
    return evaluation


def choose_game():
    while True:
        game = int(input("Input 1 for 1-player game or 2 for 2-player game: "))
        if game == 1 or game == 2:
            break
        else:
            print("Error, Input 1 for 1-player game or 2 for 2-player game")
    return game


def enter_secret_code():
    code = ""
    game = choose_game()
    if game == 1:
        code = generate_random_code()
    else:
        print("\nPlayer 2 enter the secret code (4 colors).")
        while True:
            code = input("You can use any combination of 4 symbols in ['1', '2', '3', '4', '5', '6'] as colors: ")
            if len(code) != 4:
                print("The secret code has exactly four colors. Try again!")
                continue
            if is_code_valid(code):
                break

        clear = lambda: os.system('cls')  # clear console after player enters code
        clear()
    return code


def main():
    code = enter_secret_code()
    print("Player 1 please, enter your color code.")
    print("You can use any combination of 4 symbols in ['1', '2', '3', '4', '5', '6'] as colors")

    tries = 8
    for i in range(tries):
        while True:
            print("Attempt", i+1)
            guess = input("")
            if len(guess) != 4:
                print("The secret code has exactly four colors. Try again!")
                continue
            if is_code_valid(guess):
                break
            else:
                print("You can only use ['1', '2', '3', '4', '5', '6'] as colors. Try again!")

        if code == guess:
            print("Congratulations! You found it in ", i+1, "attempts!")
            return
        else:
            print(evaluate_guess(code, guess))
    print("You failed to guess within 8 attempts.")
    print("The secret code was", code)


if __name__ == "__main__":
    main()