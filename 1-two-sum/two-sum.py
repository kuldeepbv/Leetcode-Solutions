class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []


        # map_dict = {}
        # for i in range(len(nums)):
        #     if nums[i] in map_dict:
        #         return [map_dict[nums[i]], i]
        #     else:
        #         map_dict[target - nums[i]] = i