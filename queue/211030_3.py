# 백준 문제 3190번 : 뱀
# Memory 33680KB / Time 148ms
from sys import stdin
from collections import deque
# import pprint

N = int(stdin.readline())
K = int(stdin.readline())

# 사방이 벽(1)으로 둘러싸인 N x N 보드 만들기 => 지금부터 숫자 1을 벽이라고 생각하자
# 이렇게 만들면 주어진 좌표의 인덱스를 그대로 사용할 수 있는 장점이 있다
board = [[1] * (N + 2)] + [[1] + [0] * N + [1] for _ in range(N)] + [[1] * (N + 2)]

# 사과 위치 표시 => 지금부터 숫자 6을 사과라고 생각하자
for _ in range(K):
    apple_x, apple_y = map(int, stdin.readline().split())
    board[apple_x][apple_y] = 6

# 보드와 사과의 배치 확인하기
# pprint.pprint(board)

# 뱀의 방향 전환 횟수
L = int(stdin.readline())

# 뱀의 방향 전환 상세 정보 저장
moves = []
for _ in range(L):
    info = list(stdin.readline().split())
    info[0] = int(info[0])
    moves.append(info)

# 첫 시작은 0초부터 시작
time = 0

# 뱀의 초기 위치
x, y = 1, 1

# 0: 위쪽, 1: 오른쪽, 2: 아래쪽, 3: 왼쪽 => 좌표평면상에서의 이동을 숫자로 정의
direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

# 첫 방향은 오른쪽
toward = 1

# 뱀의 위치를 큐로 표현하자
# 양방향에서 추가와 삭제가 가능한 deque 사용하기
snake_queue = deque([[1, 1]])


# 뱀 위치 표시 => 지금부터 숫자 2를 뱀이라고 생각하자
board[1][1] = 2

# 0:빈 공간, 1:벽, 2:뱀, 6:사과
# 뱀은 매 초마다 이동한다
while True:
    # 지정된 방향으로 뱀의 머리를 이동시킨다
    x = x + direction[toward][0]
    y = y + direction[toward][1]

    # 이동한 위치에 사과(6)가 있다면
    if board[x][y] == 6:
        # 해당 위치에 사과 대신에 뱀의 머리를 놓는다
        board[x][y] = 2
        # snake_queue의 오른쪽 원소는 머리, 왼쪽 원소는 꼬리를 의미한다
        snake_queue.append([x, y])

        time += 1

    # 이동한 위치에 사과가 없고 빈 공간(0)이라면
    elif board[x][y] == 0:
        board[x][y] = 2
        snake_queue.append([x, y])

        # 뱀의 전체 길이는 변하지 않는다 => 이동한 후에는 꼬리를 제거한다
        pre_x, pre_y = snake_queue.popleft()
        board[pre_x][pre_y] = 0

        time += 1

    # 이동한 위치가 벽(1)이거나 자기 자신(2)이라면
    else:
        time += 1
        break

    # 뱀의 방향 전환 명령 처리
    if len(moves) != 0:
        # 지금이 방향을 전환할 타이밍이라면
        if moves[0][0] == time:
            # 'L'인 경우 왼쪽으로 90도 회전
            if moves[0][1] == 'L':
                toward = (toward - 1) % 4
            # 'D'인 경우 오른쪽으로 90도 회전
            elif moves[0][1] == 'D':
                toward = (toward + 1) % 4
            
            # 방향 전환이 완료된 후에는 해당 명령 제거
            del moves[0]

print(time)