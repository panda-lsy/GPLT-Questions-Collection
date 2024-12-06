N=int(input())
count_list,count_list_temp=[],[]

for i in range(2,int(N**0.5)+1):
    if N%i==0:  #第一重循环
        N_temp=N
        start=i
        while N_temp%start==0:  #第二重循环
            N_temp//=start
            count_list_temp.append(start)
            start+=1
        if len(count_list_temp)>len(count_list):    #判断
            count_list=count_list_temp
        count_list_temp=[]
            
if len(count_list)==0:
    print(1)
    print(N)
else:
    print(len(count_list))
    print('*'.join(map(str,count_list)))