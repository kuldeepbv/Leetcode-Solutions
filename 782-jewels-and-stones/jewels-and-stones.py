class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        final = 0
        for char in stones:
            if char in jewels:
                final += 1
        return final