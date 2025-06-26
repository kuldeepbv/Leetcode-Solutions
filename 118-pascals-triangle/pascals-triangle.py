class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = []
        if numRows == 0:
            return final

        first_row = [1]
        final.append(first_row)

        for i in range(1, numRows):
            prev_row = final[i - 1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)
            final.append(current_row)

        return final

        for i in range(1, numRows + 1):
            temp = [0] * i
            for i, t in enumerate(temp):
                print(i, t)

