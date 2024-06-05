class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        final = []
        
        for candy in candies:
            final.append((candy + extraCandies) >= max_candies)

        return final