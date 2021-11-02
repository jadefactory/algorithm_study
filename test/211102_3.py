# 프로그래머스 문제 67258번 : 보석 쇼핑
def solution(gems):

    n = len(set(gems))
    
    if n == 1:
        return [1, 1]
    
    current_dict = dict()
    candidate = list()
    
    left = 0
    right = 0
    
    current_dict[gems[0]] = 1
    is_candidate = False
    
    while True:
        if is_candidate == True:
            left += 1
            current_dict[gems[left - 1]] -= 1
            
            if current_dict[gems[left - 1]] == 0:
                
                del current_dict[gems[left-1]]
                is_candidate = False
            
            else:
                candidate.append([left + 1 , right + 1])
        
        else:
            right += 1
            
            if right >= len(gems):
                break
                
            if gems[right] not in current_dict:
                
                current_dict[gems[right]] = 0
            
            current_dict[gems[right]] += 1
            
            if len(current_dict) == n:
                is_candidate = True
                candidate.append([left + 1, right + 1])
                
    candidate.sort(key=lambda x: x[1] - x[0])
    
    return candidate[0]