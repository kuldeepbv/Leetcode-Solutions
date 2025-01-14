class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []
        for i in range(len(A)):
            sort_A = sorted(A[:i+1])
            sort_B = sorted(B[:i+1])
            temp = 0
            for i in range(len(sort_A)):
                if sort_A[i] in sort_B:
                    temp += 1
            C.append(temp)
        return C