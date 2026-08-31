import heapq
def solution(n, k, enemy):
    answer = 0
    heap = []
    for e in enemy:
        answer += 1
        n-=e
        heapq.heappush(heap, -e)
        
        if n<0 :
            if k == 0:
                answer-=1
                break
            else:
                n -= heapq.heappop(heap)
                k -= 1
            
        
    return answer