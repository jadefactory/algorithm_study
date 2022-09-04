import sys

# N(숫자 개수), M(구간 개수)
N, M = map(int, sys.stdin.readline().strip().split())

# 숫자 데이터 저장
numbers = list(map(int, sys.stdin.readline().strip().split()))

# 구간 합을 저장할 리스트. 
# 리스트의 첫 번째 요소에는 0을 할당 : 숫자 데이터 리스트의 첫 번째 요소를 인덱싱 하기 위해
sum_list = [0]

# 구간 합을 저장할 변수 선언
sum_result = 0

# 숫자 데이터를 차례대로 탐색
for number in numbers:
    # sum_result에 현재 숫자 데이터 더해주기
    sum_result += number
    # 구간 합 리스트에 sum_result 값 저장
    sum_list.append(sum_result)

# 구간 개수만큼 반복 실행
for _ in range(M):
    # 구간 정보 수집
    start, end = map(int, sys.stdin.readline().strip().split())
    # 구간 합 출력
    print(sum_list[end] - sum_list[start-1])