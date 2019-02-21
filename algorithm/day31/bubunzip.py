import sys
sys.stdin = open("input.txt", "r")

L = list(map(int, input().split()))
n = len(L)
cnt = 0
for i in range(1<<n):
    result =[]
    for j in range(n+1):
        if i & (1<<j):
            result.append(L[j])
    if sum(result)==0:
        print(result)
        cnt += 1
print(cnt)