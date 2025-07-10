class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for acc in accounts:
            if sum(acc) > max_wealth:
                max_wealth = sum(acc)
        return max_wealth