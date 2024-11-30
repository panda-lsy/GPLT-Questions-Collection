N,sign=input().split()
N=int(N)    #储存给定符号数量
lines=[]    #记录每行符号个数
line=1      #初始行个数为1
lines.append(line)  
i=line      #输出时使用的符号总个数,暂赋值为1
while i<N:
    line+=2
    i_=i    #创建一个临时变量,若后续i>N时,返回原有i值
    i+=line*2
    if i>N:
        i=i_
        break
    lines.append(line)
    if i==N:
        i=i_
        break
for u in range(len(lines)-1,0,-1):  #倒序遍历lines,作为上半部分,忽略初始行的遍历留给后续遍历
    ans=' '*((max(lines)-lines[u])//2)+sign*lines[u]
    print(ans)
for u in range(len(lines)):#正序遍历lines,作为下半部分
    ans=' '*((max(lines)-lines[u])//2)+sign*lines[u]
    print(ans)
print(N-i)  #输出没用掉的符号数