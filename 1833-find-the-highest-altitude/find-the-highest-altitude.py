class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = []
        first = 0
        altitude.append(first)
        for i,num in enumerate(gain):
            altitude.append(altitude[i] + num)
        return max(altitude)