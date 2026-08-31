# 154540번 (무인도 여행) - Lv.2
from collections import deque
def solution(maps):
    maps = [list(row) for row in maps]

    m = len(maps)
    n = len(maps[0])

    visited = [[-1] * n for _ in range(m)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ans = []
    def bfs(x,y):
        cnt = int(maps[x][y])
        queue = deque()
        queue.append((x,y))
        visited[x][y]=1
        while queue:
            now_x, now_y = queue.popleft()
            for i in range(4):
                nx, ny = now_x + dx[i], now_y + dy[i]
                if 0<=nx<m and 0<=ny<n:
                    if visited[nx][ny]==-1 and maps[nx][ny]!='X':
                        cnt += int(maps[nx][ny])
                        visited[nx][ny]=1
                        queue.append((nx,ny))
        return cnt


    for i in range(m):
        for j in range(n):
            if visited[i][j] == -1 and maps[i][j] != 'X':
                ans.append(bfs(i, j))
                
    ans.sort()  
    return ans if ans else [-1]