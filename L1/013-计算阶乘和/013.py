N=int(input())
S=0
for u in range(1,N+1):
    temp=1
    for i in range(1,u+1):
        temp*=i
    S+=temp
print(S)