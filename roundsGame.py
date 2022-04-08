from Draws import Draw
from colorama import Fore, Back, Style
import time


def play_rounds(name, rounds):
    print(Back.RED + Fore.BLACK + f"CHECK NUMBERS FOR {name.capitalize()}" + Style.RESET_ALL)
    i = 0
    cout = 0
    while i < rounds:
        x = Draw(name)
        ls = x.check_win().split("$")
        win = x.check_win()
        time.sleep(0.5)
        print(x.res.format(*x.x, x.p))
        time.sleep(1.7)
        print(x.p_res.format(*x.y, x.s))
        time.sleep(1.2)
        print(win)

        if ls[-1].isnumeric():
            cout += int(ls[-1])
        i += 1
        if i == rounds:
            break

        next_round = input(Fore.GREEN + "Tap for next round\n" + f"------{i + 1} try------" + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.GREEN + "******Game over!!******" + Style.RESET_ALL)

    if cout > 0:
        print("Congrats You won" + Style.RESET_ALL + Fore.YELLOW + F" {cout}$" + Style.RESET_ALL)
    else:
        print("you didn't won anything!!\ngood luck next time!!")


player_name = input("Enter name: ")

number_of_rounds = int(input("How many rounds do you want to play? :"))
play_rounds(player_name, number_of_rounds)