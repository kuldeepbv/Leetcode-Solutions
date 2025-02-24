class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        
        sorted_dict = dict(sorted(count_dict.items(), key = lambda item:item[1], reverse = True))

        final = []
        for num in sorted_dict:
            if k == 0:
                return final
            else:
                final.append(num)
                k -= 1
        
        return final