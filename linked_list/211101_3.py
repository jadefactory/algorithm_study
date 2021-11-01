# 백준 문제 1406번 : 에디터
# Memory 39620KB / Time 328ms
from sys import stdin

str_list = list(stdin.readline().strip())
arr = []
N = len(str_list)
M = int(stdin.readline())

for i in range(M):
    command = stdin.readline().strip()

    if command[0] == 'P':
        str_list.append(command[2])

    elif command[0] == 'L' and str_list != []:
        arr.append(str_list.pop())

    elif command[0] == 'D' and arr != []:
        str_list.append(arr.pop())
        
    elif command[0] == 'B' and str_list != []:
        str_list.pop()

print(''.join(str_list + list(reversed(arr))))