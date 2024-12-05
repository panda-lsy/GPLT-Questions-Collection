N,sign = input().split() #将行数、符号自定义输入
N = int(N) #使行数的字符串输入转化为整数类型
line = 1 #初始定义单行个数为1
lines = [] #设置一个空集合，进行后续每行符号个数的汇集
lines.append(line) #表示在line每次更新数值后添加进入原先空集合
i = line #i表示输出时使用的符号总个数，但在此暂且赋值为1
while i<N: #给定程序运行环境
    line+=2 #令单行符号个数每次增加2
    i_=i #创建一个临时变量，若后续i>N时，便于返回原有i值
    i+=line*2 #计算在此次程序进程中所使用的符号总数量
    if i>N: #给定程序其中一个停止条件
        i=i_ #复归返回原初i值
        break #程序停止运行
    lines.append(line) #依次更新line值的变化并加入lines集合
    if i==N: #给定程序另一个停止条件
        i=i_ #复归返回原初i值
        break #程序停止运行
for u in range(len(lines)-1,0,-1): #倒序遍历lines，作为程序图案输出的上半部分
    ans = " "*((max(lines)-lines[u])//2)+sign*lines[u] #该程序前半部分表示该行需要的空格数，后半部分表示该行所需的符号个数，将两者相加链接
    print(ans) #输出图案的上半部分
for u in range(len(lines)): #正序遍历lines，作为程序图案输出的下半部分
    ans = " "*((max(lines)-lines[u])//2)+sign*lines[u] #该程序前半部分表示该行需要的空格数，后半部分表示该行所需的符号个数，将两者相加链接
    print(ans) #输出图案的下半部分
print(N-i) #输出给定可用符号数量的剩余个数