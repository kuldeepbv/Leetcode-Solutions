class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profits_capital = list(zip(profits,capital))
        profits_capital = sorted(profits_capital, key = lambda x: x[0], reverse=True)

        while k>0:
            elem = -1
            for i, tup in enumerate(profits_capital):
                if tup[1]<=w:
                    w+=tup[0]
                    elem = i
                    k-=1
                    profits_capital.pop(elem)
                    break
            if elem==-1:
                return w
        return w