class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_ind = []
        odd_ind = []
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_ind.append(num)
            else:
                odd_ind.append(num)

        even_ind.sort()
        odd_ind.sort(reverse = True)       

        ans = [0] * len(nums) 
        ei = 0
        oi = 0

        for i in range(len(ans)):
            if i % 2 == 0:
                ans[i] = even_ind[ei]
                ei += 1
            else:
                ans[i] = odd_ind[oi]
                oi += 1
            
        return ans