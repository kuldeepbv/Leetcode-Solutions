class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp = 0
        for i in s:
            if i in t:
                ind = t.find(i)
                t = t[ind+1:]
                temp += 1
            else:
                return False
        if temp == len(s):
            return True