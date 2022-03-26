n = int(input())
cnt=0
l = []
for i in range(n):
    cnt = float(input())
    l.append(cnt)

l.sort()
print(l[1])