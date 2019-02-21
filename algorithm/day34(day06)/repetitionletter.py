import sys
sys.stdin = open('input2.txt', 'r')

# 반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
# 왼쪽부터 검색.

T = int(input())

for t in range(1, T+1):
    Data = list(map(str, input()))

    Stack = [0] * len(Data)
    top = -1

    for lett in range(len(Data)):
        # print(lett)
        top = top + 1
        Stack[top] = Data[lett]
        if Stack[top] == Stack[top-1]:
            # print(Stack[top], Stack[top-1]) # 빼는 글자 확인
            Stack.pop(top)
            Stack.pop(top-1)
            top = top - 2
            # print(Stack)    # 빼고 난 후 중간 결과 확인

    # print('%s 는 최종결과입니다 :)' %Stack)
    print(f'#{t} {top+1}')


# 반복문으로 접근 했으나 실패한 코드 ( 배움에 도움이 된다.)
# for letter in range(giri):
#     if Data[letter] == Data[letter-1]:
#         Data.pop(letter)
#         Data.pop(letter-1)
#         print(Data)
#         print(letter+1)
#         print(len(Data))
#         if len(Data) <= letter:
#              = 0
#             print('%d은 변경되었습니다.' %letter )




