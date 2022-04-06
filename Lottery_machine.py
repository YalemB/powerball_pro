import random


class WhiteBallsNpwoer():
    def __init__(self):
        self.res = "Today's Powerball Winning Numbers:\n {} {} {} {} {} Power Ball {}"

    def dailyNums(self):
        nums = []
        x = 0
        while len(nums) < 5:
            n = random.randrange(1, 20 + 1)
            if n not in nums:
                nums.append(n)

        return sorted(nums)

    def strog_num(self):
        return random.randrange(1, 10 + 1)




