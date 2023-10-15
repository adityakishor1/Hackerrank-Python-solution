class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
 		res = []
        for (L, R) in queries:
            i = L
            xor = 0
            while i <= R:
                xor ^= arr[i]
                i += 1
            res.append(xor)
        return res
