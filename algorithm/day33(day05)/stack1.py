stack = [0] * 10
top = -1

for i in range (4):
    top +=1
    stack[top] = i*3

while top != -1:
    print(stack[top])
    top -= 1