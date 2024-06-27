class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        first_list = edges[0]

        for num in first_list:
            num_count = 1
            for curr_list in edges[1:]:
                if num in curr_list:
                    num_count += 1
            if num_count == n:
                return num