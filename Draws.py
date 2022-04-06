from Lottery_machine import WhiteBallsNpwoer
from Player_nums import Player
import  colorama

class Draw(Player):
    def __init__(self):
        super().__init__()
        self.title = "CHECK NUMBERS"
        self.__lottery = WhiteBallsNpwoer()
        self.__player_nums = Player()
        self.x = self.__lottery.dailyNums()  # lottery numbers
        self.y = self.__player_nums.dailyNums()  # player lucky numbers
        self.p = self.__lottery.strog_num()  # lottery power number
        self.s = self.__player_nums.strog_num()  # player strong number

    def check_win(self):  # check how many numbers the player got right
        self.c = 0
        for i in self.x:
            self.n = self.y.count(i)
            self.c += self.n
        if self.s == self.p:
            if self.c == 5:
                return "Correct White Balls and the Powerball: Jackpot $324,000,000"
            elif self.c == 4:
                return "4 Correct White Balls and the Powerball: $10,000"
            elif self.c == 3:
                return "3 Correct White Balls and the Powerball: $100"
            elif self.c == 2:
                return "2 Correct White Balls and the Powerball: $7"
            elif self.c == 1:
                return "1 Correct White Ball and the Powerball: $4"
            else:
                return "No White Balls, Just the Powerball: $4"

        elif self.s != self.p:
            if self.c == 5:
                return "5 Correct White Balls, but no Powerball: $1,000,000"
            elif self.c == 4:
                return "4 Correct White Balls, but no Powerball: $100"
            elif self.c == 3:
                return "3 Correct White Balls, but no Powerball: $7"
            else:
                return "Try again!"


    def __str__(self):
        self.__res = self.res.format(*self.x, self.p)
        self.__p_res = self.p_res.format(*self.y, self.s)
        return self.__res + "\n" + self.__p_res + "\n" +self.check_win()

