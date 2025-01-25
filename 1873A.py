t = int(input())

while t>0:
    s = input()

    s_list = list(s)

    if(s[0]=='a' or s[1]=='b' or s[2]=='c'):
        print("YES")
    else:
        print("NO")

    t-=1