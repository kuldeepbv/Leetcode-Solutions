class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_value = 0
        for i in range(len(s)-1):
            diff = abs(ord(s[i]) - ord(s[i+1]))
            ascii_value += diff
        return ascii_value