import sys
sys.stdin = open("input.txt", "r")

def IsNotWall(y, x):
    if x >= 0 and x < 5 and y >= 0 and y < 5 : return True #원하는 값이 트루로 하는것이 짜기에 편하다.
    else: return False

def Mycalc(a,b):
    if a > b : return a - b
    else: return b - a

Data = [[0 for _ in range(5)] for _ in range(5)]


for i in range(5) :
    Data[i] = list(map(int, input().split()))

print(Data)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

sum = 0
for y in range(5):
    for x in range(5):
        for dir in range(4):
            newY = y + dy[dir]
            newX = x + dx[dir]
            if IsNotWall(newY, newX):
                sum += Mycalc(Data[y][x], Data[newY][newX]) # 내 위치값, 차이의 절대값?

print(sum)