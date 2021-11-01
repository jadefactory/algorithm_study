# 백준 문제 1021번 : 회전하는 큐
# Memory 29200KB / Time 68ms
from sys import stdin

N, M = map(int, stdin.readline().split())
location = list(map(int,stdin.readline().split()))

queue = [i for i in range(1, N + 1)]
count = 0

for i in range(M):
    queue_length = len(queue)
    queue_index = queue.index(location[i])

    if queue_index < queue_length - queue_index:
        while True:
            if queue[0] == location[i]:
                del queue[0]
                break
            else:
                queue.append(queue[0])
                del queue[0]
                count += 1
    else:
        while True:
            if queue[0] == location[i]:
                del queue[0]
                break
            else:
                queue.insert(0, queue[-1])
                del queue[-1]
                count += 1

print(count)

