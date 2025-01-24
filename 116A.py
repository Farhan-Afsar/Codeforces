n = int(input())

stops = []
current = 0
max_pass = 0

for _ in range(n):
    ai, bi = map(int, input().split())
    stops.append((ai, bi))


for a,b in stops:
    current -= a
    current +=b
    max_pass = max(current,max_pass)

print(max_pass)