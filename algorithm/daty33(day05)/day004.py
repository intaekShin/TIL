import sys
sys.stdin = open("input.txt", "r")

stack = [0]*10 # 시험지에서는 10000칸 정도가 주어진다.
top = -1

for i in range(1, 4):
    top += 1
    stack[top] = i
    # stack.append(i)

while top != -1 :
    print(stack[top])
    top -= 1
    # while stack:
    # print(stack.pop())