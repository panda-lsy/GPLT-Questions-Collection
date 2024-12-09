A,B=map(int,input().split())
count=0
Sum=0
for i in range(A,B+1):
    str_i=str(i)
    print(f"{' '*(5-len(str_i))}{i}",end='')
    count+=1
    Sum+=i
    if count==5:
        print('')#默认end='\n',通过输出空字符空一行
        count-=5
if count!=0:#防止空两行
    print('')
print(f'Sum = {Sum}')
