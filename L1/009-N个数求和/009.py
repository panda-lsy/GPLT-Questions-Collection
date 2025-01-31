def GCD(a,b):
    max_num=max(abs(a),abs(b))
    min_num=min(abs(a),abs(b))
    while max_num%min_num:
        max_num,min_num=min_num,max_num%min_num
    return min_num

N=int(input())
list0=list(input().split())
if N>=2:
    for i in range(N-1):
        a0,d0=map(int,list0[i].split('/'))
        a1,d1=map(int,list0[i+1].split('/'))
        if a1!=0 and a0!=0:
            d=GCD(d0,d1)
            a=int(a0*(d1//d)+a1*(d0//d))
            d=int(d0*(d1//d))
            list0[i+1]=str(a)+'/'+str(d)
        elif a1==0:
            list0[i+1]=str(a0)+'/'+str(d0)

a,d=map(int,list0[len(list0)-1].split('/'))
if a!=0 and d!=0:
    m=GCD(a,d)
    a,d=a//m,d//m
    if abs(a)>=d:
        if abs(a)%d!=0:
            if a>0:
                print(f'{a//d} {a%d}/{d}')
            if a<0:
                print(f'{-(abs(a)//d)} {-(abs(a)%d)}/{d}')
        else:
            if a>0:
                print(f'{a//d}')
            if a<0:
                print(f'{-(abs(a)//d)}')
    else:
        print(f'{a}/{d}')
else:
    print(0)