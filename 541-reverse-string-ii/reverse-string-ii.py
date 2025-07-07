class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        final = ''
        flag = False
        for i in range(0, len(s), k):
            print(flag)
            if flag == False:
                final += s[i:i + k][::-1]
                flag = True
            else:
                final += s[i:i + k]
                flag = False
        
        return final