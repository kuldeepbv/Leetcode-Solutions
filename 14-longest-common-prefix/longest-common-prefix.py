class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final = []
        for letters in list(zip(*strs)):
            check = letters[0]
            count = 1
            for j in letters[1:]:
                if j == check:
                    count+=1
                else:
                    break
            if count == len(letters):
                final.append(letters[0])
            else:
                break
        return ''.join(final)