n = int(input())

if n % 2 == 0:
    total_sum = n // 2
else:
    total_sum = -(n + 1) // 2

print(total_sum)
