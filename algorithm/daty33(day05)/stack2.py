# 괄호의 짝을 검사하는 프로그램
import sys
sys.stdin = open("input.txt", "r")

stack = [0]* 100
top = -1

Info = [0]*128  # char 1byte ASCII code 7bit 어떤 문자를 쓰든 128을 넘지 않는다.
Data =

Info[ord(')')] = '('
Info[ord(']')] ='['
Info[ord('>')] ='<'

howmany = len(Data)


for i in range(howmany):
    if Data[i] == '(' or Data[i] == '{' or Data[i] == '[' or Data[i] == '<':
        top += 1
        stack[top] = Data[i]
    elif info[ord(Data[i])] == stack[top] : # ?
        top -= 1
