arr = []

arr = list(map(int, input().split()))

arr_set = set(arr)

print(len(arr)-len(arr_set))

