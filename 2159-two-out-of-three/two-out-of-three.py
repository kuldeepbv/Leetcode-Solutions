class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            if (num in nums2 or num in nums3) and num not in ans:
                ans.append(num)
        
        for num in nums2:
            if num in nums3 and num not in ans:
                ans.append(num)

        return ans
