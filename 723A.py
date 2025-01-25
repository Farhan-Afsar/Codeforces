arr = list(map(int,input().split()))

arr.sort()

distance = (arr[1] - arr[0]) + (arr[2] - arr[1])

print(distance)