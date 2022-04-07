from Lottery_machine import WhiteBallsNpwoer
from Player_nums import Player
from colorama import Fore, Back, Style


class Draw():
    def __init__(self,name):
        self.name = name.capitalize()
        super().__init__()
        self.title = Back.RED+Fore.BLACK +f"CHECK NUMBERS FOR {self.name}."+ Style.RESET_ALL
        self.__lottery = WhiteBallsNpwoer()
        self.__player_nums = Player()
        self.x = self.__lottery.dailyNums()  # lottery numbers
        self.y = self.__player_nums.dailyNums()  # player lucky numbers
        self.p = self.__lottery.strog_num()  # lottery power number
        self.s = self.__player_nums.strog_num()  # player strong number
        self.res = Fore.BLUE +"Today's Powerball Winning Numbers:\n" + Style.RESET_ALL +" {} {} {} {} {} " + Fore.YELLOW + "{}" + Style.RESET_ALL
        self.p_res = Fore.BLUE +"Your lucky numbers:\n" +  Style.RESET_ALL + " {} {} {} {} {} " + Style.RESET_ALL + Fore.YELLOW + "{}" + Style.RESET_ALL

    def check_win(self):  # check how many numbers the player got right
        self.c = 0
        for i in self.x:
            if i in self.y:
                self.c += 1
        if self.s == self.p:
            if self.c == 5:
                return "Correct White Balls and the Powerball: " + Fore.YELLOW + "Jackpot $324,000,000"
            elif self.c == 4:
                return Fore.YELLOW + "4 " + Style.RESET_ALL + "Correct White Balls and the Powerball: " + Fore.YELLOW + "$10,000"
            elif self.c == 3:
                return Fore.YELLOW + "3 " + Style.RESET_ALL + "Correct White Balls and the Powerball: " + Fore.YELLOW + "$100"
            elif self.c == 2:
                return Fore.YELLOW + "2 " + Style.RESET_ALL + "Correct White Balls and the Powerball: " + Fore.YELLOW + "$7"
            elif self.c == 1:
                return Fore.YELLOW + "1 " + Style.RESET_ALL + "Correct White Ball and the Powerball: " + Fore.YELLOW + "$4"
            else:
                return "No White Balls, Just the Powerball: " + Fore.YELLOW + "$4"

        elif self.s != self.p:
            if self.c == 5:
                return Fore.YELLOW + "5 " + Style.RESET_ALL + "Correct White Balls, but no Powerball:" + Fore.YELLOW + "$1,000,000"
            elif self.c == 4:
                return Fore.YELLOW + "4 " + Style.RESET_ALL + "Correct White Balls, but no Powerball:" + Fore.YELLOW + "$100"
            elif self.c == 3:
                return Fore.YELLOW + "3 " + Style.RESET_ALL + "Correct White Balls, but no Powerball: " + Fore.YELLOW + "$7"
            else:
                return Fore.RED + "Try again!"+ Style.RESET_ALL

    def __str__(self):
        self.res = self.res.format(*self.x, self.p) # string for  lottery numbers
        self.p_res = self.p_res.format(*self.y, self.s)   # string for player lucky numbers
        return self.title + "\n" + self.res + "\n" + self.p_res + "\n" + self.check_win()
