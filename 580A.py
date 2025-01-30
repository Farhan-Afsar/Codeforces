
n = int(input())

arr = list(map(int,input().split()))
current = 1
max_len = 1


for i in range(1,len(arr)):
    if arr[i] >= arr[i-1]:
        current += 1
    else:
        max_len = max(current,max_len)
        current = 1
max_len = max(current,max_len)
print(max_len)