t = int(input())

while t>0:
    n = int(input())

    arr = list(map(int,input().split()))

    score = 0
    a = set()

    for i in arr:
        if i in a:
             a.remove(i)
             score += 1
        else:
            a.add(i)
    
    print(score)
    
    t-=1