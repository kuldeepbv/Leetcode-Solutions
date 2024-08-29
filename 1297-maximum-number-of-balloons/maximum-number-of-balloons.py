class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        check = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        final = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        
        for char in text:
            if char in check.keys():
                final[char] += 1
        
        for f in final:
            if final[f] == 0:
                return 0
            else:
                final[f] = final[f] // check[f]
        
        return min(final.values())