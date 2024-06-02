class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i,char in enumerate(s[::-1]):
            s[i] = char