class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_list = []
        for char in s:
            char = char.lower()
            if char.isalnum():
                string_list.append(char)
        if string_list == string_list[::-1]:
            return True
        else:
            return False