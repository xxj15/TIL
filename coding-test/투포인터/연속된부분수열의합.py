def solution(sequence, k):
    answer = [0, len(sequence)-1]
    left, right = 0, 0
    summ = sequence[0]
    
    while left<= right and right < len(sequence):
        if summ == k:
            if right - left < answer[1]-answer[0]:
                answer = [left, right]
            
            summ -= sequence[left]
            left += 1
        
        elif summ > k :
            summ -= sequence[left]
            left += 1

        else:
            right += 1
            if right < len(sequence):
                summ += sequence[right]

    return answer