class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        final = {}
        for i, row in enumerate(mat):
            final[i] = row.count(1)

        sorted_dict = sorted(final.items(), key = lambda item: item[1])
        sorted_dict = dict(sorted_dict)

        return list(sorted_dict.keys())[:k]