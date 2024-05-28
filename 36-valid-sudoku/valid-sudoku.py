class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        count = 0

        for row in board:
            unique_element = []
            for row_element in row:
                if row_element == ".":
                    unique_element.append(row_element)
                elif row_element in numbers and row_element not in unique_element:
                    unique_element.append(row_element)
                else:
                    break
            if len(unique_element) == len(board):
                count += 1

        for i in range(len(board)):
            column = []
            for j in range(len(board[i])):
                column.append(board[j][i])
            unique_element = []
            for column_element in column:
                if column_element == ".":
                    unique_element.append(column_element)
                elif column_element in numbers and column_element not in unique_element:
                    unique_element.append(column_element)
                else:
                    break
            if len(unique_element) == len(board):
                count += 1

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):  
                square = []
                for row in board[i:i+3]:
                    for r in row[j:j+3]:
                        square.append(r)
                
                unique_element = []
                for square_element in square:
                    if square_element == ".":
                        unique_element.append(square_element)
                    elif square_element in numbers and square_element not in unique_element:
                        unique_element.append(square_element)
                    else:
                        break
                if len(unique_element) == len(board):
                    count += 1

        if count == 27:
            return True
        else:
            return False