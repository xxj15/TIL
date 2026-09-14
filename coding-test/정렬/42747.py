# H-index
def solution(citations):
    answer = 0
    h = len(citations)
    
    while True:
        large = sum(x >= h for x in citations)
    
        if large>=h:
            break
        h-=1
        
    answer = h
        
    
    return answer

# 정렬 이용한 풀이 
# def solution(citations):
#     answer = 0
#     h = len(citations)
    
#     while True:
#         large = sum(x >= h for x in citations)
    
#         if large>=h:
#             break
#         h-=1
        
#     answer = h
        
    
#     return answer