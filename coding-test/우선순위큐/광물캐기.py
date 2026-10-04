# 그리디 + 우선순위큐
import heapq
def solution(picks, minerals):
    mineral_group = []
    pirodo = []
    minerals = minerals[:sum(picks) * 5]
    
    for i in range(0, len(minerals), 5):
        mineral_group.append(minerals[i:i+5])

    for group in mineral_group:
        s = 0
        for m in group:
            if m == 'diamond':
                s += 25
            elif m == 'iron':
                s += 5
            else:
                s += 1
        heapq.heappush(pirodo, (-s, group))
    
    ans = 0
    for idx, pick_cnt in enumerate(picks):
        for _ in range(pick_cnt):
            if not pirodo:
                break
            
            _, group = heapq.heappop(pirodo)
            
            if idx == 0:
                for _ in group :
                    ans += 1
            
            elif idx == 1:
                for m in group:
                    if m == 'diamond':
                        ans += 5
                    else:
                        ans += 1
            
            else:
                for m in group:
                    if m == 'diamond': ans += 25
                    elif m == 'iron' : ans += 5
                    else: ans += 1
    
    return ans