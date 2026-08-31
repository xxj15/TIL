def solution(k, dungeons):
    n = len(dungeons)
    visited = [-1]*n
    answer = 0
    
    def dfs(fatigue, cnt):
        nonlocal answer
        
        answer = max(answer, cnt)
        for i in range(n):
            if visited[i]==-1 and fatigue>=dungeons[i][0]:
                visited[i]=0
                dfs(fatigue-dungeons[i][1], cnt+1)
                visited[i]=-1
    dfs(k, 0)      

    return answer