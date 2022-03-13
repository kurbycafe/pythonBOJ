
for _ in range(0,3):
    a = []
    a = input().split(" ")
    a = list(map(int, a))
    b = a[0] * 60 * 60 + a[1] * 60 + a[2]
    c = a[3] * 60 * 60 + a[4] * 60 + a[5]
    timeDifference = c-b
    h = timeDifference // 60 // 60 % 24
    m = timeDifference // 60 % 60
    s = timeDifference % 60
    print(h, m, s)
