class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}

        for i, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = i
            else:
                if abs(nums_dict[num] - i) <= k:
                    return True
                else:
                    nums_dict[num] = i
        
        return False
