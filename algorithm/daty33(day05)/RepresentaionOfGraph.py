import sys
sys.stdin = open("input.txt", "r", encoding='utf8')


MyMap = [[0]*8 for i in range(8)]
visited = [0] *8    # 재방문 금지
def DFS(here):
    print(here, end="-")
    visited[here] = True

    for next in range(8):
        if MyMap[here][next] and not visited[next]:
            DFS(next)

Data = list(map(int, input().split()))
howmany = int(len(Data) / 2)


for i in range(howmany):
    Start = Data[i*2]
    Stop = Data[i*2+1]
    MyMap[Start][Stop] = 1
    MyMap[Stop][Start] = 1

DFS(1)