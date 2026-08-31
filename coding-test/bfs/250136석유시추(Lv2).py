from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [[-1] * m for _ in range(n)]
    lands = [0] * (n*m+1)
    land_id = 1

    def bfs(x, y):
        cnt = 1
        queue = deque()
        queue.append((x, y))

        while queue:
            now_x, now_y = queue.popleft()
            for i in range(4):
                nx, ny = now_x + dx[i], now_y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == -1 and land[nx][ny] == 1:
                        visited[nx][ny] = land_id
                        queue.append((nx, ny))
                        cnt += 1
        return cnt
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == -1:
                visited[i][j]=land_id
                lands[land_id] = bfs(i, j)
                land_id += 1

    max_ans = 0
    for j in range(m):
        check = set()
        ans = 0
        for i in range(n):
            lnd = visited[i][j]
            if lnd != -1 and lnd not in check:
                check.add(lnd)
                ans += lands[lnd]
        max_ans = max(max_ans, ans)

    return max_ans