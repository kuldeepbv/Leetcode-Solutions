class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final = []
        for op in operations:
            if op == '+':
                final.append(final[-2] + final[-1])
            elif op == 'D':
                final.append(2 * final[-1])
            elif op == 'C':
                final.pop()
            else:
                final.append(int(op))

        return sum(final)