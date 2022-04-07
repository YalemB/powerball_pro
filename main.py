from Draws import Draw
from colorama import Fore, Back, Style
y = input("Enter name to play : ")
i = 0
z = 0
print("5 rounds Game")
while i < 5:
    x = Draw(y)
    print(x)
    ls_res = x.check_win().split("$")
    if ls_res[-1].isnumeric():
        z += int(ls_res[-1])

    t= input(" ")
    i +=1

if z > 0:
    print("Congrats You won"+Style.RESET_ALL+Fore.YELLOW+F" {z}$"+Style.RESET_ALL)
else:
    print("you didn't won anything!!\ngood luck next time!!")
print( "GAME OVER !!")



