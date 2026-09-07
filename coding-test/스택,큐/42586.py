# 기능개발 
import math
def solution(progresses, speeds):
    answer = []
    need_time = []
    for i in range(len(progresses)):
        time = math.ceil((100-progresses[i])/speeds[i])
        need_time.append(time)
    
    i=0
    while i<=len(progresses)-1:
        cnt = 1
        for j in range(i+1, len(need_time)):
            if need_time[i]>=need_time[j]:
                cnt += 1
                
            else:
                break
        answer.append(cnt)
        i += cnt
    
    return answer