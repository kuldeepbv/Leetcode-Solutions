class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        cost.sort(reverse = True)
        total = 0
        for i in range(1,len(cost)+1):
            if i % 3 != 0:
                total += cost[i-1]

        return total