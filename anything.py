Flag = True


while Flag:
    sum =0
    a= input()
    lenNum= len(a) +1
    stra = str(a)
    if a!='0':
        for i in stra:
            if i == "1":
                sum +=2
            elif i =="0":
                sum +=4
            else:
                sum+= 3
        sum +=lenNum
        print(sum)
    else:
        Flag=False


