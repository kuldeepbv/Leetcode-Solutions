class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first = 0
        all_char = 0

        while first < len(s) and all_char < len(t):
            if s[first] == t[all_char]:
                all_char += 1
            first += 1
        return len(t) - all_char