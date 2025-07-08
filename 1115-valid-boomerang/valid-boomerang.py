class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        return ((points[0][0] * (points[1][1] - points[2][1])) + (points[1][0] * (points[2][1] - points[0][1])) + (points[2][0] * (points[0][1] - points[1][1]))) != 0



        # if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
        #     return False
        # temp = []
        # for i in range(2):
        #     if (points[i + 1][0] - points[i][0]) == 0:
        #         m = (points[i + 1][1] - points[i][1])
        #     else:
        #         m = (points[i + 1][1] - points[i][1]) / (points[i + 1][0] - points[i][0])
        #     if m in temp:
        #         return False
        #     temp.append(m)
        # return True    