class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}

        for s_ele, t_ele in zip(s, t):
            if s_ele in s_dict:
                if s_dict[s_ele] != t_ele:
                    return False
            else:
                if t_ele in s_dict.values():
                    return False
                else:
                    s_dict[s_ele] = t_ele

        return True