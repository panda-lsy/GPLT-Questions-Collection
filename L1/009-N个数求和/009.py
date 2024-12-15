N=int(input())
nums=list(input().split())
nums0=[]
nums1=[]
num0=0
num1=1
#化简
def ease(num0,num1):
    for i in range(int(num1**0.5)+1,1,-1):
        if abs(num0)%i==0 and abs(num1)%i==0 and num0!=0:
            num0//=i
            num1//=i
    return(num0,num1)
#获取所有分子、分母
for num in nums:
    temp=list(num.split('/'))
    #两项分子通分
    num0=num0*(int(temp[1]))+(int(temp[0]))*num1
    num1*=(int(temp[1]))
    num0,num1=ease(num0,num1)
nums1_=nums1[:]
if num0==0:
    print(0)
elif abs(num0)>=abs(num1):
    if abs(num0)%abs(num1)==0:
        print(num0//num1)
    else:
        ans0=num0//num1
        num0=num0%num1
        print(f'{ans0} {num0}/{num1}')
else:
    print(f'{num0}/{num1}')