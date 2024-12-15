num=input()
num0=num.count('2')
if '-' in num:
    ans=num0/(len(num)-1)
else:
    ans=num0/len(num)
if num[0]=='-':
    ans*=1.5
if int(num[len(num)-1])%2==0 or int(num[len(num)-1])==0:
    ans*=2
ans='%.2f'%(ans*100)
print(f'{ans}%')