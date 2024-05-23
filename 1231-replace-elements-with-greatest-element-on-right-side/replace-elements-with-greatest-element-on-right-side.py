class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_Max = -1
        for i in range(len(arr)-1, -1,-1):
            new_max = max(right_Max, arr[i])
            arr[i] = right_Max
            right_Max = new_max 
        return arr