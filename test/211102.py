# 프로그래머스 문제 72412번 : 순위 검색
def solution(info, query):
    infos = [i.split() for i in info]
    queries = []
    
    for q in query:
        
        q = q.split()
        
        for i in range(3):
            q.remove('and')
            
        queries.append(q)
        
    answer = [0] * len(query)
    
    for i in range(len(queries)):
        
        for info_item in infos:
            
            for k in range(5):
                
                if queries[i][k] == '-':
                    continue
                    
                elif k == 4:
                    
                    if int(info_item[k]) >= int(queries[i][k]):
                        answer[i] += 1
                        
                elif info_item[k] != queries[i][k]:
                    
                    break
                    
    return answer