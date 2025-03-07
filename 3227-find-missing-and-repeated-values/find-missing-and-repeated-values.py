class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) * len(grid)

        count = {}

        for temp_list in grid:
            for num in temp_list:
                if num not in count:
                    count[num] = 1
                else:
                    count[num] += 1

        for i in range(1,n+1):
            if i not in count:
                missing = i
            elif count[i] == 2:
                repeat = i

        return [repeat, missing]