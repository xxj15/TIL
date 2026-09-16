import math
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    numbers.sort()

    visited = [-1]* len(numbers)
    ans = set()
    
    def is_prime(num):
        if num < 2 :
            return False
        else:
            for i in range(2, int(math.sqrt(num))+1 ):
                if num % i == 0 :
                    return False
        return True
    
    def dfs(number):
        if number and is_prime(int(number)):
            ans.add(int(number))
        
        for i in range(len(numbers)):
            if visited[i] == -1:
                visited[i]=1
                dfs(number + numbers[i])
                visited[i]=-1
    
    dfs('')
        
    return len(ans)