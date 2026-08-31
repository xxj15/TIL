def solution(word):
    alphabet = ['A','E','I','O','U']
    answer = 0
    w = []
    
    def dfs(cur):
        nonlocal answer
        
        if ''.join(cur) == word:
            return True
        
        if len(cur)<5 :
            for i in range(5):
                cur.append(alphabet[i])
                answer+=1
                if dfs(cur):
                    return True
                cur.pop()
        
        return False
            
    dfs(w)
    
    return answer