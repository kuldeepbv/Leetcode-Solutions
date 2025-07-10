class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            if set(word).issubset(set(allowed)):
                ans += 1
        return ans
        #     check = len(word)
        #     cnt = 0
        #     for char in word:
        #         if char in allowed:
        #             cnt += 1
        #     if cnt == check:
        #         ans += 1
        # return ans