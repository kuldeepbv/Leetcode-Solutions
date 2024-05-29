class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        final = []
        for i in range(len(numbers)):
            next_num = target - numbers[i]
            if next_num in numbers[i+1:]:
                final.append(i+1)
                final.append((numbers[i+1:].index(next_num)) + (i+2))
                break
        return final