t = int(input())

while t> 0:
    n = input().strip()

    n = n[:-2] + 'i'

    print(n)

    t -= 1