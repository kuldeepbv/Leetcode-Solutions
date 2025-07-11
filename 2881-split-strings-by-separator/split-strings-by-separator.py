class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        final = []
        for word in words:
            temp = word.split(separator)
            for w in temp:
                if w:
                    final.append(w)
        
        return final