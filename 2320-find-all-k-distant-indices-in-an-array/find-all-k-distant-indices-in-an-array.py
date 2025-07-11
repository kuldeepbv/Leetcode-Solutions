class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        j = []
        for i, num in enumerate(nums):
            if num == key:
                j.append(i)

        ans = []

        for i in range(len(nums)):
            flag = False
            for j_ind in j:
                if abs(i - j_ind) <= k:
                    flag = True
                    break
            if flag:
                ans.append(i)

        return ans