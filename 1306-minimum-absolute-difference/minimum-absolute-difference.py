class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = []
        for i in range(len(arr) - 1):
            diff.append(abs(arr[i] - arr[i+1]))
        
        min_diff = min(diff)
        final = []
        for i, num in enumerate(diff):
            if num == min_diff:
                final.append([arr[i], arr[i+1]])

        return final