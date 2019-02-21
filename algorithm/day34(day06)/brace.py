import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    # print(f'{t}는 테스트케이스 번호!')
    # Stack list 및 top 선언
    stack = [0] * 10
    top = -1
    # Infolist 및 Data 선언
    Info = [99] * 128
    Data = input()
    print(f'"{Data}"는 Data에서 뽑은 문장입니다.')
    # 닫는 괄호를 Info list에서 뽑으면 Info['닫는 괄호'] '여는 괄호'로 출력 하는 코드.
    Info[ord(')')] = '('
    Info[ord('}')] = '{'
    # print(Info)
    # 입력받은 내용의 길이를 변수로 선언
    howmany = len(Data)
    fail_flag = 0
    # 실제 괄호 검사
    for i in range(howmany):    #반복문
        if Data[i] == '{' or Data[i] == '(':    # 여는 괄호가 나오면
            top += 1    # Stack을 쌓는다.(가상의 개념) 순서를 카운트.
            stack[top] = Data[i]    # 실제 내용 쌓기
            # print('스택쌓기',Data[i], top, stack)
        elif Data[i] == '}' or Data[i] == ')':    # 닫는 괄호가 나오면
            if Info[ord(Data[i])] != stack[top]: # 여는 괄호와 같은 괄호인지 검사! 다르다면
                fail_flag = 1   # 검사를 끝내자.
        # elif Info[ord(Data[i])] == stack[top]:     # 닫는 괄호가 나오고 쌓은 스택과 일치(여는괄호와 닫는괄호의 종류가같음)하면
            stack[top] = 0
            top -= 1    # Stack을 뺀다.
            # print('빼기', Data[i], top, stack)
    if top == -1 and fail_flag == 0:
        print(f"#{t} 1")   # 괄호검사가 정상적으로 끝나면.
    else:
        print(f'#{t} 0')


