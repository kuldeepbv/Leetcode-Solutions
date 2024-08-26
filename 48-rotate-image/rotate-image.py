import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        final = copy.deepcopy(matrix)
        temp = 0
        while temp < len(final[0]):
            for i in range(len(final) - 1, -1, -1):
                matrix[temp][len(final) - 1 - i] = final[i][temp]
            temp += 1