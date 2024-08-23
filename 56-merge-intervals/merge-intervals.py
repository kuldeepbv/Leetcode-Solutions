class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        ##return intervals
        final = []
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]

            while i < len(intervals) - 1 and intervals[i+1][0] <= end:
                i += 1
                end = max(end, intervals[i][1])
            
            final.append([start, end])
            i += 1
        
        return final