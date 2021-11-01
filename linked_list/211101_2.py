# 백준 문제 1158번 : 요세푸스 문제
# Memory 29708KB / Time 84ms
N, K = map(int, input().split())
people = [i for i in range(1, N + 1)]

josephus = []
del_index = 0

for _ in range(N):
    del_index += K-1

    if del_index >= len(people):
        del_index = del_index % len(people)

    josephus.append(str(people.pop(del_index)))

answer = ', '.join(josephus)

print('<{}>'.format(answer))