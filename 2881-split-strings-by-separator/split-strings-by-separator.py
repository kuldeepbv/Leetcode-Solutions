class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        final = []
        for word in words:
            temp = word.split(separator)
            for t in temp:
                if t != '':
                    final.append(t)

            #print(final)
            #final = final + word.split(separator)
        return final