class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()

        if len(s_list) != len(pattern):
            return False
        
        s_dict = {}
        check = []

        for i, letter in enumerate(pattern):
            if letter not in s_dict:
                if s_list[i] not in check:
                    s_dict[letter] = s_list[i]
                    check.append(s_list[i])
                else:
                    return False
            else:
                if s_dict[letter] != s_list[i]:
                    return False
        
        return True