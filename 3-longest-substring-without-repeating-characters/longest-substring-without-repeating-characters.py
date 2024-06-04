class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        final = {}
        repeat = 0
        max_length = 0
        for i,char in enumerate(s):
            if char in final and final[char] >= repeat:
                repeat = final[char] + 1
            else:
                max_length = max(max_length, i - repeat + 1)
            final[char] = i

        return max_length