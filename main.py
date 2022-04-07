from Draws import Draw
from colorama import Fore, Back, Style
y = input(Fore.BLUE +"Enter name to play : ")
i = 0
z = 0
print("5 rounds Game"+ Style.RESET_ALL)
while i < 5:
    x = Draw(y)
    print(x)
    ls_res = x.check_win().split("$")
    if ls_res[-1].isnumeric():
        z += int(ls_res[-1])

    t= input(" ")
    i +=1

if z > 0:
    print(Fore.BLUE +f"Congrats You won"+Style.RESET_ALL+Fore.YELLOW+F" {z}$")
else:
    print(Fore.BLUE +"you didn't won anything!!\ngood luck next time!!")
print( Fore.BLUE + "GAME OVER !!")



