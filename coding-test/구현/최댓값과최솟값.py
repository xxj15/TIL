def solution(s):
    numbers = list(map(int, s.split()))
    max_num = max(numbers)
    min_num = min(numbers)
    answer = [min_num, max_num]
    
    return " ".join(map(str,answer))