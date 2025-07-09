class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                prod *= -1
            print(prod)
            
        return prod
        # def signFunc(product):
        #     if product > 0:
        #         return 1
        #     elif product < 0:
        #         return -1
        #     else:
        #         return 0 
    
        # prod = 1
        # for num in nums:
        #     prod *= num 
            
        # return signFunc(prod)