t = int(input())

while t > 0:

    arr = []

    arr = list(map(int, input().split()))

    if arr[0] == 1 and arr[1] == 1:
        print(1)

    elif arr[0] == arr[1] :
        print(0)

    else:
        print(arr[1]-arr[0])


    t -= 1
