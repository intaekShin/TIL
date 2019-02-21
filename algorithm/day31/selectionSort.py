import sys
sys.stdin = open("input.txt", "r")

def select(list, k) :
    for i in range(0, k) :
        minIndex = i
        for j in range (i+1, len(list)) :
            if list[minIndex] > list[j] :
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list[k-1]

def selectionSort(a) :
    for i in range(0, len(a)-1) :
        min = i
        for j in range(i+1, len(a)) :
            if a[min] > a[j] :
                min = j
        a[i], a[min] = a[min], a[i]

Data = [[0 for _ in range(5)] for _ in range(5)]
result = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5) :
    Data[i] = list(map(int, input().split()))


for change_list in range(5):
    for change_num in range(5):
        for list_num in range(5):
            for index in range(5):
                if Data[change_list][change_num] > Data[list_num][index]:
                    Data[change_list][change_num], Data[list_num][index] = Data[list_num][index], Data[change_list][change_num]
        result[change_list][change_num] = Data[change_list][change_num] # 순서대로 온 숫자를 차곡차곡 쌓아놓자.
        Data[change_list][change_num] = 99    # 변경될 수 없이 큰 수나 아주 작은 수를 대입하자.

print(result)