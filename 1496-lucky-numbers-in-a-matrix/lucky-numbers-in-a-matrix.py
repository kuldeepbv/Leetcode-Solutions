class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_num = []
        column = []
        for mat in matrix:
            min_num.append(min(mat))
        
        for i in range(len(matrix[0])):
            temp = []
            for mat in matrix:
                temp.append(mat[i]) 
            column.append(max(temp))
        
        final = []

        for col in column:
            if col in min_num:
                final.append(col)
        return final 