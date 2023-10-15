class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in  range(n)]
        for i, j, w in edges:
            dist[i][j] = w
            dist[j][i] = w
        for i in range(n):
            dist[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        res = 0
        minCnt = float('inf')
        for i in range(n):
            cnt = 0
            for d in dist[i]:
                if d <= distanceThreshold:
                    cnt += 1
            if cnt <= minCnt:
                minCnt = cnt
                res = i
        return res
