class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse = True)
            add_element = stones[0] - stones[1]
            del stones[0]
            del stones[0]
            if add_element != 0:
                stones.append(add_element)
            #break
        if len(stones) == 0:
            return 0
        return stones[0]
