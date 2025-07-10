class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []
        sorted_heights = sorted(heights, reverse = True)

        for h in sorted_heights:
            idx = heights.index(h)
            ans.append(names[idx])
        return ans