# 백준 문제 10845번 : 큐
# Memory 29200KB / Time 80ms
from sys import stdin

N = int(stdin.readline())

queue = []
for _ in range(N):
    command = stdin.readline().strip()

    if command.find('push') != -1:
        elements = list(command.split())
        queue.append(int(elements[1]))

    if command == 'pop':
        if len(queue) > 0:
            print(queue[0])
            del queue[0]
        else:
            print(-1)

    if command == 'size':
        print(len(queue))

    if command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    if command == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)

    if command == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)