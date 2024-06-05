class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = {}

        for word in words:
            temp_char = []
            for char in word:
                if char not in common:
                    common[char] = 1
                    temp_char.append(char)
                else:
                    if char not in temp_char:
                        common[char] += 1
                        temp_char.append(char)
                    else:
                        repeat = (char) * (temp_char.count(char) + 1)
                        if repeat not in common:
                            common[repeat] = 1
                            temp_char.append(char)
                        else:
                            common[repeat] += 1
                            temp_char.append(char)
        
        final = [key for key,value in common.items() if value == len(words)]
        
        final_dict = {}
        for f in final:
            f_list = list(f)
            char = f_list[0]
            if char not in final_dict:
                final_dict[char] = len(f_list)
            else:
                if len(f_list) > final_dict[char]:
                    final_dict[char] = len(f_list)
        
        final_common = []
        
        for key,value in final_dict.items():
            for val in range(value):
                final_common.append(key)
        return final_common