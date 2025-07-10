class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = []
        repeat = []
        for num in nums:
            if num in repeat:
                print('1st if')
                continue
            if num not in ans:
                print('2nd if')
                ans.append(num)
            else:
                print('else')
                repeat.append(num)
                ans.remove(num)
            print(ans)
            print(repeat)
        return sum(ans)
        #     if num not in 
        #     if num not in nums[i+1:]:
        #         print('if')
        #         ans += num
        # return ans