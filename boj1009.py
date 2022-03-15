on = []
cnt = 0
for _ in range(0,4):
    a,b = map(int,input().split(" "))
    cnt+=(b-a)
    on.append(cnt)

print(max(on))
