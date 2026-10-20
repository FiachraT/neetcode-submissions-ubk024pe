import math
class Solution:
    def hammingWeight(self, n: int) -> int:
        # find the biggest 2 to the powers that fit, then subtract and repeeat
        count = 0
        while n != 0:
            p = math.floor(math.log(n, 2))
            n -= 2**p
            count += 1
        return count

        