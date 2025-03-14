class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        max_candy = max(candies)

        left = 0
        right = max_candy

        while left < right:
            middle = (left + right + 1) // 2

            if self.allocate_candies(candies, k, middle):
                left = middle
            else:
                right = middle - 1
        
        return left
    
    def allocate_candies(self, candies, k, candies_num):
        max_num_children = 0

        for pile in candies:
            max_num_children += pile // candies_num
        
        return max_num_children >= k