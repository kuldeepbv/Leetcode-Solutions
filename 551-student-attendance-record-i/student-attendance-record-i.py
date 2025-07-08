class Solution:
    def checkRecord(self, s: str) -> bool:
        return (s.count('A') < 2 and len(s.split('LLL')) == 1) 
        cnt = 0
        for i in range(len(s)):
            if s[i] == 'A' and 'A' in s[i:]: 
                return False
            if s[i] == 'L':
                cnt += 1
                if cnt == 3:
                    return False
            else:
                cnt = 0
        return True