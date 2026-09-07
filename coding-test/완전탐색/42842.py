def solution(brown, yellow):
    w, h = 1, 0
    while w >= h:
        h += 1
        if yellow % h != 0 :
            continue
        w = yellow // h 
        if (w+2) * (h+2) - yellow == brown:
            answer = [w+2, h+2]
            break
        
    return answer