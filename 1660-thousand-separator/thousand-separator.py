class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        flag = 0
        ans = ''

        for i in range(len(n) - 1, -1, -1):
            if flag == 3:
                ans += '.' + n[i]
                flag = 1
            else:
                ans += n[i]
                flag += 1
        
        return ans[::-1]
            