class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        final = []
        for word in s_list:
            final.append(word[::-1])
        
        return ' '.join(final)