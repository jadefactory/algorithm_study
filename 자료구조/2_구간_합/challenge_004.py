import sys
input_data = sys.stdin.readline

# n(리스트의 크기), m(구간 수)
n, m = map(int, input_data().split())

# A(원본 리스트), D(합 배열)
A = [[0]*(n+1)]
D = [[0]*(n+1) for _ in range(n+1)]

# 원본 리스트 데이터 저장
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# 합 배열 저장
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 구간 합에 대한 결과 계산 및 출력
for _ in range(m):
    x1, y1, x2, y2 = map(int, input_data().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)