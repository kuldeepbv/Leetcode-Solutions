class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_list = list(magazine)

        for char in ransomNote:
            if char not in magazine_list:
                return False
            else:
                magazine_list.remove(char)
        
        return True