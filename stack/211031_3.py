# 백준 문제 9012번 : 괄호
# Memory 29200KB / Time 72ms
from sys import stdin

T = int(stdin.readline())
answer = None

for _ in range(T):
    L_count = 0
    R_count = 0
    arr = list(stdin.readline().strip())

    for i in range(len(arr)):

        if arr[i] == '(':
            L_count += 1

        else:
            R_count += 1
            
            if R_count > L_count:
                answer = 'NO'
                break

    if L_count != R_count:
        answer = 'NO'

    else:
        answer = 'YES'

    print(answer)