# 백준 문제 10773번 : 제로
# Memory 29980KB / Time 112ms
from sys import stdin

K = int(stdin.readline())
stack_list = [0]

for i in range(K):
    number = int(stdin.readline())

    if number != 0:
        stack_list.append(number)
        
    else:
        stack_list.pop()

print(sum(stack_list))