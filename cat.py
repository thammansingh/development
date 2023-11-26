t=()
sum1=()
for i in range(5):
    print("enter marks of student no.",i+1)
    mark=()
    m1=int(input("enter marks of 1st subject= "))
    m2=int(input("enter marks of 2nd subject= "))
    m3=int(input("enter marks of 3rd subject = "))
    print()
    mark=(m1 , m2 , m3)
    t=t + (mark,)
    print("tuple" ,t)
sum1=t[i][0]+t[i][1]+t[i][2]
print(sum1)   

