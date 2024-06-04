class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        current = 0
        for g in gain:
            current += g
            if current > max_alt:
                max_alt = current
        return max_alt