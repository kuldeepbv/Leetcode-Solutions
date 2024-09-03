class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            temp_target = numbers[left] + numbers[right]
            if temp_target > target:
                right -= 1
            elif temp_target < target:
                left += 1
            else:
                return [left + 1, right + 1]
