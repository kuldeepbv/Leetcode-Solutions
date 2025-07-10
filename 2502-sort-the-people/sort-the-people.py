class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # ans = []
        # sorted_heights = sorted(heights, reverse = True)

        # for h in sorted_heights:
        #     idx = heights.index(h)
        #     ans.append(names[idx])
        # return ans

        # ans = {}
        # for name, height in zip(names, heights):
        #     ans[name] = height
        # sort_dict = sorted(ans.items(), key = lambda item: item[1], reverse = True)

        # l = list(zip(names, heights))
        # sort_l = sorted(l, key = lambda item: item[1], reverse = True)
        # ans = []
        # for nh in sort_l:
        #     ans.append(nh[0])
        # return ans
        
        name = [name for name, height in sorted(zip(names, heights), key = lambda item: item[1], reverse = True)]
        return name