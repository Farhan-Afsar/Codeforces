t = int(input())

while t>0:

    n = int(input())
    arr = list(map(int,input().split()))

    a = set(arr)

    for i in range(n):
        if arr.count(arr[i]) == 1:
            print(i+1)
            break
    t-=1