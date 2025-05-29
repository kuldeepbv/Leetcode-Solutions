class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i

        for i, num in enumerate(nums):
            if num == target:
                return [i, hashmap[num]]

        return [-1, -1]