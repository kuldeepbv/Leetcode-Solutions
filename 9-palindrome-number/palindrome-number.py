class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = str(x)

        return x == x[::-1]

        # l = 0
        # r = len(x) - 1
        
        # while l < r:
        #     if int(x[l]) != int(x[r]):
        #         return False
        #     l += 1
        #     r -= 1

        # return True