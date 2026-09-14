import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if scoville[0]>=K:
        return 0
    while len(scoville)>=2:
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        new = a + b * 2
        heapq.heappush(scoville, new)
        if scoville[0]>=K:
            return answer
    
    return answer if scoville[0]>=K else -1