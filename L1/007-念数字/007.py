list0=['-','0','1','2','3','4','5','6','7','8','9']
list1=['fu','ling','yi','er','san','si','wu','liu','qi','ba','jiu']
ans=[]
num=input()
for string in num:
    ans.append(list1[list0.index(string)])
print(' '.join(ans))