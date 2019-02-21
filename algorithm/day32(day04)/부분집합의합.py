# 3
# 3 6
# 5 15
# 5 10
import sys
sys.stdin = open("input.txt", "r", encoding='utf8')


# T = int(input())
# N, K = list(map(int, input().split()))
# print(N)
# print(K)
# # result = ?
# jiphap = [0]*N
# for element in range(N):
#     jiphap[element] = element+1
# print(jiphap)
# print(1<<N)

# < 참고: 비트 연산자 >
# arr = [1, 2, 3]
# n = len(arr)
# for i in range(1<<n) :
#     for j in range(n) :
#         if i & (1<<j) :   # 0이 아닌 값은 True다.
#             print(arr[j], end=", ")   # for j 문이 끝날 때까지 같은 줄에 출력하기
#     print()   # 세로로 한줄 띄우기
# print()



arr = [1, 2, 3]
n = len(arr)
dab = [0]*(1<<n)
print(dab)
for i in range(1<<n) :
    for j in range(n) :
        if i & (1<<j) :   # 0이 아닌 값은 True다.
            dab[i][j] = (arr[j])   # for j 문이 끝날 때까지 같은 줄에 출력하기

print(dab)

# 위 목록 중에 길이가 N 이고(&) 합이 K인지 비교한 후 개수를 센다.
# 길이 N 측정 : 문자열을 리스트로 바꾸기. 집합변수.split(,)
