## CASE 1

import sys

# 과목의 수
N = sys.stdin.readline().strip()

# 점수 정보
scores = list(map(int, sys.stdin.readline().strip().split()))

# 점수 정보 중 최대값 저장
max_score = max(scores)

# 조정 점수로 변환
adj_scores = []
for score in scores:
    adj_score = score / max_score * 100
    adj_scores.append(adj_score)

# 조정 점수의 평균 저장
answer = sum(adj_scores) / int(N)

# 결과 출력
print(answer)

#################################################################

## CASE 2

import sys

# 과목의 수
N = sys.stdin.readline().strip()

# 점수 정보 저장
scores = list(map(int, sys.stdin.readline().strip().split()))

# 점수 정보 중 최대값 저장
max_score = max(scores)

# 점수의 합 
sum_score = sum(scores)

# 결과값 출력
print(sum_score * 100 / max_score / int(N))