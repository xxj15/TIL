# 귤 고르기 

from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    tangerine_num = defaultdict(int)
    
    for t in tangerine:
        tangerine_num[t]+=1
    tangerine_num = sorted(tangerine_num.items(), key = lambda x:x[1],reverse=True)
    
    for key, value in tangerine_num:
        if k - value<=0:
            answer += 1 
            break
        k-= value
        answer += 1
    return answer