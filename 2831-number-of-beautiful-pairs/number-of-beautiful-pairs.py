from math import gcd
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            f = int(str(nums[i])[0])
            for next_num in nums[i+1:]:
                l = str(next_num)
                if len(l) > 1:
                    if gcd(f, int(l[-1])) == 1:
                        ans += 1
                else:
                    if gcd(f, int(l)) == 1:
                        ans += 1
        return ans