class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # def signFunc(product):
        #     if product > 0:
        #         return 1
        #     elif product < 0:
        #         return -1
        #     else:
        #         return 0 
    
        prod = 1
        for num in nums:
            prod *= num
        
        if prod > 0:
            return 1
        elif prod < 0:
            return -1
        else:
            return 0 
            
        #return signFunc(prod)