class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        final_dict = {}
        for num in arr:
            if num not in final_dict:
                final_dict[num] = 1
            else:
                final_dict[num] += 1

        set_sort = sorted(list(set(final_dict.values())))
        orig_sort = sorted(list(final_dict.values()))
        return set_sort == orig_sort