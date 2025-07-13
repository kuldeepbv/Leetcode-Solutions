class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        i = 0

        while i < len(s):
            print(i)
            if ans and abs(ord(s[i]) - ord(ans[-1])) == 32:
                print('if')
                ans.pop()
            else:
                print('else')
                ans.append(s[i])
            print(ans)
            i += 1
        
        return ''.join(ans)