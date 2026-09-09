# 할인 행사 
from collections import Counter
def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        cnt_dict = Counter(discount[i:i+10])
        for idx, fruit in enumerate(want):
            if cnt_dict[fruit] < number[idx]:
                break
        else:
            answer+=1
    return answer