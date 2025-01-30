s = input()

num = s.split('+')
num.sort()
s = '+'.join(num)
print(s)