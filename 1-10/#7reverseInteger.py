import math

class Solution(object):
    def reverse(self, x):
        MIN = -2147483648 # -2^31
        MAX = 2147483647  # 2^31 - 1

        res = 0
        negative = False
        
        # make sure it accepts negative
        if x < 0:
            negative = True
            x = abs(x)

        while x:
            digit = int(math.fmod(x, 10)) # python functionality of
            x = int(x / 10)               #  -1 % 10 = 9 and -1 // 10 =- 1

            if (res > MAX // 10 or 
                (res == MAX // 10 and digit >= MAX % 10)):
                return 0

            if (res < MIN // 10 or
                (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            
            res = (res * 10) + digit

        return -res if negative else res
