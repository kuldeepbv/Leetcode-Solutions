class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'

        vowels_in_s = []

        for char in s:
            if char in vowels:
                vowels_in_s.append(char)
        
        final = []
        i = len(vowels_in_s) - 1

        for char in s:
            if char in vowels:
                final.append(vowels_in_s[i])
                i -= 1
            else:
                final.append(char)
            
        return ''.join(final)