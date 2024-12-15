HP1,HP2=map(int,input().split())
HP1_,HP2_=HP1,HP2
N=int(input())
end=False
for i in range(N):
    S1,H1,S2,H2=map(int,input().split())
    if end==False:
        if H1==S1+S2 and H2!=S1+S2:
            HP1-=1
        elif H2==S1+S2 and H1!=S1+S2:
            HP2-=1
        if HP1<0:
            print('A')
            print(HP2_-HP2)
            end=True
        elif HP2<0:
            print('B')
            print(HP1_-HP1)
            end=True