from math import gcd
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            f = int(str(nums[i])[0])
            for next_num in nums[i+1:]:
                l = int(str(next_num)[-1])
                if gcd(f, l) == 1:
                    ans += 1
        return ans