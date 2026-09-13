# 프로세스
from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for idx, key in enumerate(priorities):
        queue.append((idx, key))

    while queue:
        escape = True
        idx, pri = queue.popleft()
        
        for i, p in queue:
            if pri<p:
                queue.append((idx,pri))
                escape = False
                break
                
        if escape:
            answer += 1
            if idx == location:
                break
        
    return answer