class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in final.keys():
                final[sorted_word] = [word]
            else:
                final[sorted_word].append(word)
        return final.values()