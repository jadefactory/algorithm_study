# 백준 문제 10828번 : 스택
# Memory 29200KB / Time 80ms
from sys import stdin

N = int(stdin.readline())

stack = []
for _ in range(N):
    command = stdin.readline().strip()

    if command.find('push') != -1:
        elements = list(command.split())
        stack.append(int(elements[1]))

    if command == 'pop':
        if len(stack) > 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)

    if command == 'size':
        print(len(stack))

    if command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if command == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)