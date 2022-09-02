import sys

# n값 받기
n = sys.stdin.readline().strip()

# numbers 변수에 list 함수를 이용하여 숫자를 한 자리씩 나누어 받기
numbers = list(sys.stdin.readline().strip())

# 결과값을 저장할 answer 변수 선언
answer = 0

# numbers 변수 탐색
for num in numbers:
    # answer 변수에 numbers에 있는 각 자리수를 하나씩 가져와 더하기
    answer += int(num)

# 결과값 출력
print(answer)