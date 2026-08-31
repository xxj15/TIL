# 1845번 - 해시 

def solution(nums):
    answer = 0
    amt = len(nums)/2
    new_nums = set(nums)
    if len(new_nums) <= amt:
        answer = len(new_nums)
    else:
        answer = amt
    
    return answer
