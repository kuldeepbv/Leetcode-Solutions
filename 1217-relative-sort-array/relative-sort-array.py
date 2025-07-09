class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        final = []
        for num in arr2:
            cnt = arr1.count(num)
            while cnt > 0:
                final.append(num)
                cnt -= 1

        arr1.sort()
        print(final, arr1)
        for num in arr1:
            print(num)
            if num not in final:
                cnt = arr1.count(num)
                while cnt > 0:
                    final.append(num)
                    cnt -= 1

        return final
