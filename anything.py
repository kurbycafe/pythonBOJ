max =0
for _ in range(2):
    sum=0
    a = []
    a = input().split(" ")
    for i in a:
        sum+=int(i)
        if(sum > max):
            max = sum

print(max)
