import time
def calcTimeInSec(a,b,c,second):
    min, sec = divmod(second, 60)
    hour, min = divmod(min, 60)
    a+=hour;b+=min;c+=sec
    if(a>23 or b >59 or c>59):
        b += (c / 60);c %= 60
        a += (b / 60); b %= 60
        a %=24
    return "%d %d %d" % (a,b,c)

while(True):
    a,b,c = map(int, input().split())
    d = int(input())
    print(calcTimeInSec(a,b,c,d))




