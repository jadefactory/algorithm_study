# 백준 문제 2161번 : 카드1
# Memory 34924KB / Time 120ms
import queue

N = int(input())

data = queue.Queue()

for i in range(N):
    data.put(i+1)

thrown_card = []
while data.qsize() != 1:
    thrown_card.append(data.get())
    remain_card = data.get()
    data.put(remain_card)

last_card = data.get()
thrown_card.append(last_card)

for i in thrown_card:
    print(int(i), end=' ')