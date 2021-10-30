# 백준 문제 3190번 : 뱀
# 틀렸습니다
from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())

apples = []
for _ in range(K):
    apple_position = tuple(map(int, stdin.readline().split()))
    apples.append(apple_position)

L = int(stdin.readline())

moves = []
for _ in range(L):
    directions = list(stdin.readline().split())
    directions[0] = int(directions[0])
    moves.append(tuple(directions))


# 0으로 채운 N x N 보드 만들기
board = [[0] * N for i in range(N)]

# 사과 정보 보드에 넣기
for x, y in apples:
    # 현재 사과 위치
    board[x][y] = 1

# 뱀 위치
snake = [(1,1)]
direction = [(0,1), (1,0), (0,-1), (-1,0)] # 오른쪽, 아래쪽, 왼쪽, 위쪽
first_direction = 0 
second = 0
x, y = 1, 1 # 처음 시작 위치

while True:
    second += 1
    # 머리의 위치
    x += direction[first_direction][0]
    y += direction[first_direction][1]

    # 좌표가 보드의 범위 내에 있다면
    if 1 <= x <= N and 1 <= y <= N:
        # 뱀 길이 증가
        snake.append((x, y))

        # 머리를 제외한 나머지 부분
        for i in snake[:-1]:
            # 자기 자신의 위치와 겹치는 부분이 있다면(자기 자신과 충돌한 경우라면)
            if (x, y) == i:
                break

        # 머리가 도달한 곳이 비어있는 보드라면
        if board[x][y] == 0:
            # 꼬리 제거
            snake.pop(0)

        # 이동한 위치에 사과가 있었다면
        if board[x][y] == 1:
            # 뱀이 사과를 먹는다 => 사과가 있던 위치를 0으로 바꾸기
            # 머리가 늘어나고 꼬리는 그대로 유지되기 때문에 꼬리는 제거하지 않음
            board[x][y] = 0

    # 좌표가 보드 범위를 벗어난 경우
    else:
        break

    # moves에 값이 존재하고 현재 시점에 moves의 동작이 진행되어야 한다면 
    if moves and second == int(moves[0][0]):
        # 오른쪽으로 90도 회전해야 한다면
        if moves[0][1] == 'D':
            # 이동 방향이 4가지(오른쪽, 아래쪽, 왼쪽, 위쪽)이므로
            first_direction = (first_direction + 1) % 4 
            moves.pop(0)

        # 왼쪽으로 90도 회전해야 한다면
        else:
            first_direction = (first_direction - 1) % 4
            moves.pop(0)

print(second)