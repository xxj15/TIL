# 영어 끝말잇기
def solution(n, words):
    answer = [0,0]
    word_list = set()
    
    
    for idx, word in enumerate(words):
        if word in word_list or (idx>0 and words[idx-1][-1] != word[0]):
            answer = [idx%n+1, idx//n+1]
            break
        word_list.add(word)
        

    return answer