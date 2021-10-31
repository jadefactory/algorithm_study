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