from collections import Counter
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []
        for i in range(len(A)):
            cnt_A = Counter(A[:i+1])
            cnt_B = Counter(B[:i+1])
            agg_cnt = cnt_A + cnt_B
            temp = 0
            for value in agg_cnt.values():
                if value == 2:
                    temp += 1
            C.append(temp)
        return C