from Lottery_machine import WhiteBallsNpwoer
from Player_nums import Player
from colorama import Fore, Back, Style


class Draw():
    def __init__(self, name):
        self.name = name.capitalize()
        super().__init__()
        self.__lottery = WhiteBallsNpwoer()
        self.__player_nums = Player()
        self.x = self.__lottery.dailyNums()  # lottery numbers
        self.y = self.__player_nums.dailyNums()  # player lucky numbers
        self.p = self.__lottery.strog_num()  # lottery power number
        self.s = self.__player_nums.strog_num()  # player strong number
        self.res = "Today's Powerball Winning Numbers:\n" +Fore.LIGHTMAGENTA_EX +" {} {} {} {} {} " + Fore.YELLOW + "{}" + Style.RESET_ALL
        self.p_res = "Your lucky numbers:\n" +  Fore.LIGHTMAGENTA_EX  + " {} {} {} {} {} " + Style.RESET_ALL + Fore.YELLOW + "{}" + Style.RESET_ALL

    def check_win(self):  # check how many numbers the player got right
        self.txt = "Correct White Balls and the Powerball: " # white balls catch and the power ball string
        self.txt2 = "Correct White Balls, but no Powerball:" # white ball catch without power ball string
        self.c = 0
        for i in self.x:
            if i in self.y:
                self.c += 1
        if self.s == self.p:
            if self.c == 5:
                return self.txt + Fore.YELLOW + "Jackpot $324,000,000"
            elif self.c == 4:
                return Fore.YELLOW + "4 " + Style.RESET_ALL + self.txt + Fore.YELLOW + "$10,000"
            elif self.c == 3:
                return Fore.YELLOW + "3 " + Style.RESET_ALL + self.txt + Fore.YELLOW + "$100"
            elif self.c == 2:
                return Fore.YELLOW + "2 " + Style.RESET_ALL + self.txt + Fore.YELLOW + "$7"
            elif self.c == 1:
                return Fore.YELLOW + "1 " + Style.RESET_ALL + self.txt + Fore.YELLOW + "$4"
            else:
                return "No White Balls, Just the Powerball: " + Fore.YELLOW + "$4"

        elif self.s != self.p:
            if self.c == 5:
                return Fore.YELLOW + "5 " + Style.RESET_ALL + self.txt2 + Fore.YELLOW + "$1,000,000"
            elif self.c == 4:
                return Fore.YELLOW + "4 " + Style.RESET_ALL + self.txt2 + Fore.YELLOW + "$100"
            elif self.c == 3:
                return Fore.YELLOW + "3 " + Style.RESET_ALL + self.txt2 + Fore.YELLOW + "$7"
            else:
                return Fore.RED + "Try again!"+ Style.RESET_ALL

    def __str__(self):
        # string for  lottery numbers and player numbers and results
        return self.res.format(*self.x, self.p) + "\n" + self.p_res.format(*self.y, self.s) + "\n" + self.check_win()
