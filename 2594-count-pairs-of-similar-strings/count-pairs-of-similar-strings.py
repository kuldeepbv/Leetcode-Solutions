class Solution:
    def similarPairs(self, words: List[str]) -> int:
        set_words = [set(word) for word in words]
        
        ans = 0

        for i, set_word in enumerate(set_words):
            for next_set_word in set_words[i+1:]:
                if set_word == next_set_word:
                    ans += 1
        return ans
        #for 