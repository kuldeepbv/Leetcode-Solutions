class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
        # final = []

        # for num in nums1:
        #     if num in nums2:
        #         final.append(num)
        
        # return list(set(final))