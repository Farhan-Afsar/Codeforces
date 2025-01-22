t = int(input())

while t > 0:

    n = int(input())

    arr = []

    arr = list(map(int, input().split()))

    arr_sum = 0
    count = 0

    even = []
    odd = []

    for i in range(n):
        if arr[i] % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])

    arr = even + odd

    for i in range(n):

        arr_sum += arr[i]

        if arr_sum % 2 == 0:
            count += 1
            while  arr_sum % 2 == 0:
                arr_sum //= 2


    print(count)


    t -= 1

