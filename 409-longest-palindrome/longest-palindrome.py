class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = {}
        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        
        even_num = 0
        one_count = 0
        odd_count = []

        for num in char_dict.values():
            if num % 2 == 0:
                even_num += num
            else:
                if num == 1 and one_count != 0:
                    one_count += 1
                else:
                    odd_count.append(num)

        if odd_count:
            final = even_num + one_count + max(odd_count)
            odd_count.remove(max(odd_count))
            for odd_num in odd_count:
                final += odd_num - 1
        else:
            final = even_num + one_count

        return final