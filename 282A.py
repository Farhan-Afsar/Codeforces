t = int(input())

val = 0

for _ in range(t):
    s = input().strip()
    if s[1] == '+':
        val += 1
    else:
        val -= 1

print(val)
