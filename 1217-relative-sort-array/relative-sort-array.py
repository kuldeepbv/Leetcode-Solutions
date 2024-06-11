class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num_count = {}
        not_in_arr2 = []

        for num in arr1:
            if num in arr2:
                if num in num_count:
                    num_count[num] += 1
                else:
                    num_count[num] = 1
            else:
                not_in_arr2.append(num)

        final = []

        for num in arr2:
            while num_count.get(num) > 0:
                final.append(num)
                num_count[num] -= 1
        
        final = final + sorted(not_in_arr2)
    
        return final