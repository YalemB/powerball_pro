import random
from colorama import Fore, Back, Style


class WhiteBallsNpwoer():

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




