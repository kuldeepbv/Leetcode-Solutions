class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ''
        for w1, w2 in itertools.zip_longest(word1, word2, fillvalue = ''):
            final = final + w1 + w2
        return final