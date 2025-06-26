class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
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
                
        for key, value in t_dict.items():
            if key in s_dict:
                if value != s_dict[key]:
                    return key
            else:
                return key