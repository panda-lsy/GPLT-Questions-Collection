N=input()
N_list=[int(D) for D in N]  #统计所有的字符串形式数字并转换为整型，储存在列表之中
N_list.sort()   #将列表的元素按照从小到大顺序排列
N_list_=[]  #创建一个空列表，用于筛选数字种类
Ms=[]   #创建根据数字种类绑定其出现次数的列表
for num in N_list:
    if num in N_list_:  
        Ms[N_list_.index(num)]+=1   
    else:
        Ms.append(1)
        N_list_.append(num)
for D in N_list_:
    print(f'{D}:{Ms[N_list_.index(D)]}')
