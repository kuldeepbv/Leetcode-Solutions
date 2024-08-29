class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for char in s:
        #     if char not in t:
        #         return False
        #     else:
        #         t = t.replace(char, '', 1)

        # if t == '':
        #     return True
        # else:
        #     return False
        s_dict = {}
        t_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1

        if s_dict == t_dict:
            return True
        else:
            return False