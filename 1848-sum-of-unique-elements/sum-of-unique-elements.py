class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = []
        repeat = []
        for num in nums:
            if num in repeat:
                continue
            if num not in ans:
                ans.append(num)
            else:
                repeat.append(num)
                ans.remove(num)
        return sum(ans)