class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = arr[1] - arr[0]
        count = 0
        ans = []
        
        for i in range(len(arr)-1):
            currDiff = arr[i+1] - arr[i]
            
            if currDiff < minDiff:
                minDiff = currDiff
                count = 1
                ans = [[arr[i], arr[i+1]]]
            elif currDiff == minDiff:
                count += 1
                ans.append([arr[i], arr[i+1]])

            else:
                continue
        
        return ans
        # arr.sort()
        # diff = []
        # for i in range(len(arr) - 1):
        #     diff.append(abs(arr[i] - arr[i+1]))
        
        # min_diff = min(diff)
        # final = []
        # for i, num in enumerate(diff):
        #     if num == min_diff:
        #         final.append([arr[i], arr[i+1]])

        # return final