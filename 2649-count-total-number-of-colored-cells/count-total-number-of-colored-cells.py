class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n * (n - 1) * 2
        # if n == 1:
        #     return 1

        # ans = 1
        # for i in range(1,n):
        #     ans += (i * 4)
        
        # return ans