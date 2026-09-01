from collections import deque

def solution(queue1, queue2):
    n = (len(queue1)+len(queue2))*2
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    cnt = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    if (sum1+sum2)%2 :
        return -1 
    
    while True:
        if sum1 == sum2:
            return cnt

        if cnt >= n:
            return -1

        if sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
        else:
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
            sum2 -= num
        cnt += 1
    return cnt