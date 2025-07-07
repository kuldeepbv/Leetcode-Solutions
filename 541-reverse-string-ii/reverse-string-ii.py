class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s = list(s)
        # final = ''
        # flag = False
        for i in range(0, len(s), 2 * k):
            list_s[i:i + k] = list_s[i:i + k][::-1]
            # if flag == False:
            #     final += s[i:i + k][::-1]
            #     flag = True
            # else:
            #     final += s[i:i + k]
            #     flag = False
        
        return ''.join(list_s)