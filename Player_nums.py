from Lottery_machine import WhiteBallsNpwoer


class Player(WhiteBallsNpwoer):
    def __init__(self):
        super().__init__()
        self.p_res = txt2 = "Your lucky numbers:\n {} {} {} {} {} Power Ball {}"

    def __str__(self):
        return super().__str__() + "\n" + self.p_res


# x= Player()
# print(x)
