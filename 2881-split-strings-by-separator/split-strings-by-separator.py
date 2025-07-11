class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        final = []
        for word in words:
            temp = word.split(separator)
            final += temp

        ans = []
        
        for f in final:
            if f:
                ans.append(f)
        
        return ans