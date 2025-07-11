class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        j = []
        for i, num in enumerate(nums):
            if num == key:
                j.append(i)

        j_ind = 0
        ans = []
        while j_ind < len(j):
            temp = []
            for i in range(len(nums)):
                if abs(i - j[j_ind]) <= k:
                    temp.append(i)
            j_ind += 1
            ans += temp
        return list(set(ans))