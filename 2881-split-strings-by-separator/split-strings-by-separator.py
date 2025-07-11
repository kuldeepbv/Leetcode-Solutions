class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        final = [w for word in words for w in word.split(separator) if w]
        return final

        # final = []
        # for word in words:
        #     for w in word.split(separator):
        #         if w:
        #             final.append(w)
        
        # return final