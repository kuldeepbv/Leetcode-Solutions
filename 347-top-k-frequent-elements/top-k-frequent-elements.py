class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final_dict = {}
        for num in nums:
            if num not in final_dict.keys():
                final_dict[num] = 1
            else:
                final_dict[num] += 1

        sorted_dict = dict(sorted(final_dict.items(), key=lambda item: item[1], reverse = True))

        return list(sorted_dict.keys())[:k]