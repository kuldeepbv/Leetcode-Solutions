class Solution:
    def checkRecord(self, s: str) -> bool:
        return (s.count('A') < 2 and len(s.split('LLL')) == 1) 
        # for i in range(len(s)-1, -1, -1):
        #     if s[i] == 'A' and 'A' in s[:i]: 
        #         return False
        #     elif s[i] == 'L':
        #         if s[i-1] == 'L' and s[i-2] == 'L':
        #             return False
        # return True