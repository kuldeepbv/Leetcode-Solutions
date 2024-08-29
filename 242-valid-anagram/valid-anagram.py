class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if char not in t:
                return False
            else:
                t = t.replace(char, '', 1)

        if t == '':
            return True
        else:
            return False