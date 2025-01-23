t = int(input())

while t>0:
    
    arr = []
    s = input()
    for i in s:
        arr.append(int(i))

    first_sum = 0
    last_sum = 0

    for i in range(0,3):
        first_sum+= arr[i]

    for i in range(len(arr)-3,len(arr)):
        last_sum+= arr[i]

    if first_sum == last_sum:
        print("YES")
    else:
        print("NO")
    t-=1