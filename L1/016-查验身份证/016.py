N=int(input())
quality=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
Z=[0,1,2,3,4,5,6,7,8,9,10]
M=[1,0,'X',9,8,7,6,5,4,3,2]
AP=False
for i in range(N):
    num=input()
    temp=0
    if num[:-1].isdigit()!=True:
        print(num)
        AP=True
    else:
        for u in range(len(num)-1):
            temp+=int(num[u])*quality[u]
        Z0=temp%11
        if str(M[Z.index(Z0)])!=num[17]:
            print(num)
            AP=True
if AP==False:
    print('All passed')
