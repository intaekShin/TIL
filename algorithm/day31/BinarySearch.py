import sys
sys.stdin = open("input.txt", "r")

mokpyo = 7
result = 'not founding'
bs = list(map(int, input().split()))
print (bs)
start = 0
end = len(bs)
index = (start+end)//2
jungang = bs[index]
while mokpyo != jungang:
    if mokpyo < jungang:
        end = index-1
        index = (start+end)//2
        jungang = bs[index]
    elif mokpyo > jungang:
        start = index+1
        index = (start + end) // 2
        jungang = bs[index]
if mokpyo == jungang:
    result = 'search success'

print(result)
print(start)


