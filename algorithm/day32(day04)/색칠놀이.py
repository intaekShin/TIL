# 3
# 2
# 2 2 4 4 1
# 3 3 6 6 2
# 3
# 1 2 3 3 1
# 3 6 6 8 1
# 2 3 5 6 2
# 3
# 1 4 8 5 1
# 1 8 3 9 1
# 3 2 5 8 2
import sys
sys.stdin = open("input.txt", "r", encoding='utf8')

# 0 리스트 만들어서 red: 1 채우고 blue : 2채워서 purple: 3 도출하면 됨. 끝!


T = int(input())    # T: Test case
for W in range(T):
    charae = W+1
    result = 0
    N = int(input())
    sagak = [0]*N
    for rac in range(N):
        sagak[rac] = list(map(int, input().split()))
    # print(sagak)    # 확인용 코드
    blank = [[0 for _ in range(10)] for _ in range(10)]

    for Q in range(N):
        if sagak[Q][4] == 1:
            for r in range(sagak[Q][1], sagak[Q][3]+1):   # r의 범위
               for c in range(sagak[Q][0], sagak[Q][2]+1 ):    # c의 범위
                   if not blank[r][c] == 1: # 중복 방지!
                       blank[r][c] += 1
        elif sagak[Q][4] == 2:
            for r in range(sagak[Q][1], sagak[Q][3]+1):
               for c in range(sagak[Q][0], sagak[Q][2]+1):
                   if not blank[r][c] == 2:
                       blank[r][c] += 2
    # for n in range(10):
    #     print(blank[n])     # 확인용 코드

    for gumsakan in blank:  # 하나씩 다 살피기 !
        for real in gumsakan:
            if real == 3:
                result += 1
    print('#%d %d' % (charae, result))
