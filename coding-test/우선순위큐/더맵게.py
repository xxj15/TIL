import heapq
def solution(scoville, K):
    ans = 0
    heapq.heapify(scoville)
    
    while len(scoville) >=2 and scoville[0]<K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new = first + second * 2
        
        heapq.heappush(scoville, new)
        ans += 1
    
    if scoville[0] < K:
        return -1
    
    return ans