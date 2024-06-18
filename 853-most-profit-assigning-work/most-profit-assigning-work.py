class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        zipped_list = sorted(zip(difficulty, profit))
        worker.sort()
        max_profit = 0
        curr_idx = 0
        temp_profit = 0

        for work in worker:
            while curr_idx < len(zipped_list) and work >= zipped_list[curr_idx][0]:
                temp_profit = max(temp_profit, zipped_list[curr_idx][1])
                curr_idx += 1
            max_profit += temp_profit

        return max_profit