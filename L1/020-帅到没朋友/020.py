N=int(input())
IDs=set()
for i in range(N):
    inp_list=list(map(int,input().split()))
    K=inp_list[0]
    if int(K)>1:
        IDs=IDs | set(map(int,inp_list[1:]))
M=int(input())
IDs_=list(map(int,input().split()))
oplist=[]
for ID in IDs_:
    if not ID in IDs and not ID in oplist:
        oplist.append(ID)
if len(oplist)!=0:
    oplist=list(map(str,oplist))
    print(' '.join(oplist))
else:
    print('No one is handsome')